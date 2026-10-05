import pathlib
import unittest


SKILL_PATH = pathlib.Path(__file__).resolve().parents[1] / "SKILL.md"
TEXT = SKILL_PATH.read_text(encoding="utf-8")


class EmbeddedFirmwareEngineerStartHereRoutingRound35Test(unittest.TestCase):
    def test_start_here_section_exists(self) -> None:
        self.assertIn("## Start Here", TEXT)
        self.assertIn('### Direct firmware implementation, bring-up, or debug request', TEXT)

    def test_direct_request_branch_sets_current_mode(self) -> None:
        self.assertIn(
            "Current mode: operate as a repo-first firmware implementation/debug specialist for the current board and toolchain, not as a generic embedded explainer.",
            TEXT,
        )

    def test_direct_request_branch_sets_first_action_and_blocker_rule(self) -> None:
        self.assertIn(
            "First action: inspect the existing repo, build files, linker/map config, pin/peripheral definitions, and any failing logs before proposing code changes.",
            TEXT,
        )
        self.assertIn(
            "Clarify only if blocked: ask concise follow-up questions only when the target MCU/board, framework/SDK, or failure symptom cannot be recovered from the repo or user-provided artifacts.",
            TEXT,
        )

    def test_direct_request_branch_sets_first_deliverable_order(self) -> None:
        self.assertIn("First deliverable order:", TEXT)
        self.assertIn("1. Confirmed target facts and assumptions", TEXT)
        self.assertIn("2. Concrete implementation or debug plan tied to the detected MCU/framework", TEXT)
        self.assertIn("3. Code/config changes or the exact files/commands to inspect next", TEXT)
        self.assertIn("4. Explicit hardware, timing, and safety risks", TEXT)


if __name__ == "__main__":
    unittest.main()
