"""Regress the observed SDK/system-library mismatch without loading any SDK."""

import copy
import importlib.util
from pathlib import Path
import unittest


SOURCE = Path(__file__).resolve().parents[1] / "tools/rockdepth/probe_da2.py"
SPEC = importlib.util.spec_from_file_location("rockdepth_probe", SOURCE)
PROBE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PROBE)


class RuntimeIdentityTests(unittest.TestCase):
    def setUp(self):
        self.report = {
            "backend": {"sdk_version": "RKNN VERSION:\n  API: 2.3.2 (build)\n  DRV: 0.9.6\n"},
            "runtime_files": [{"path": "/usr/lib/librknnrt.so.2.0.0b0", "sha256": "private-content"}],
        }

    def test_namespace_alias_name_does_not_override_verified_content(self):
        PROBE.verify_runtime(self.report, "2.3.2", "private-content")

    def test_old_library_api_is_rejected_even_with_expected_file_hash(self):
        old = copy.deepcopy(self.report)
        old["backend"]["sdk_version"] = "RKNN VERSION:\n  API: 2.0.0b0 (build)\n  DRV: 0.9.6\n"
        with self.assertRaisesRegex(RuntimeError, "API version"):
            PROBE.verify_runtime(old, "2.3.2", "private-content")

    def test_version_label_does_not_substitute_for_mapped_content(self):
        with self.assertRaisesRegex(RuntimeError, "mapped RKNN library"):
            PROBE.verify_runtime(self.report, "2.3.2", "different-content")

    def test_absent_runtime_mapping_is_rejected(self):
        self.report["runtime_files"] = []
        with self.assertRaisesRegex(RuntimeError, "mapped RKNN library"):
            PROBE.verify_runtime(self.report, "2.3.2", "private-content")


if __name__ == "__main__":
    unittest.main()
