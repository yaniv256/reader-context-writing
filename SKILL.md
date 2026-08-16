---
name: reader-context-writing
description: Draft and revise substantial reader-facing prose by explicitly separating the current user-session context from the reader's evolving knowledge, questions, objections, and expectations, tracked in inline comments or synchronized sidecars. Use for articles, essays, tutorials, reports, white papers, opinion pieces, operational source artifacts, and major rewrites where conversation context, user feedback, jargon, patchwork editing, or unexplained assumptions could leak into the document.
---

# Reader Context Writing

Write the document as a conversation with its eventual reader—not as a continuation of the current user session or a transcript of the drafting process.

Treat reader-context comments as working memory. Keep them in editable source formats that support non-rendered comments, such as Markdown or HTML. Do not render them in the published document.

## Choose inline comments or a sidecar

Use inline reader-context blocks only when the document's rendered form is the artifact its reader consumes. A comment hidden by the renderer is not hidden from a reader who consumes the raw source.

When the raw source is itself operational or reader-facing—such as `SKILL.md`, a prompt, source code, or a configuration file—keep the canonical file clean and create an annotated sidecar named `<stem>.readercontext.<extension>`. For example, pair `SKILL.md` with `SKILL.readercontext.md`.

The sidecar must:

- contain the complete canonical document in the same order;
- add only explicit `READER CONTEXT SIDECAR` comment blocks;
- model the actual future reader of the canonical artifact, not the current agent or user;
- remain mechanically synchronized so removing its reader-context blocks reproduces the canonical file byte for byte.

For a skill, model a fresh agent that has loaded `SKILL.md` because the skill triggered. Assume that agent has no memory of the conversation that produced the skill. Track what the instructions have established, what the agent may misread, and what the next section must clarify for correct execution.

Whenever either file changes, update its counterpart and run the sidecar parity check before considering the edit complete. Never ask the operational reader to ignore embedded session notes; keep those notes out of the operational artifact.

## Separate the user session from the reader's context

Maintain two distinct contexts:

- **User-session context:** everything available in the current agent's session with the user, including messages, prior drafts, corrections, objections, research, tool results, and editorial discussion.
- **Reader context:** only what the rendered document has actually told the reader, plus reasonable knowledge implied by the declared audience.

Use user-session context to decide what the document should accomplish. Never treat user-session context as knowledge the reader already has.

Before drafting, state internally:

1. Who is the reader?
2. What may this reader safely be assumed to know before the first sentence?
3. What should the reader understand, believe, feel, or be able to do by the end?
4. What central sentence must remain true throughout the document?

## Use the reader-context loop

Draft in short passages of roughly one to three paragraphs. In inline mode, insert a hidden block before each passage. In sidecar mode, insert the block only in the annotated sidecar at the corresponding location:

```markdown
<!--
READER CONTEXT
Reader model: [What the reader now knows and believes solely from the rendered text.]
Reader voice: "[The reader's likely natural-language reaction, question, doubt, or expectation.]"
Unresolved: [What remains confusing, unproved, undefined, or emotionally unearned.]
Next passage: [The single change the next passage should make in the reader's context.]
Do not assume: [Relevant user-session knowledge that has not yet been taught.]
-->
```

Then write the passage that performs the stated context change.

After every paragraph, briefly simulate the reader's reaction, even when no new comment block is needed. Add or update a block whenever the reader's state, question, or required next move changes materially. Do not let several pages pass under one stale reader model.

Give the simulated reader a real voice. “The reader may be confused” is less useful than: “Why are these arrays allowed to overlap? Won't one feature corrupt another?” The concrete question reveals what must be answered and when.

## Make each passage earn the next one

For every paragraph, verify:

- What new fact, distinction, intuition, proof, or motivation did this paragraph add?
- Could the reader understand every term from prior rendered text?
- What question does the paragraph create?
- Does the next paragraph answer that question, or deliberately explain why another step must come first?
- Has the prose changed register—from engineer to mathematician, beginner to expert, manifesto to tutorial—without building a bridge?

Introduce notation only after the object has an intuitive or concrete meaning. Introduce specialized names after teaching the mechanism unless the audience can safely be assumed to know them.

When a construction creates an obvious concern, answer it at the point of introduction. Do not present a formula that appears to mix signals and postpone the anti-interference mechanism until several sections later.

## Prevent conversation leakage

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

### Assuming shared context

Do not drop research names, conclusions, or distinctions merely because the current agent and user already understand them. Teach the mechanism in ordinary language first. Let terminology become a label for something the reader already recognizes.

### Writing to the user's latest objection

Do not let the last correction dominate the next draft. Ask whether a fresh reader would naturally have that objection at that location. If yes, stage and answer it. If no, extract the underlying insight and place it where it advances the reader's journey.

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

For explanatory opinion writing, alternate between prescription and enablement:

- State what should change and why it matters.
- Teach enough mechanism for the reader to see that the prescription is actionable.
- Supply proof or derivation where the claim depends on it.
- Return to the engineering consequence.

Do not confuse “tutorial” with “build a complete toy project.” A tutorial can remain at the level of general mechanisms, equations, design choices, and implementation patterns.

## Revise with two passes

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

## Completion standard

Finish only when:

- the reader can acquire every necessary concept from the rendered document;
- every major transition follows from a simulated reader question or need;
- reader-context working notes accurately track the current draft;
- the document's central sentence remains visible in every section's purpose;
- examples illuminate rather than narrow the thesis;
- rendered prose contains no user-session residue;
- objections appear where the reader would generate them, not where the user happened to raise them.

The governing rule is:

> Write from the conversation occurring inside the reader, not from the conversation that produced the draft.
