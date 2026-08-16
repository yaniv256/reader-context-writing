---
name: reader-context-writing
description: Draft and revise substantial reader-facing prose by explicitly separating the current user-session context from the reader's evolving knowledge, interests, questions, objections, and expectations. Always edit a reader-context-annotated source and mechanically generate its clean reader-facing counterpart. Use for articles, essays, tutorials, reports, white papers, opinion pieces, operational source artifacts, and major rewrites where conversation context, user feedback, jargon, patchwork editing, irrelevant rationale, or unexplained assumptions could leak into the document.
---

# Reader Context Writing
<!--
READER CONTEXT SIDECAR
Reader model: A fresh agent knows the skill concerns writing from the eventual reader's perspective, but has not yet learned the operating method.
Does not know: How to keep the reader's perspective active while the user session remains naturally salient.
Cares about: Producing a document that a fresh reader can follow without access to the drafting session.
Does not care about: The conversation, revisions, or naming decisions that produced this skill.
Reader voice: "Is this a general writing philosophy, or does it require a concrete workflow?"
Unresolved: The distinction between the current user session and the document reader's experience.
Next passage: Establish the governing perspective and the role of reader-context working memory.
Do not assume: Knowledge of the conversation in which this skill was designed.
-->

Write the document as a conversation with its eventual reader—not as a continuation of the current user session or a transcript of the drafting process.

Treat reader-context comments as working memory. Keep them in the annotated source and generate a clean operational file that omits them. Always maintain both files.

## Always edit the annotated source

For every document, create an annotated editing source named `<stem>.readercontext.<extension>` and generate the clean operational file from it. For example, edit `SKILL.readercontext.md` and render `SKILL.md`.

The annotated file is the only editing authority. The clean file is a generated projection for readers and downstream systems. Do not edit the clean file, even for a small or apparently mechanical correction. An edit made without the surrounding reader context is not reader-context-aware and bypasses the method this skill exists to enforce.

The annotated source must:

- contain the complete clean document in the same order;
- add only explicit `READER CONTEXT SIDECAR` comment blocks;
- model the actual future reader of the clean artifact, not the current agent or user;
- be the editing authority from which the clean artifact is generated;
- remain mechanically synchronized so removing its reader-context blocks reproduces the clean file byte for byte.

For a skill, model a fresh agent that has loaded `SKILL.md` because the skill triggered. Assume that agent has no memory of the conversation that produced the skill. Track what the instructions have established, what the agent may misread, and what the next section must clarify for correct execution.

For every revision:

1. Read the annotated source, including the reader-context blocks around the passage.
2. Make the prose change in the annotated source and update the affected reader-context blocks.
3. Run the renderer to replace the clean file.
4. Run the parity check and reject the revision if the generated output differs from the annotated source with its blocks removed.

If the clean file was edited accidentally, do not preserve that edit as an exception. Recreate the change in the annotated source with its reader context, then regenerate the clean file. Never ask the operational reader to ignore embedded session notes; keep those notes out of the operational artifact.

## Separate the user session from the reader's context
<!--
READER CONTEXT SIDECAR
Reader model: The agent knows every document has an annotated editing source and a generated clean output.
Does not know: The exact boundary between information available in the user session and information established for the reader.
Cares about: Keeping operational source clean while retaining useful writing-state memory.
Does not care about: Why this file-pair convention was proposed or which earlier convention it replaced.
Reader voice: "Whose context am I tracking, and what information am I forbidden to carry across?"
Unresolved: A precise boundary between material learned while drafting and material taught by the document.
Next passage: Define user-session context and reader context as separate state.
Do not assume: That the eventual reader saw the prompt, research discussion, corrections, or earlier drafts.
-->

Maintain two distinct contexts:

- **User-session context:** everything available in the current agent's session with the user, including messages, prior drafts, corrections, objections, research, tool results, and editorial discussion.
- **Reader context:** only what the rendered document has actually told the reader, plus reasonable knowledge implied by the declared audience.

Use user-session context to decide what the document should accomplish. Never treat user-session context as knowledge the reader already has.

The user session remains naturally present because the agent is participating in it. Reader context does not. Reconstruct the reader's position deliberately at each point in the document. Keep asking:

1. What does the reader not know here?
2. What does the reader not care about here?

The first question prevents unexplained assumptions. The second prevents session details, rationales, and concerns from entering the document merely because they matter to the agent and user.

Before drafting, state internally:

1. Who is the reader?
2. What may this reader safely be assumed to know before the first sentence?
3. What should the reader understand, believe, feel, or be able to do by the end?
4. What central sentence must remain true throughout the document?

## Use the reader-context loop
<!--
READER CONTEXT SIDECAR
Reader model: The agent understands the two contexts and has an initial reader contract, but still needs an executable drafting routine.
Does not know: Which reader-state fields to record or how often to refresh them.
Cares about: A repeatable loop that controls the next passage rather than merely describing the audience once.
Does not care about: The user-session discussion that led to the chosen fields.
Reader voice: "What exactly do I write down as the reader moves through the document?"
Unresolved: The cadence, fields, and granularity of reader-state updates.
Next passage: Provide the working-memory template and explain how to keep it current.
Do not assume: That a single up-front audience description remains accurate throughout a long draft.
-->

Draft in short passages of roughly one to three paragraphs. In the annotated source, insert a reader-context block before each passage:

```markdown
<!--
READER CONTEXT SIDECAR
Reader model: [What the reader now knows and believes solely from the rendered text.]
Does not know: [What the reader has not yet been told or cannot yet infer.]
Cares about: [What currently gives the reader a reason to continue.]
Does not care about: [User-session details or rationale that do not serve the reader here.]
Reader voice: "[The reader's likely natural-language reaction, question, doubt, or expectation.]"
Unresolved: [What remains confusing, unproved, undefined, or emotionally unearned.]
Next passage: [The single change the next passage should make in the reader's context.]
Do not assume: [Relevant user-session knowledge that has not yet been taught.]
-->
```

Then write the passage that performs the stated context change.

After every paragraph, briefly simulate the reader's reaction, even when no new comment block is needed. Ask again what the reader still does not know and does not care about. Add or update a block whenever the reader's knowledge, interest, question, or required next move changes materially. Do not let several pages pass under one stale reader model.

Give the simulated reader a real voice. “The reader may be confused” is less useful than: “Why are these arrays allowed to overlap? Won't one feature corrupt another?” The concrete question reveals what must be answered and when.

## Make each passage earn the next one
<!--
READER CONTEXT SIDECAR
Reader model: The agent can now create reader-context blocks and simulate concrete reader reactions.
Does not know: How to convert the tracked state into paragraph order and transitions.
Cares about: Making each passage prepare the reader for the next.
Does not care about: Editorial rationale that does not change the reader's understanding or motivation.
Reader voice: "How do I use those reactions to control explanatory order rather than merely annotate it?"
Unresolved: The test for whether one paragraph has prepared the next.
Next passage: Turn the reader model into paragraph-level sequencing checks.
Do not assume: That logical correctness alone makes a transition understandable.
-->

For every paragraph, verify:

- What new fact, distinction, intuition, proof, or motivation did this paragraph add?
- Could the reader understand every term from prior rendered text?
- What does the reader still not know?
- Why does the reader care about the next detail?
- What matters in the user session but not to the reader, and should therefore be omitted?
- What question does the paragraph create?
- Does the next paragraph answer that question, or deliberately explain why another step must come first?
- Has the prose changed register—from engineer to mathematician, beginner to expert, manifesto to tutorial—without building a bridge?

Introduce notation only after the object has an intuitive or concrete meaning. Introduce specialized names after teaching the mechanism unless the audience can safely be assumed to know them.

When a construction creates an obvious concern, answer it at the point of introduction. Do not present a formula that appears to mix signals and postpone the anti-interference mechanism until several sections later.

## Prevent conversation leakage
<!--
READER CONTEXT SIDECAR
Reader model: The agent knows how to sequence ideas from the reader's questions and prior knowledge.
Does not know: How to recognize sentences that remain grammatically sound while leaking the user session.
Cares about: Keeping the rendered prose self-contained and relevant.
Does not care about: Why the user requested a correction unless that reason independently serves the document.
Reader voice: "Even with good structure, how do I catch prose that is secretly replying to the user or narrating my drafting process?"
Unresolved: Recognizable symptoms of user-session residue in rendered prose.
Next passage: Name leakage patterns and distinguish useful reader-inclusive language from private-process narration.
Do not assume: That grammatically polished prose is reader-facing prose.
-->

Scan rendered prose for sentences that make sense only as replies to the user or as notes to oneself. Rewrite them as claims that serve the reader.

Common leakage patterns include:

- “Only now do we need notation.”
- “As we discussed earlier...” when the discussion is not in the document.
- “The clean response to this objection is...” when the reader has not raised it.
- “Later we will explain...” used to postpone an explanation needed now.
- “The tutorial point is...” or “what matters for us...”
- defensive novelty disclaimers inherited from the user session;
- unexplained references such as “this problem,” “the previous example,” or “our scheme” whose antecedent exists only in conversation;
- emphasis that reflects what the user recently corrected rather than what the reader needs emphasized.

Inclusive “we” is not automatically a problem. Keep it when it genuinely includes the reader in a derivation, experiment, or shared engineering prescription. Remove it when it narrates the writing process or preserves the emotional shape of the user session.

## Correct the recurring failure modes
<!--
READER CONTEXT SIDECAR
Reader model: The agent can detect direct conversation leakage and understands that inclusive “we” is context-dependent.
Does not know: Which structural failures can survive a sentence-level leakage scan.
Cares about: Avoiding audience shifts, defensive prose, scope drift, and stale reader models.
Does not care about: Preserving the emotional emphasis or sequence of corrections from the user session.
Reader voice: "What are the less obvious ways a draft can still follow the user session instead of the reader's context?"
Unresolved: Structural and editorial failure modes that survive a sentence-level leakage scan.
Next passage: Provide concrete correction rules for the most common failures.
Do not assume: That local edits can repair a draft whose audience or explanatory order has changed.
-->

### Assuming shared context

Do not drop research names, conclusions, or distinctions merely because the current agent and user already understand them. Teach the mechanism in ordinary language first. Let terminology become a label for something the reader already recognizes.

### Writing to the user's latest objection

Do not let the last correction dominate the next draft. Ask whether a fresh reader would naturally have that objection at that location. If yes, stage and answer it. If no, extract the underlying insight and place it where it advances the reader's journey.

### Carrying correction rationale into the document

A correction from the user often includes a reason so the current agent can apply it well. Treat that reason as user-session context, not as reader-facing content. Preserve the correction's effect. Include its rationale only when a fresh reader independently needs the underlying reason to understand, evaluate, or act on the document. State that reason directly; do not narrate the correction, defend the new wording, or explain why an earlier version was wrong.

### Switching audiences midstream

Do not move abruptly from concrete engineering prose to unexplained mathematical objects. Define what an encoder emits, what the symbols refer to, and why the equation is needed before presenting it.

### Overcorrecting with defensive hedges

Calibrate qualifications to the evidence and intended claim, not to tension in the drafting conversation. Do not insert a caveat that contradicts the stated construction or quietly changes the engineering contract. State exact guarantees exactly, probabilistic guarantees probabilistically, and empirical choices as measurements.

### Letting examples seize the article

Use examples to clarify the general argument. Do not silently turn a general data-science article into a recommender-system tutorial, implementation exercise, or other narrower piece unless the reader contract calls for that scope.

### Following side quests

Preserve valuable tangents in notes, but exclude them when they do not help establish the central thesis. A correct and interesting digression can still damage the reader's model by introducing a second argument before the first is secure.

### Patching a structurally wrong draft

Before revising a long document, read it completely from beginning to end. Reconstruct its reader journey and central claim before editing. If the audience, governing thesis, explanatory order, or manifesto/tutorial balance has changed, rewrite the document top to bottom. Do not disguise a structural rewrite as scattered local edits.

### Leaving stale reader comments

Treat hidden comments as part of the source. Whenever prose changes, update nearby reader context. A comment that describes an earlier draft is worse than no comment because it gives the next writer a false model of the reader.

## Balance manifesto and tutorial
<!--
READER CONTEXT SIDECAR
Reader model: The agent knows the main failure modes, including scope drift, defensive hedging, side quests, structural patching, and stale comments.
Does not know: How much mechanism to teach while maintaining a strong argument.
Cares about: Making prescriptions understandable and actionable without losing focus.
Does not care about: A complete toy implementation when the document's claim does not require one.
Reader voice: "How should I balance making a strong claim with teaching enough for the claim to feel actionable?"
Unresolved: The proper rhythm between prescription, mechanism, evidence, and consequence.
Next passage: Define a reusable manifesto–tutorial alternation without forcing a toy implementation.
Do not assume: That explanatory depth requires turning the document into a complete build tutorial.
-->

For explanatory opinion writing, alternate between prescription and enablement:

- State what should change and why it matters.
- Teach enough mechanism for the reader to see that the prescription is actionable.
- Supply proof or derivation where the claim depends on it.
- Return to the engineering consequence.

When a mathematical claim needs more support than the main line can carry, keep the claim's definitions, assumptions, status, governing intuition, and a precise pointer in the body. Put the full proof or derivation and its limits in a named appendix. Do not make the reader choose between smooth prose and a believable claim.

Do not confuse “tutorial” with “build a complete toy project.” A tutorial can remain at the level of general mechanisms, equations, design choices, and implementation patterns.

## Revise with two passes
<!--
READER CONTEXT SIDECAR
Reader model: The agent understands the desired drafting rhythm and the difference between explanation and an exhaustive project.
Does not know: How to review the finished draft without letting session knowledge fill its gaps.
Cares about: A revision method that tests the actual reader journey and the visible prose independently.
Does not care about: The agent's intended meaning when the document itself does not communicate it.
Reader voice: "Once the draft exists, how do I review the whole reader journey without letting my intent excuse what the page fails to say?"
Unresolved: A revision procedure that independently checks comprehension and conversation leakage, then turns discovered defects into systematic improvement.
Next passage: Separate the reader-journey audit from the rendered-prose leakage audit, then define the whole-document correction loop.
Do not assume: That checking hidden comments alone proves the visible document works.
-->

### Reader-journey pass

Read the complete rendered prose in order while ignoring what the current session intended. At each hidden block, test whether its reader model follows from the preceding rendered text. Repair missing definitions, premature abstractions, unanswered questions, scope drift, and misplaced objections.

### Conversation-leakage pass

Temporarily ignore hidden comments and scan only rendered prose. Flag any sentence that sounds like:

- an instruction to oneself;
- a response to the user rather than the reader;
- a reference to the drafting process;
- an assumption imported from conversation;
- an apology or defense that the reader did not request.

Rewrite each flagged sentence as direct exposition, or delete it if it performs no reader-facing work.

## Turn every discovered defect into a whole-document revision loop

<!--
READER CONTEXT SIDECAR
Reader model: The agent can audit reader journey and conversation leakage but may still respond to a reported defect with a narrow local patch.
Does not know: How to generalize one concrete failure into a repeatable prompt, measurable baseline, and article-wide correction.
Cares about: Fixing the class of failure everywhere without inventing a favorable evaluation after editing.
Does not care about: A score that was not frozen before revision or an audit prompt that names the known target.
Reader voice: "When one paragraph fails, how do I improve the document rather than merely repair the example I was shown?"
Unresolved: Prompt tuning, quantitative evaluation, revision scope, and comparable readback.
Next passage: Define the mandatory prompt–score–revise–rescore procedure.
Do not assume: That a local defect is unique, or that the same rubric will be remembered unless it is recorded.
-->

When a reader or reviewer identifies a writing defect, do not begin by fixing that passage. Treat the defect as evidence of a class of failures that may occur elsewhere in the document.

Use this procedure:

1. **Name the failure class.** Describe the general reader failure without quoting or identifying the known passage. Examples include missing symbol provenance, unsupported mathematical claims, conversation leakage, misplaced qualifications, or supporting detail that interrupts the main line.
2. **Tune an audit prompt.** Create or revise a prompt that would detect the failure from the rendered document alone. It must read the complete document, reconstruct reader state, produce evidence for each finding, and include false-positive controls. The saved prompt must not reveal the positive-control passage.
3. **Freeze a quantitative rubric.** Before revising, record dimensions, weights totaling 100, full-credit standards, and calibration anchors. The rubric must penalize the discovered failure class without allowing improvement in one dimension to hide damage in another.
4. **Run the baseline audit.** Apply the prompt and rubric to the full clean document from top to bottom. Record the score, all related findings, and a dependency-ordered recommendation for revision.
5. **Revise the complete annotated source.** Read it from top to bottom and repair every supported finding in dependency order. Update affected reader-context blocks. Rewrite broadly when local fixes would damage flow or leave the governing structure inconsistent.
6. **Regenerate the clean document.** Never patch the clean projection. Render it from the annotated authority and verify byte-for-byte sidecar parity.
7. **Rerun the identical audit and rubric.** Read the complete revised document, not only the changed passages. Record the new score and an item-level readback showing whether every baseline finding was resolved, remains open, or changed form.
8. **Reject self-congratulation.** Do not raise the score because effort was spent or because the known example improved. Every point increase needs document evidence under the frozen anchors. Record declared limitations and new regressions.
9. **Iterate when necessary.** If the second pass exposes another general failure class, tune the prompt again and repeat the full loop. Do not patch the new example in isolation.

Keep the prompt, rubric, baseline, revision recommendation, post-revision evaluation, and resolution trace beside the document whenever the repository supports review artifacts. A non-blinded same-session audit demonstrates that the prompt operationalizes the defect; it does not count as independent validation. When independence matters, give a fresh evaluator only the clean document, reader contract, frozen prompt, and rubric.

## Completion standard
<!--
READER CONTEXT SIDECAR
Reader model: The agent has a complete drafting method, two review passes, and a quantitative whole-document correction loop.
Does not know: The exact evidence required before the work can be considered finished.
Cares about: A stopping rule that proves comprehension, relevance, continuity, and clean separation from the user session.
Does not care about: How much effort the drafting session required or how many corrections preceded the final document.
Reader voice: "What evidence tells me the document is actually finished?"
Unresolved: A concise stopping condition that covers knowledge transfer, transitions, scope, comment accuracy, and user-session residue.
Next passage: State the completion gate and compress the skill into one governing rule.
Do not assume: That absence of obvious grammatical defects means the reader journey is complete.
-->

Finish only when:

- the reader can acquire every necessary concept from the rendered document;
- every major transition follows from a simulated reader question or need;
- each passage accounts for what the reader does not yet know and has no reason to care about;
- reader-context working notes accurately track the current draft;
- the document's central sentence remains visible in every section's purpose;
- examples illuminate rather than narrow the thesis;
- rendered prose contains no user-session residue;
- objections appear where the reader would generate them, not where the user happened to raise them.

The governing rule is:

> Write from the conversation occurring inside the reader, not from the conversation that produced the draft.
