from pathlib import Path
import unittest


SKILL_PATH = Path(__file__).resolve().parents[1] / "SKILL.md"


class EntryPathPriorityRound10Test(unittest.TestCase):
    def test_skill_defines_entry_path_priority_for_common_branches(self) -> None:
        text = SKILL_PATH.read_text(encoding="utf-8")

        self.assertIn("## Entry Path Priority", text)
        self.assertIn("New Windows scaffold with no existing sketch", text)
        self.assertIn("start with `scripts/init-project.ps1`", text)
        self.assertIn("Existing sketch that needs compile/upload", text)
        self.assertIn("go straight to `references/workflow.md`", text)
        self.assertIn("WSL2 shell but only a Windows `COMx` port is visible", text)
        self.assertIn("prefer Windows `arduino-cli` with the `COMx` port first", text)
        self.assertIn(
            "Only stay in WSL for upload after USB pass-through exposes `/dev/ttyACM*` or `/dev/ttyUSB*`",
            text,
        )


if __name__ == "__main__":
    unittest.main()
