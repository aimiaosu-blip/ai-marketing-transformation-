import json, unittest
from unittest.mock import patch, MagicMock
from portfolio.marketing import *
class MarketingTests(unittest.TestCase):
    def setUp(self): self.policy=json.loads(__import__('pathlib').Path('data/brand_policy.json').read_text())
    def test_template_pass_and_claim_block(self):
        text,mode=generate({'product':'Panel','audience':'Buyers'},self.policy)
        self.assertTrue(evaluate(text,self.policy)['publishable'])
        self.assertFalse(evaluate(text+' CARBON NEUTRAL',self.policy)['publishable'])
        self.assertIn('not LLM',mode)
    def test_required_phrase_and_length(self):
        self.assertFalse(evaluate('Hello',self.policy)['publishable'])
        self.assertFalse(evaluate('practical progress '+'word '*80,self.policy)['publishable'])
    def test_all_time_included(self):
        result=workflow_metrics([dict(workflow='assisted',draft_minutes=10,review_minutes=15,rework_minutes=5,approved=True,quality_score=80)])
        self.assertEqual(result['assisted']['approved_per_hour'],2)
    def test_local_model_adapter_mocked(self):
        response=MagicMock();response.__enter__.return_value.read.return_value=b'{"response":"practical progress"}'
        with patch.dict(os.environ,{'OLLAMA_MODEL':'test'}),patch('urllib.request.urlopen',return_value=response):
            text,mode=generate({'product':'Panel','audience':'Buyer'},self.policy,True)
            self.assertEqual(text,'practical progress')
