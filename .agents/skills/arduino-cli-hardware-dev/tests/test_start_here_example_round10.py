from pathlib import Path
import unittest


SKILL_PATH = Path(__file__).resolve().parents[1] / "SKILL.md"


class StartHereExampleRound10Test(unittest.TestCase):
    def test_start_here_has_worked_example(self) -> None:
        text = SKILL_PATH.read_text(encoding="utf-8")

        # The Example block must appear inside the Direct compile/upload section
        self.assertIn("**Example:**", text)

        # Example must show a concrete user trigger and assistant response
        self.assertIn("User:", text)
        self.assertIn("Assistant:", text)

        # Example must reference arduino-cli compile + upload workflow
        self.assertIn("arduino-cli compile", text)
        self.assertIn("arduino-cli upload", text)

        # Example must show Entry Path Priority routing decision
        self.assertIn("New Windows scaffold", text)
        self.assertIn("scripts/init-project.ps1", text)

        # Example must show the assistant doing triage before running
        self.assertIn("COM", text)

    def test_example_appears_under_direct_compile_section(self) -> None:
        text = SKILL_PATH.read_text(encoding="utf-8")

        # Find the Direct compile section and verify example follows it
        direct_compile_pos = text.find("### Direct compile/upload request")
        example_pos = text.find("**Example:**", direct_compile_pos)

        self.assertNotEqual(
            example_pos, -1,
            "**Example:** block not found after '### Direct compile/upload request'"
        )

        # Example should come before the next major section
        existing_sketch_pos = text.find("### Existing sketch compile/upload")
        self.assertNotEqual(
            direct_compile_pos, -1,
            "'### Direct compile/upload request' section not found"
        )
        self.assertGreater(
            example_pos, direct_compile_pos,
            "**Example:** must appear after '### Direct compile/upload request'"
        )


if __name__ == "__main__":
    unittest.main()
