#!/usr/bin/env python3
"""Verify that a reader-context sidecar reduces exactly to its canonical file."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


BLOCK = re.compile(
    rb"<!--\nREADER CONTEXT SIDECAR\n.*?\n-->\n",
    flags=re.DOTALL,
)


def strip_reader_context_blocks(content: bytes) -> bytes:
    return BLOCK.sub(b"", content)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("canonical", type=Path)
    parser.add_argument("sidecar", type=Path)
    args = parser.parse_args()

    canonical = args.canonical.read_bytes()
    sidecar = args.sidecar.read_bytes()
    stripped = strip_reader_context_blocks(sidecar)

    if stripped != canonical:
        print(
            f"sidecar mismatch: stripping READER CONTEXT SIDECAR blocks from {args.sidecar} "
            f"does not reproduce {args.canonical}",
            file=sys.stderr,
        )
        return 1

    blocks = len(BLOCK.findall(sidecar))
    if blocks == 0:
        print(
            f"sidecar mismatch: {args.sidecar} contains no READER CONTEXT SIDECAR blocks",
            file=sys.stderr,
        )
        return 1

    print(f"sidecar synchronized: {blocks} reader-context blocks; canonical bytes match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
