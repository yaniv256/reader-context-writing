#!/usr/bin/env python3
"""Verify that a reader-context sidecar reduces exactly to its canonical file."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


MARKER = b"READER CONTEXT SIDECAR"


def reader_context_block_ranges(content: bytes) -> list[tuple[int, int]]:
    """Locate real sidecar comments while preserving examples in Markdown fences."""
    lines = content.splitlines(keepends=True)
    offsets: list[int] = []
    offset = 0
    for line in lines:
        offsets.append(offset)
        offset += len(line)

    ranges: list[tuple[int, int]] = []
    fence_char: bytes | None = None
    fence_length = 0
    index = 0
    while index < len(lines):
        stripped = lines[index].lstrip(b" \t")
        if stripped.startswith(b"```") or stripped.startswith(b"~~~"):
            char = stripped[:1]
            length = len(stripped) - len(stripped.lstrip(char))
            if fence_char is None:
                fence_char = char
                fence_length = length
            elif char == fence_char and length >= fence_length:
                fence_char = None
                fence_length = 0
            index += 1
            continue

        if (
            fence_char is None
            and lines[index].rstrip(b"\r\n") == b"<!--"
            and index + 1 < len(lines)
            and lines[index + 1].rstrip(b"\r\n") == MARKER
        ):
            end = index + 2
            while end < len(lines) and lines[end].rstrip(b"\r\n") != b"-->":
                end += 1
            if end == len(lines):
                raise ValueError("unterminated READER CONTEXT SIDECAR block")
            ranges.append((offsets[index], offsets[end] + len(lines[end])))
            index = end + 1
            continue

        index += 1

    return ranges


def strip_reader_context_blocks(content: bytes) -> bytes:
    ranges = reader_context_block_ranges(content)
    output: list[bytes] = []
    cursor = 0
    for start, end in ranges:
        output.append(content[cursor:start])
        cursor = end
    output.append(content[cursor:])
    return b"".join(output)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("clean", type=Path)
    parser.add_argument("annotated", type=Path)
    args = parser.parse_args()

    clean = args.clean.read_bytes()
    annotated = args.annotated.read_bytes()
    try:
        ranges = reader_context_block_ranges(annotated)
        stripped = strip_reader_context_blocks(annotated)
    except ValueError as error:
        print(f"sidecar mismatch: {error}", file=sys.stderr)
        return 1

    if stripped != clean:
        print(
            f"sidecar mismatch: stripping READER CONTEXT SIDECAR blocks from {args.annotated} "
            f"does not reproduce {args.clean}",
            file=sys.stderr,
        )
        return 1

    blocks = len(ranges)
    if blocks == 0:
        print(
            f"sidecar mismatch: {args.annotated} contains no READER CONTEXT SIDECAR blocks",
            file=sys.stderr,
        )
        return 1

    print(f"sidecar synchronized: {blocks} reader-context blocks; clean output bytes match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
