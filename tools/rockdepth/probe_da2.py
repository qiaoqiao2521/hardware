#!/usr/bin/env python3
"""Read back a real RKNN prediction using the software owner's depth adapter."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import time


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_runtime(report: dict, expected_version: str, expected_sha256: str) -> None:
    """Verify loaded content, including namespace aliases with old file names."""
    version = re.search(r"\bAPI:\s*([^\s]+)", report["backend"]["sdk_version"])
    if not version or version.group(1) != expected_version:
        raise RuntimeError("Actually loaded RKNN API version differs from the frozen version")
    if not any(f["sha256"] == expected_sha256 for f in report["runtime_files"]):
        raise RuntimeError("Actually mapped RKNN library differs from the frozen library")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app-dir", type=Path, required=True)
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--expected-sha256", required=True)
    parser.add_argument("--reference-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--limit", type=int, default=1)
    parser.add_argument("--core", choices=("auto", "0", "1", "2"), default="auto")
    parser.add_argument("--expected-runtime-version", default="2.3.2")
    parser.add_argument("--expected-runtime-sha256",
                        default="d31fc19c85b85f6091b2bd0f6af9d962d5264a4e410bfb536402ec92bac738e8")
    args = parser.parse_args()
    if args.limit < 1 or digest(args.model) != args.expected_sha256:
        raise ValueError("Invalid frame limit or RKNN model hash")
    args.output_dir.mkdir(parents=True, exist_ok=False)
    sys.path.insert(0, str(args.app_dir.resolve()))
    import numpy as np
    from backends import RKNNDepthBackend, validate_depth

    manifest = json.loads((args.reference_dir / "reference.json").read_text())
    if len(manifest["frames"]) < args.limit:
        raise ValueError("Reference manifest has fewer frames than requested")
    backend = RKNNDepthBackend(args.model, input_size=(252, 448), core=args.core)
    report = {"backend": backend.metadata(), "core": args.core,
              "reference_video_sha256": manifest["video_sha256"],
              "operator_cpu_fallback": "five original align_corners Resize operators",
              "status": "running", "requested_frames": args.limit, "frames": []}
    try:
        report["runtime_mapping"] = sorted({line.split()[-1]
            for line in Path("/proc/self/maps").read_text().splitlines()
            if "librknnrt.so" in line})
        report["runtime_files"] = [{"path": p, "sha256": digest(Path(p))}
            for p in report["runtime_mapping"]]
        verify_runtime(report, args.expected_runtime_version, args.expected_runtime_sha256)
        report["render_device_handles"] = sorted({str(p.resolve())
            for p in Path("/proc/self/fd").iterdir()
            if str(p.resolve()).startswith("/dev/dri/")})
        (args.output_dir / "probe.json").write_text(json.dumps(report, indent=2))
        for item in manifest["frames"][:args.limit]:
            frame = item["id"]
            input_path = args.reference_dir / f"{frame}-input.npy"
            tensor = np.load(input_path, allow_pickle=False)
            if tensor.shape != (1, 3, 252, 448) or tensor.dtype != np.float32:
                raise ValueError("Input differs from the frozen float32 NCHW contract")
            input_hash = digest(input_path)
            tensor_hash = hashlib.sha256(tensor.tobytes()).hexdigest()
            if input_hash != item["input_sha256"]:
                raise ValueError("Input file digest differs from the reference")
            started = time.monotonic()
            depth = validate_depth(backend.infer_tensor(tensor))
            elapsed_ms = (time.monotonic() - started) * 1000
            if depth.shape != (252, 448):
                raise ValueError("RKNN output shape differs from the reference")
            output = args.output_dir / f"{frame}-rknn.npy"
            np.save(output, depth, allow_pickle=False)
            report["frames"].append({"id": frame, "input_sha256": input_hash,
                "tensor_sha256": tensor_hash,
                "output_sha256": digest(output), "inference_ms": elapsed_ms,
                "shape": list(depth.shape), "finite": True,
                "min": float(depth.min()), "max": float(depth.max())})
            (args.output_dir / "probe.json").write_text(json.dumps(report, indent=2))
            print(json.dumps(report["frames"][-1]), flush=True)
        report["status"] = "complete"
    finally:
        if sys.exc_info()[0] is not None:
            report["status"] = "failed"
            report["error_type"] = sys.exc_info()[0].__name__
        (args.output_dir / "probe.json").write_text(json.dumps(report, indent=2))
        backend.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
