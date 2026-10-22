import unittest
from pathlib import Path
from streamlit.testing.v1 import AppTest
class AppTests(unittest.TestCase):
    def test_dashboard_starts(self):
        app=AppTest.from_file(Path(__file__).resolve().parents[1]/'app.py').run(timeout=30)
        self.assertEqual(len(app.exception),0,str(app.exception))

    def test_generate_and_policy_failure(self):
        app=AppTest.from_file(Path(__file__).resolve().parents[1]/'app.py').run()
        app.button[0].click().run()
        app.text_area(key='copy').set_value('practical progress carbon neutral').run()
        import json
        self.assertFalse(json.loads(app.json[0].value)['publishable'])
        self.assertEqual(len(app.exception),0)
