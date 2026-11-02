import unittest
from pathlib import Path
from streamlit.testing.v1 import AppTest


class AppTests(unittest.TestCase):
    def test_dashboard_starts(self):
        app = AppTest.from_file(Path(__file__).resolve().parents[1] / "app.py").run(
            timeout=30
        )
        self.assertEqual(len(app.exception), 0, str(app.exception))

    def test_generate_and_policy_failure(self):
        app = AppTest.from_file(Path(__file__).resolve().parents[1] / "app.py").run()
        app.button[0].click().run()
        app.text_area(key="copy").set_value("practical progress carbon neutral").run()
        import json

        self.assertFalse(json.loads(app.json[0].value)["publishable"])
        self.assertEqual(len(app.exception), 0)

    def test_edit_requires_fresh_factual_confirmation(self):
        app = AppTest.from_file(Path(__file__).resolve().parents[1] / "app.py").run()
        app.checkbox[1].check().run()
        self.assertTrue(app.checkbox[1].value)
        app.text_area(key="copy").set_value(
            "Updated copy with practical progress"
        ).run()
        self.assertFalse(app.checkbox[1].value)
        self.assertEqual(len(app.exception), 0)
