# Writing Failure Modes

<!--
READER CONTEXT SIDECAR
Reader model: An agent using the writing skill needs a memorable starter vocabulary for recurring reader failures and permission to evolve it through evidence.
Does not know: The conversations or documents in which these names originated.
Cares about: Fast recognition, precise boundaries, reusable prompts, and a safe way to change the taxonomy.
Does not care about: Treating the current list as permanent doctrine or preserving a clever name after it stops helping.
Reader voice: "Which failure patterns should stay active in my attention, and how may I improve this list?"
Unresolved: Future audits may add, rename, merge, sharpen, or retire entries.
Next passage: Establish the reference as a fluid starter set, then define each memorable failure mode.
Do not assume: That naming a failure proves it exists in the current document.
-->

This is a **fluid starter taxonomy**, not a closed standard. Use it to keep recurring reader failures active in attention. Add, rename, merge, sharpen, or remove entries when calibrated writing work shows that doing so improves detection and compliance.

Writing is an attention trade. The reader pays continuously with time and attention. The writer must return a real benefit: understanding, usefulness, surprise, pleasure, confidence, saved effort, or another outcome the reader values. Every instruction, transition, and requested detour must earn its cost.

Edit only this annotated file because it preserves the reader model that makes future revisions reader-aware. Regenerate `failure-modes.md` after every change so future agents receive the useful guidance without inheriting hidden session context.

## How to evolve this reference

When a reader reports a defect—or an agent detects one—do not spend the user's time fixing only that instance. The same mechanism may recur elsewhere in the current document and in future documents. A generalized prompt converts one complaint into a full-document search now and a reusable detector later. This prevents the user from having to report the same class repeatedly.

Use this sequence because revision changes the evidence. The prompt, rubric, and unchanged baseline must exist before the first fix; otherwise the known example can narrow the search and hide its siblings.

1. Start from a real reader failure so the taxonomy solves observed harm rather than collecting invented categories.
2. Check whether an existing entry covers the mechanism. Improving it preserves one strong detector instead of scattering attention across synonyms.
3. Write a blinded prompt aimed at the failure mechanism, freeze a rubric, and run both on the unchanged document. The prompt should ordinarily find two to five distinct supported locations, including the reported class; this demonstrates useful generalization before revision.
4. Give a genuinely new class a short, memorable name so future writers can recall and apply the check without the originating conversation.
5. Store the executable prompt, baseline, false positives, revision slate, and rerun evidence in `reviews/writing-failure-modes/` so the result can be reproduced and challenged within the project.
6. Add or revise the compact definition here so the learned failure remains available across future projects and documents.
7. Merge or retire an entry when repeated audits show that it is redundant, misleading, too broad, or no longer useful. Preserve its prompts and prior results in project history so removing it from the starter set does not erase evidence.

Memorable names are a compliance tool: a compact image is easier for future writers and agents to recall and apply consistently. Treat any claim about how memorability directs model attention as a working heuristic, not established model science.

## Humpty Dumpty

Use a familiar technical word or established symbol for a quantity that violates its conventional meaning, range, normalization, or contract. The reader applies the ordinary meaning and reaches an impossible or misleading interpretation.

## Red Herring

Analyze a technically valid internal quantity that does not answer the reader's or product's actual question. The derivation looks rigorous while the promised score, prediction, ranking, probability, or error remains unexplained.

## Symbol Without a Passport

Introduce a symbol, count, scale, or term without enough local provenance for the reader to know what it denotes in the current argument. The reader must search backward, guess whether it was repurposed, or abandon the derivation.

## Mumbling

Write a sentence aimed at the writer, a past reviewer, or someone else who is not in the room. The intended reader merely overhears an internal monologue or side conversation that was not addressed to them.

## The Volunteered Alibi

Address the reader with an unsolicited defense that makes an otherwise unremarkable choice look suspicious. This differs from Mumbling: Mumbling fails audience address; the Volunteered Alibi addresses the correct reader but produces suspicion rather than reassurance.

## Math Costume Failure

Write mathematical source that looks plausible in the editor but renders incorrectly or misleadingly on the delivery surface. Validate the rendered notation, not merely the source syntax.

## Proof Traffic Jam

Place necessary support in the main line where it blocks the reader's progress. Preserve rigor by moving the proof, derivation, caveat chain, or specialist support to an appendix, endnote, footnote, expandable section, or linked destination.

## The Sirens of Detail

Follow attractive details before the reader has reached the question that makes them valuable. Detail is the continent containing the treasure; premature detail sings at the harbor entrance and shipwrecks the argument before the reader reaches that depth. Move the detail to the point of need rather than discarding it.

## Railroading

Write for one imaginary, perfectly predictable reader and force the whole audience through one reading order or depth. Model the audience as a party with different interests. Preserve a coherent main path while signposting meaningful branches through section links, cross-references, appendices, endnotes, footnotes, indexes, or labeled optional depth.

## The Missing Carrot

Ask the reader to follow an instruction, transition, or reading path without exposing a real benefit in return for their attention. The reader is free to leave; prose cannot assume they will tag along. State what they gain, what problem they avoid, or what capability the requested step unlocks. The benefit must matter to the reader rather than merely serving the writer's preferred process.
