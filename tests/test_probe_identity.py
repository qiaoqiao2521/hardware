import unittest

from hardwire.core.evidence import EvidenceBundle
from hardwire.core.probe import SystemProbe
from hardwire.benchmarks.matrix import BoardMatrix
from hardwire.core.diagnostic import DiagnosticEngine


class ProbeIdentityTests(unittest.TestCase):
    def collect_cpu_facts(self, **payload):
        bundle = SystemProbe.parse_raw_data(
            EvidenceBundle("fixture", "unknown"), payload
        )
        return {fact.key: fact.value for fact in bundle.facts if fact.category == "cpu"}

    def test_shared_arm_core_types_do_not_identify_soc_or_core_counts(self):
        for big_cores in (2, 4):
            with self.subTest(big_cores=big_cores):
                parts = ["0xd05"] * 4 + ["0xd0b"] * big_cores
                cpuinfo = "\n\n".join(
                    f"processor: {i}\nCPU part: {part}"
                    for i, part in enumerate(parts)
                )
                facts = self.collect_cpu_facts(
                    arch="aarch64", model="Radxa ROCK 5C",
                    cpuinfo=cpuinfo, nproc=str(len(parts)),
                )
                self.assertIn("Cortex-A76", facts["model_name"])
                self.assertIn("Cortex-A55", facts["model_name"])
                self.assertIn("unverified", facts["model_name"])
                self.assertNotIn("RK3588", facts["model_name"])
                self.assertNotIn("4×", facts["model_name"])
                self.assertEqual(facts["threads"], len(parts))

    def test_explicit_x86_cpu_name_is_preserved(self):
        facts = self.collect_cpu_facts(
            arch="x86_64", cpuname="Intel(R) Celeron(R) CPU J1900 @ 1.99GHz",
            nproc="4",
        )
        self.assertEqual(facts["model_name"], "Intel(R) Celeron(R) CPU J1900 @ 1.99GHz")

    def test_cpuinfo_hardware_name_is_preserved(self):
        facts = self.collect_cpu_facts(arch="aarch64", cpuinfo="Hardware: Test SoC")
        self.assertEqual(facts["model_name"], "Test SoC")

    def test_missing_cpu_name_does_not_crash(self):
        facts = self.collect_cpu_facts(arch="aarch64")
        self.assertEqual(facts["model_name"], "Generic aarch64 CPU")

    def test_device_tree_model_terminator_is_not_part_of_board_name(self):
        bundle = SystemProbe.parse_raw_data(EvidenceBundle("fixture", "unknown"),
                                          {"model": "RK3566 EVB2\x00\n"})
        model = next(f.value for f in bundle.facts if f.key == "board_model")
        self.assertEqual(model, "RK3566 EVB2")

    def test_interface_enumeration_does_not_claim_physical_connectivity(self):
        bundle = SystemProbe.parse_raw_data(EvidenceBundle("fixture", "unknown"), {
            "ip_a": "1: lo: <LOOPBACK,UP>\n2: eth0: <NO-CARRIER,BROADCAST> state DOWN\n"
                    "3: dummy0: <BROADCAST> state DOWN\n",
        })
        DiagnosticEngine.run_diagnostics(bundle)
        result = next(i for i in bundle.inferences if i.id == "NETWORK_LINK_DETECTED")
        self.assertEqual(result.evidence[0]["value"], ["eth0", "dummy0"])
        self.assertIn("枚举", result.claim)
        self.assertNotIn("已建立", result.claim)
        self.assertIn("不能证明", result.caveat)

    def test_matrix_separates_lite_specs_from_unverified_historical_benchmarks(self):
        output = BoardMatrix.render_markdown()
        specs = next(line for line in output.splitlines()
                     if line.startswith("| **Radxa ROCK 5C Lite") and "TOPS" in line)
        self.assertIn("RK3582", specs)
        self.assertIn("2 × A76", specs)
        self.assertIn("4 × A55", specs)
        self.assertIn("5 TOPS", specs)
        historical = next(line for line in output.splitlines()
                          if "ROCK 5C历史记录" in line)
        self.assertIn("型号未实证", historical)
        self.assertNotIn("1.2 个 N100", historical)
        self.assertNotIn("6 TOPS", output)


if __name__ == "__main__":
    unittest.main()
