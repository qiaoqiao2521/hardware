from pathlib import Path
import unittest


SKILL_PATH = Path(__file__).resolve().parents[1] / "SKILL.md"


class SkillSmokeTest(unittest.TestCase):
    def test_frontmatter_and_key_resources_exist(self) -> None:
        text = SKILL_PATH.read_text(encoding="utf-8")

        self.assertIn("name: arduino-cli-hardware-dev", text)
        self.assertIn("description:", text)
        self.assertIn("scripts/init-project.ps1", text)
        self.assertIn("references/wsl2.md", text)


if __name__ == "__main__":
    unittest.main()
