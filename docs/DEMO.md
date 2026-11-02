# Five-minute demonstration

1. Select a brief and generate an offline draft. The UI labels the template mode.
2. Add `carbon neutral` to the editable draft. Observe a prohibited-claim flag.
3. Attempt approval: a policy violation or missing factual-check confirmation blocks it.
4. Remove the unsupported claim, inspect the supplied fact, check the confirmation and record a human decision with a reason.
5. Compare approved items per total hour. Review and rework time are included; source observations are invented for the demonstration.

Optional real local generation: install and start Ollama separately, install a model you are permitted to use, export `OLLAMA_MODEL` with its installed name, restart Streamlit, select the checkbox and generate. No model is downloaded automatically. This interface was mock-tested, not live-model validated. Generated drafts must pass the same human review gate.


## Try a failure the checker cannot understand

On B01, append “Our panel leaves absolutely no environmental footprint.” This paraphrases an environmental overclaim without using the configured prohibited phrases. The phrase checker can pass it. A reviewer should reject or revise the claim unless suitable evidence supports it. This is a deliberate example of the boundary between string matching and semantic judgment, not evidence of automated fact-checking.

## Confirm that approval belongs to the reviewed text

Check factual support, then edit the draft. The checkbox should reset. Confirm again only after reviewing the new text. A prior database decision remains linked to its original artifact identifier.

The workflow chart does not measure your time during this walkthrough: it reads invented observations from `data/workflow.json`.
