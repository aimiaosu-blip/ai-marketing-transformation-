# Research report: AI marketing transformation and governance

## Executive finding

A marketing workflow should measure approved useful output after review and rework, rather than generation speed alone. The MVP connects briefs, drafts, policy checks, factual confirmation and human disposition. On 24 **invented workflow observations**, assisted production yields 1.345 approved items per total labor hour versus 1.017 for manual production. This difference is determined by the input assumptions; it is not an observed productivity improvement or evidence of a company's AI maturity.

## Research question and operationalization

When can generative assistance create marketing capacity without weakening brand governance? Three fictional briefs are translated into editable drafts. Offline mode is a transparent deterministic template. Optional Ollama mode calls an installed local generative model; that interface is mock-tested, with no claim of live-model validation. Both modes share the same checks and human decision gate.

The policy requires a brand phrase, disallows four environmental or commercial overclaims, and sets a 70-word limit. The displayed score deducts 25 points per violation, floored at zero. This is a configurable compliance heuristic, not an expert brand-consistency scale. A reviewer must additionally confirm factual support: passing a phrase checker alone cannot authorize release. The application records a disposition but never publishes content externally.

## Workflow comparison and computed results

Each synthetic mode contains 12 items, of which 10 are marked approved. The assumed manual workflow totals 590 minutes and the assisted workflow 446 minutes; each includes 80 minutes of rework. Both have mean synthetic quality score 83.83. Approved items per hour equals 60 multiplied by approved count, divided by draft + review + rework minutes. Total modeled time is lower by 144 minutes (24.4%), but these values are invented and cannot be cited as realized savings.

The assisted assumptions deliberately include a longer review stage: 15 minutes per item versus 8 minutes manually. Drafting gains are partially consumed by review burden. A useful business evaluation would also include training, model administration, rejected output, coordination and governance overhead, none of which are measured here.

## Governance implications

Marketing transformation changes roles as well as tools. The proposed division of responsibility is: marketing owns the brief and channel objective; brand owners define policy; the assistant drafts and flags; a named reviewer evaluates evidence, tone and context; an accountable manager owns publication decisions. The local demonstration uses self-declared aliases and does not implement enterprise authorization.

Each review is tied to the exact text and policy. Editing the draft changes its hash. Blocked copy cannot be approved simply by choosing an approval option. The audit supports inspection but is not an immutable enterprise ledger. Phrase matching misses paraphrases, negation, exaggeration and contextual brand violations; human judgment remains essential.

## Proposed thesis design

Conduct process-mapping interviews across marketing, brand and legal/compliance stakeholders. Build a task taxonomy separating ideation, adaptation, translation, factual claims and final publication. Use a counterbalanced within-person study with matched briefs, one manual and one assisted condition. Predefine quality with independent blinded reviewers and an anchored rubric covering factual support, brand voice, usefulness and originality. Record active labor separately from elapsed lead time; report disagreement and rejected drafts, not only accepted examples.

Test whether observed time differences persist after review and rework. Examine adoption barriers and decision-right changes qualitatively. A business case should combine measured labor, model and governance costs with uncertainty ranges, without assuming all saved minutes become cash savings. An appropriate deliverable is an operating model and stage-gated pilot recommendation, not a universal claim that AI replaces marketing work.

## Limitations

No employee study, customer response, sales effect or live model benchmark has been conducted. Briefs and labor observations are synthetic. The three offline drafts demonstrate workflow plumbing, not creative diversity. Real deployment requires approved data handling, model governance, versioned policies, authenticated reviewers and channel-specific legal checks.

## Reproduction and evidence

Run `python -m portfolio.demo` from the repository root. Inputs are in `data/`; row-level or aggregate outputs are in `results/`. Run `python -m pytest -q` for the tested behavioral boundaries. All original synthetic materials are MIT-licensed.
