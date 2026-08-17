# Missing Carrot Audit — Baseline — August 16, 2026

<!--
READER CONTEXT SIDECAR
Reader model: The evaluator has frozen the prompt and rubric before changing the failure-mode reference and has read the unchanged clean reference completely.
Does not know: Whether the prompt will generalize beyond the reported workflow instruction.
Cares about: Distinct locations, false positives, score evidence, and a revision slate that explains rather than merely expands.
Does not care about: Rewarding the writer for already knowing the missing rationale in conversation.
Reader voice: "Which instructions expect me to tag along without knowing why?"
Unresolved: Calibration count, supported findings, baseline score, and revision order.
Next passage: Report the unchanged-document findings before authorizing revision.
Do not assume: That terse prose is unmotivated or that every command needs a separate rationale.
-->

## Audited authority

- Document: `references/failure-modes.md`
- Published commit: `88210ae49e52e08db67c05a01208526e446e4e9e`
- Prompt: `missing-carrot-audit-prompt.md`
- Method: complete clean-reference read from title through Railroading
- Prompt and rubric: frozen before this baseline and before reference revision

## Calibration result: two distinct locations

The audit found two supported locations:

1. the paired-file editing instruction before “How to evolve this reference”;
2. the seven-step evolution procedure, including the prompt-first rule reported by the reader.

The seven adjacent steps count as one location because they share one missing workflow rationale.

## Location 1: paired-file editing instruction

- **Requested action:** edit only the annotated reference and regenerate the clean reference.
- **Reader state:** the reader knows that the taxonomy is fluid but has not been told why two synchronized files exist.
- **Missing purpose:** the annotated file keeps reader-context reasoning available during edits; generation prevents hidden context from leaking into the clean reference read by future agents.
- **Likely effect:** an agent may regard the two-file rule as ceremony, edit the clean file directly, or fail to regenerate it.
- **Severity:** major.
- **Confidence:** high.
- **Revision objective:** connect the file authority and generation step to writing quality and clean-reader safety.

## Location 2: evolution procedure

- **Requested action:** classify a real defect, write and calibrate a blinded prompt, store project evidence, then update the cross-project taxonomy.
- **Reader state:** the reader receives seven commands but not the larger goal that makes the sequence necessary.
- **Missing purpose:** one reported failure is evidence of a recurring class. The prompt searches the rest of the current document and becomes a reusable detector for future documents, sparing the user from reporting every recurrence. Calibration proves that the prompt generalizes before revision changes the evidence. Project storage preserves executable proof; the compact reference makes the learned class available across projects.
- **Likely effect:** an agent may fix the local example, write a prompt tailored only to it, treat evidence storage as bureaucracy, or omit the durable cross-project update.
- **Severity:** blocker because this is the reference's central operating procedure.
- **Confidence:** high.
- **Revision objective:** motivate the workflow before enumerating it, then connect each phase to the current-document and future-document payoff.

## False-positive readback

- The opening explains that the reference keeps recurring failures active in attention and may evolve when doing so improves detection and compliance.
- The memorable-name paragraph explains why naming helps recall and qualifies the attention claim.
- Math Costume Failure gives the rendering consequence before requesting rendered validation.
- Proof Traffic Jam explains that relocation preserves rigor while restoring flow.
- The Sirens of Detail explains why premature detail is moved rather than discarded.
- Railroading explains the reader-population model and what meaningful branches accomplish.

## Frozen-rubric baseline: 38/100

| Dimension | Score | Evidence |
|---|---:|---|
| Reader benefit and attention exchange | 8/30 | The central maintenance workflow spends attention without exposing its governing reader and user benefit. |
| Action-to-purpose linkage | 8/25 | File and audit commands are not tied to their purposes. |
| Payoff or avoided-cost clarity | 6/20 | The reference omits current-document discovery, future reuse, and saved user effort. |
| Workflow continuity | 10/15 | The sequence is ordered but the reason for that order is missing. |
| Reader autonomy and adaptability | 6/10 | Without reasons, agents cannot safely adapt terse rules to new contexts. |

The central workflow blocker caps the score at 69. The arithmetic score is 38 and remains 38.

## Dependency-ordered revision slate

1. Explain why a reported defect must become a generalized prompt before any local fix.
2. State both payoffs: find recurrences in the current document and retain a detector for future documents.
3. State the user-time obligation: do not make the user report the same class repeatedly.
4. Explain why prompt and rubric precede revision and why two-to-five-location calibration matters.
5. Explain the division between project evidence and the compact cross-project reference.
6. Explain why annotated authority and generated clean output protect both writing quality and the future reader.
7. Rerun the identical prompt and rubric over the complete regenerated reference.
