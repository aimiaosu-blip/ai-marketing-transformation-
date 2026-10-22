# Data contract and metrics

`briefs.json`: three fictional product/audience/fact briefs; `brand_policy.json`: brand name, required phrase, prohibited phrases and word cap. The word limit uses whitespace token counts. Brand score is max(0, 100 − 25 × violation count), a heuristic.

`workflow.json`: 12 manually authored-formula rows per mode. For item i=1..12: manual draft minutes=28+i; assisted=9+i; manual review=8; assisted=15; rework=12 when i is divisible by 3 and 4 otherwise; approved unless i is divisible by 5; quality=75+(7i mod 20). These are invented observations, not logs. Approved per hour=60 × approved count / sum(draft+review+rework). Missing or zero effort cannot demonstrate productivity.
