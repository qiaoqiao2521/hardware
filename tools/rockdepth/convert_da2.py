#!/usr/bin/env python3
"""Convert a fixed DA2 ONNX with external normalization using Toolkit2."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--expected-sha256", required=True)
    args = parser.parse_args()
    source_hash = hashlib.sha256(args.model.read_bytes()).hexdigest()
    if source_hash != args.expected_sha256:
        raise ValueError("ONNX source hash does not match the frozen reference")
    if args.output.exists():
        raise FileExistsError("Refusing to overwrite an existing RKNN artifact")

    from rknn.api import RKNN

    rknn = RKNN(verbose=True)
    try:
        # ONNX accepts normalized float NCHW. Preserve identity preprocessing.
        steps = (
            ("config", lambda: rknn.config(target_platform="rk3588")),
            ("load_onnx", lambda: rknn.load_onnx(model=str(args.model))),
            ("build", lambda: rknn.build(do_quantization=False)),
            ("export", lambda: rknn.export_rknn(str(args.output))),
        )
        for name, operation in steps:
            print(json.dumps({"phase": name, "status": "running"}), flush=True)
            code = operation()
            if code != 0:
                raise RuntimeError(f"RKNN {name} failed with status {code}")
        print(json.dumps({
            "status": "converted",
            "onnx_sha256": source_hash,
            "rknn_sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
            "target_platform": "rk3588",
            "quantization": False,
            "normalization": "external",
            "board_inference": "not_run",
        }), flush=True)
    finally:
        rknn.release()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
