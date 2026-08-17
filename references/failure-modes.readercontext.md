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

Edit only this annotated file. Regenerate `failure-modes.md` with the sidecar renderer after every change.

## How to evolve this reference

1. Start from a real reader failure, not an invented category.
2. Check whether an existing entry already covers the mechanism. Improve it rather than adding a synonym.
3. Write a blinded prompt, freeze a rubric, and calibrate on the unchanged document. A new prompt should ordinarily find two to five distinct supported locations, including the reported class.
4. Give a genuinely new class a short, memorable name that evokes the mechanism without requiring the originating conversation.
5. Record its project-specific prompt and evidence in `reviews/writing-failure-modes/`.
6. Add or revise the compact cross-project definition here.
7. Merge or retire an entry when repeated audits show that it is redundant, misleading, too broad, or no longer useful. Preserve useful prompts and prior results in the project history even when the starter taxonomy changes.

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
