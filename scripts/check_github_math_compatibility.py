#!/usr/bin/env python3
"""Fail closed on unverified or known-bad math commands in GitHub-bound Markdown."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


COMMAND_RE = re.compile(r"\\([A-Za-z]+|[,;:!])")
BLOCK_RE = re.compile(r"\$\$(.*?)\$\$|```math\s*(.*?)```", re.DOTALL)
INLINE_RE = re.compile(r"(?<!\\)\$(?!\$)(.+?)(?<!\\)\$(?!\$)", re.DOTALL)
NON_MATH_FENCE_RE = re.compile(r"```(?!math\b).*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def math_segments(markdown: str) -> list[str]:
    segments: list[str] = []
    spans: list[tuple[int, int]] = []
    for match in BLOCK_RE.finditer(markdown):
        segments.append(match.group(1) if match.group(1) is not None else match.group(2))
        spans.append(match.span())

    scrubbed = list(markdown)
    for start, end in spans:
        scrubbed[start:end] = " " * (end - start)
    remaining = "".join(scrubbed)
    remaining = NON_MATH_FENCE_RE.sub("", remaining)
    remaining = INLINE_CODE_RE.sub("", remaining)
    segments.extend(match.group(1) for match in INLINE_RE.finditer(remaining))
    return segments


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("markdown", type=Path)
    parser.add_argument(
        "--registry",
        type=Path,
        default=Path(__file__).resolve().parent.parent
        / "references"
        / "github-math-compatibility.json",
    )
    args = parser.parse_args()

    registry = json.loads(args.registry.read_text(encoding="utf-8"))
    allowed = set(registry["allowed_commands"])
    forbidden = registry["forbidden_commands"]
    hazards = registry["markdown_escape_hazards"]

    segments = math_segments(args.markdown.read_text(encoding="utf-8"))
    commands: set[str] = set()
    failures: list[str] = []
    for segment_index, segment in enumerate(segments, start=1):
        for match in COMMAND_RE.finditer(segment):
            command = match.group(1)
            commands.add(command)
            if command in forbidden:
                failures.append(
                    f"math segment {segment_index}: \\{command}: {forbidden[command]}"
                )
            elif command in hazards:
                failures.append(
                    f"math segment {segment_index}: \\{command}: {hazards[command]}"
                )
            elif command not in allowed:
                failures.append(
                    f"math segment {segment_index}: unverified GitHub math command \\{command}; "
                    "test it through GitHub's Markdown preprocessing and live math renderer, "
                    "then add the result to the registry"
                )

    print(
        json.dumps(
            {
                "markdown": str(args.markdown),
                "math_segments": len(segments),
                "commands": [f"\\{command}" for command in sorted(commands)],
                "failures": failures,
            },
            indent=2,
        )
    )
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
