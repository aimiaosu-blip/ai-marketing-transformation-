import json
from pathlib import Path
from portfolio.charts import bars
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results';OUT.mkdir(exist_ok=True)
def load(name): return json.loads((ROOT/'data'/name).read_text())
def write(name,value): (OUT/name).write_text(json.dumps(value,indent=2)+'\n')

from portfolio.marketing import *
policy=load('brand_policy.json');output=[]
for brief in load('briefs.json'):
    text,mode=generate(brief,policy);output.append(dict(id=brief['id'],text=text,mode=mode,evaluation=evaluate(text,policy)))
metrics=workflow_metrics(load('workflow.json'));write('drafts.json',output);write('metrics.json',metrics)
bars({k:v['approved_per_hour'] for k,v in metrics.items()},OUT/'overview.svg','Assumed synthetic approved items / total labor hour')

print('Rebuilt synthetic outputs in',OUT)
