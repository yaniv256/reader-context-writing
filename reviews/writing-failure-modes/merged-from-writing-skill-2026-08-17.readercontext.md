# Entries merged from the `writing` skill, 2026-08-17

<!--
READER CONTEXT SIDECAR
Reader model: A future agent or reviewer who finds four taxonomy entries with no audit evidence behind them and wants to know whether to trust them.
Does not know: That an earlier, single-file skill existed, or which session produced these corrections.
Cares about: Whether each entry is calibrated, and what is still owed before it can be relied on.
Does not care about: The history of the earlier skill beyond what bears on these four entries.
Reader voice: "Where did these come from, and have they been tested like the rest?"
Unresolved: None of the four has a blinded prompt or a baseline run.
Next passage: State the provenance, then the evidence debt, then each entry's originating defect.
-->

Four entries in `references/failure-modes.md` — the Ghost Menu, the Rain Check, the Grandfathered Claim, and the Borrowed Witness — entered the taxonomy by merge rather than by audit. They come from a predecessor skill that catalogued the same class of failure without the two-file workflow or the naming convention.

**They do not yet meet this project's own bar.** The process in `references/failure-modes.md` requires a blinded prompt, a frozen rubric, and a baseline run on an unrevised document before the first fix, and requires that the prompt find two to five distinct supported locations. None of these four has any of that. Each rests on a single observed defect in one technical specification, corrected in conversation at the time. Treat them as candidate detectors until someone runs the calibration, and retire any that cannot find siblings.

Each was checked against the existing taxonomy before being added, since the process prefers sharpening one detector to adding a synonym:

| Entry | Nearest existing mode | Why it was not folded in |
|---|---|---|
| The Ghost Menu | The Volunteered Alibi | The Alibi defends a choice that was made; this describes choices that were not. |
| The Rain Check | "Later we will explain..." under conversation leakage | That covers postponing a needed explanation. This covers a pointer standing where the sentence itself belongs, with a distinct test: is the sentence complete without the reference? |
| The Grandfathered Claim | Patching a structurally wrong draft | That prescribes reading top to bottom. This is the narrower discipline that a sentence carried through a revision is a claim re-asserted, and that absolutes are where it fails. |
| The Borrowed Witness | Make every scaling claim complete | That section governs mathematical rigor. This is a correspondence failure: sound arithmetic over the wrong population. |

The originating defects, for anyone building the calibration prompts:

- **Ghost Menu** — a specification stated that no article body text was used and no external service called. Both true, neither asked for.
- **Rain Check** — "Section 4 recovers exactly that," two sections before section 4 existed for the reader. Three of four forward references in that document turned out to be standing in for a missing sentence.
- **Grandfathered Claim** — "Nothing here is fitted" survived two revisions that added a fitted constant in the paragraph beneath it.
- **Borrowed Witness** — an opening cited a 67.6% null rate for a section field. Accurate, and dominated by homepage, obituary and games traffic the model excludes; among the story pages actually ranked, the field was 91.3% populated.
