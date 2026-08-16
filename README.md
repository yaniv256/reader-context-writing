# Reader Context Writing

Reader Context Writing is a skill for drafting and revising substantial reader-facing prose around the reader's evolving knowledge, questions, objections, and expectations.

This private repository is the review home for the skill exported from ChatGPT on August 15, 2026. The original ZIP is preserved locally with SHA-256:

```text
00b7f665a0f2a94c77d8ed6dc0618b29b8a29c786f7dece1266289b9cba9eec9
```

## Contents

- `SKILL.md` — the complete skill instructions.
- `SKILL.readercontext.md` — a synchronized annotated view that models a fresh agent reading the skill.
- `agents/openai.yaml` — OpenAI product metadata and the default invocation prompt.
- `scripts/check_reader_context_sidecar.py` — verifies that stripping `READER CONTEXT SIDECAR` blocks from the annotated view reproduces `SKILL.md` byte for byte.

Run the synchronization check with:

```sh
python3 scripts/check_reader_context_sidecar.py SKILL.md SKILL.readercontext.md
```

## Review status

This repository is private and has not been released or licensed for public reuse yet. If the review is successful, the public-release step should make the licensing and distribution decisions explicitly.

The uploaded `agents/openai.yaml` refers to `assets/icon.svg`, but the uploaded ZIP did not contain that asset. The source files are preserved as uploaded rather than inventing an icon. Before public release, either add the intended icon asset or remove those metadata fields.
