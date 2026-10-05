import pathlib
import unittest


SKILL_PATH = pathlib.Path(__file__).resolve().parents[1] / "SKILL.md"
TEXT = SKILL_PATH.read_text(encoding="utf-8")


class EmbeddedFirmwareEngineerSmokeTest(unittest.TestCase):
    def test_frontmatter_and_title_exist(self) -> None:
        self.assertIn("name: embedded-firmware-engineer", TEXT)
        self.assertIn("description: Specialist in bare-metal and RTOS firmware", TEXT)
        self.assertIn("# Embedded Firmware Engineer", TEXT)

    def test_existing_core_sections_exist(self) -> None:
        self.assertIn("## 🎯 Your Core Mission", TEXT)
        self.assertIn("## 🔄 Your Workflow Process", TEXT)
        self.assertIn("## 🚀 Advanced Capabilities", TEXT)


if __name__ == "__main__":
    unittest.main()
