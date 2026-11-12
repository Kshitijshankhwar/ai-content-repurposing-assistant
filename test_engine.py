import unittest
from content_engine import build_prompt, demo_content_pack, quality_report, validate_pack

SOURCE = ("A college student named Maya discovers a note inside an old library book. "
          "She stays to investigate and hears footsteps behind the locked archive door.")
BRIEF = {"platform":"Instagram Reels","language":"English","tone":"Suspenseful","duration":30,"audience":"Young adults"}

class TestEngine(unittest.TestCase):
    def test_prompt_has_source_and_constraints(self):
        prompt = build_prompt(SOURCE, BRIEF)
        self.assertIn("Do not invent", prompt)
        self.assertIn(SOURCE, prompt)
    def test_demo_pack_shape(self):
        pack = demo_content_pack(SOURCE, BRIEF)
        self.assertEqual(len(pack["hooks"]), 5)
        self.assertEqual(len(pack["scripts"]), 3)
        self.assertEqual(len(pack["captions"]), 2)
        self.assertEqual(len(pack["ctas"]), 3)
    def test_quality_checks(self):
        report = quality_report(demo_content_pack(SOURCE, BRIEF), SOURCE)
        self.assertTrue(report["five_hooks_present"])
        self.assertTrue(report["all_hooks_at_most_15_words"])
        self.assertTrue(report["hooks_are_unique"])
    def test_reject_bad_pack(self):
        with self.assertRaises(ValueError):
            validate_pack({"hooks":[]})
    def test_reject_short_source(self):
        with self.assertRaises(ValueError):
            build_prompt("hello", BRIEF)
    def test_demo_not_general_ai(self):
        with self.assertRaises(ValueError):
            demo_content_pack("This is a different story about a train and a traveller. "*3, BRIEF)

if __name__ == "__main__":
    unittest.main()
