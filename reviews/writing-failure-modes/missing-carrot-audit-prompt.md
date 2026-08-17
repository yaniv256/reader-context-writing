# Missing Carrot Audit Prompt


Read the complete clean document from title to final line. Find instructions, transitions, or required procedures that assume the reader will comply without explaining the purpose, payoff, avoided harm, or relation to the reader's goal.

Call a location **The Missing Carrot** only when all of these are true:

1. The text asks the reader to perform, avoid, preserve, or sequence an action.
2. A reader without the authoring conversation cannot recover why the action matters from nearby context.
3. The missing reason is material: knowing it would change compliance, execution quality, prioritization, or the ability to adapt the rule correctly.
4. The instruction is not merely a self-evident mechanical substep inside an already motivated operation.

Do not flag:

- a mechanical command whose purpose was established immediately before it;
- a familiar convention whose consequence is obvious to the intended audience;
- concise definitions that describe a failure rather than instruct an action;
- repetition of a rationale that is already visible and applicable;
- motivation invented after the fact that does not actually support the instruction.

For every supported location, report:

- identifying language;
- requested action;
- what the reader knows immediately beforehand;
- missing purpose, payoff, or avoided cost;
- how the omission may reduce compliance or distort execution;
- severity and confidence;
- a revision objective without replacement prose.

Group adjacent steps governed by one missing rationale as one location. Target two to five distinct supported locations, including the positive-control class during calibration. One location suggests overfitting; more than five requires a noise review. Record plausible false positives and explain why they do not qualify. Do not revise the document.

Treat writing as an attention trade. The reader pays continuously with time and attention; the prose must return a real benefit such as understanding, usefulness, surprise, pleasure, confidence, or avoided effort. A vague promise or the writer's convenience is not payment.

## Frozen 100-point rubric

- Reader benefit and attention exchange: 30 points
- Action-to-purpose linkage: 25 points
- Payoff or avoided-cost clarity: 20 points
- Workflow continuity: 15 points
- Reader autonomy and adaptability: 10 points

A central required workflow with no recoverable rationale is a blocker and caps the score at 69. An isolated unexplained instruction is major and caps the score at 89.
