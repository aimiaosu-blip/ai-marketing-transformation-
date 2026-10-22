import json, os, urllib.request

def evaluate(text,policy):
    lower=text.lower(); violations=[]
    for phrase in policy['prohibited']:
        if phrase.lower() in lower: violations.append('Prohibited claim: '+phrase)
    for phrase in policy['required']:
        if phrase.lower() not in lower: violations.append('Missing brand phrase: '+phrase)
    if len(text.split())>policy['max_words']: violations.append('Word limit exceeded')
    return {'score':round(max(0,100-25*len(violations)),1),'violations':violations,'publishable':not violations}

def generate(brief,policy,use_local_model=False):
    if not brief.get('product','').strip() or not brief.get('audience','').strip(): raise ValueError('Product and audience required')
    if use_local_model:
        model=os.environ.get('OLLAMA_MODEL')
        if not model: raise ValueError('Set OLLAMA_MODEL to an installed local model')
        prompt='Draft marketing content using only these supplied facts. No unsupported environmental claims. Return only copy. Brand policy: '+json.dumps(policy)+' Brief: '+json.dumps(brief)
        body=json.dumps({'model':model,'prompt':prompt,'stream':False}).encode()
        request=urllib.request.Request('http://127.0.0.1:11434/api/generate',data=body,headers={'Content-Type':'application/json'})
        with urllib.request.urlopen(request,timeout=60) as response: text=json.load(response)['response']
        if not isinstance(text,str) or not text.strip(): raise ValueError('Empty model output')
        return text,'Local Ollama generative model (unvalidated draft)'
    text=f"{policy['brand']}: {brief['product']} for {brief['audience']}. {brief.get('verified_fact','Ask for product specifications before purchase.')} Built for practical progress. Contact our team to discuss your project."
    return text,'Offline deterministic template — not LLM inference'

def workflow_metrics(rows):
    result={}
    for mode in sorted({r['workflow'] for r in rows}):
        group=[r for r in rows if r['workflow']==mode]; total=sum(r['draft_minutes']+r['review_minutes']+r['rework_minutes'] for r in group)
        approved=sum(r['approved'] for r in group)
        result[mode]={'items':len(group),'total_minutes':total,'approved_items':approved,'approved_per_hour':round(60*approved/total,3) if total else None,'mean_quality':round(sum(r['quality_score'] for r in group)/len(group),2),'rework_minutes':sum(r['rework_minutes'] for r in group)}
    return result
