TITLE='AI Marketing Transformation & Governance'

import json
from pathlib import Path
import streamlit as st
import pandas as pd
from portfolio.governance import ReviewStore, digest
ROOT=Path(__file__).resolve().parent
st.set_page_config(page_title=TITLE,layout='wide')
st.title(TITLE)
st.warning('Synthetic portfolio demonstration. No real company data or validated business outcomes. Independent project; no company affiliation.')
def load(name): return json.loads((ROOT/'data'/name).read_text())
def review(artifact,blocked=False):
    st.subheader('Human review')
    st.caption('Self-declared demo reviewer. A decision applies only to this exact artifact version. Local SQLite audit; not enterprise authentication.')
    with st.form('review'):
        reviewer=st.text_input('Reviewer alias',value='demo-reviewer')
        decision=st.selectbox('Decision',['revise','approve','reject'])
        reason=st.text_area('Reason')
        submit=st.form_submit_button('Record human decision')
    store=ReviewStore(ROOT/'runtime'/'audit.sqlite')
    if submit:
        try:store.decide(digest(artifact),decision,reviewer,reason,blocked);st.success('Decision recorded')
        except ValueError as exc:st.error(str(exc))
    st.caption('Audit hash chain valid: '+str(store.verify()))
    st.dataframe(store.rows())
    st.download_button('Download audit JSON',json.dumps(store.rows(),indent=2),'audit.json')
    store.db.close()

from portfolio.marketing import generate, evaluate, workflow_metrics
policy=load('brand_policy.json');briefs=load('briefs.json')
selected=st.selectbox('Brief',[b['id'] for b in briefs]);brief=dict(next(b for b in briefs if b['id']==selected))
brief['product']=st.text_input('Product',value=brief['product'])
brief['audience']=st.text_input('Audience',value=brief['audience'])
brief['verified_fact']=st.text_area('Supplied fact (synthetic; reviewer must verify)',value=brief['verified_fact'])
local=st.checkbox('Use installed local Ollama model (optional)',False)
if st.button('Generate draft'):
    try:
        text,mode=generate(brief,policy,local);st.session_state['copy']=text;st.session_state['mode']=mode
    except Exception as exc:st.error('Generation failed: '+type(exc).__name__)
if 'copy' not in st.session_state:st.session_state['copy'],st.session_state['mode']=generate(brief,policy)
st.caption(st.session_state['mode'])
text=st.text_area('Editable draft',key='copy',height=150)
evaluation=evaluate(text,policy);st.json(evaluation)
verified=st.checkbox('I checked factual support for all claims in this draft')
st.subheader('Workflow comparison — assumed synthetic observations')
metrics=workflow_metrics(load('workflow.json'));st.dataframe(pd.DataFrame(metrics).T)
st.bar_chart(pd.DataFrame(metrics).T[['approved_per_hour']])
st.caption('Includes draft, review and rework time. These assumptions do not demonstrate real productivity gains.')
review({'text':text,'policy':policy,'evaluation':evaluation,'facts_checked':verified},bool(evaluation['violations']) or not verified)
