import pathlib
import unittest


SKILL_PATH = pathlib.Path(__file__).resolve().parents[1] / "SKILL.md"
TEXT = SKILL_PATH.read_text(encoding="utf-8")


class EmbeddedFirmwareEngineerFirstResponseShapeRound34Test(unittest.TestCase):
    def test_first_response_shape_section_exists(self) -> None:
        self.assertIn("## First Response Shape", TEXT)

    def test_first_response_shape_has_4_point_acknowledgment(self) -> None:
        self.assertIn("1. **Target confirmed**:", TEXT)
        self.assertIn("2. **Plan preview**:", TEXT)
        self.assertIn("3. **Next inspect**:", TEXT)
        self.assertIn("4. **Risk flag**:", TEXT)

    def test_first_response_shape_positioned_after_start_here(self) -> None:
        idx_start = TEXT.find("## Start Here")
        idx_first_resp = TEXT.find("## First Response Shape")
        idx_identity = TEXT.find("## 🧠 Your Identity & Memory")
        self.assertGreater(idx_first_resp, idx_start)
        self.assertLess(idx_first_resp, idx_identity)


if __name__ == "__main__":
    unittest.main()
