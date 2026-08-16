#!/usr/bin/env python3
"""Render a clean operational document from its annotated reader-context source."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from check_reader_context_sidecar import reader_context_block_ranges, strip_reader_context_blocks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("annotated", type=Path)
    parser.add_argument("clean", type=Path)
    args = parser.parse_args()

    if args.annotated.resolve() == args.clean.resolve():
        print("render refused: annotated source and clean output must differ", file=sys.stderr)
        return 1

    annotated = args.annotated.read_bytes()
    try:
        blocks = len(reader_context_block_ranges(annotated))
    except ValueError as error:
        print(f"render refused: {error}", file=sys.stderr)
        return 1
    if blocks == 0:
        print(
            f"render refused: {args.annotated} contains no READER CONTEXT SIDECAR blocks",
            file=sys.stderr,
        )
        return 1

    clean = strip_reader_context_blocks(annotated)
    args.clean.write_bytes(clean)
    print(f"rendered {args.clean} from {args.annotated}: removed {blocks} reader-context blocks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
