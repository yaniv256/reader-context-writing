#!/usr/bin/env python3
"""Assert the survival budget: no top-level section may lose half its readers.

Reads `Survival: NN%` fields from a reader-context annotated source, multiplies them
in document order, and checks the cumulative figure at the end of each top-level
section against 2**-n.

Exit 1 on violation, so it can gate a build. Read-only.

The cumulative product is a BUDGET, not a forecast. Measured behaviour shows readers
who commit tend to continue, so independent multiplication understates real completion.
Its value is that it compounds: a locally tolerable passage becomes visibly expensive.
"""
from __future__ import annotations
import re, sys, argparse
from pathlib import Path

SURVIVAL = re.compile(r"^Survival:\s*(\d+)%", re.M)
TOP = re.compile(r"^## (?!Appendix)(\d+)\.\s+(.*)$")


def check(path: Path, floor: float) -> int:
    lines = path.read_text(encoding="utf-8").split("\n")
    product, scored, fails, rows = 1.0, 0, [], []
    current = None
    for line in lines:
        m = TOP.match(line)
        if m:
            n = int(m.group(1))
            if current is not None:
                target = 2.0 ** -(current)
                rows.append((current, product, target))
                if product < target * (1 - 1e-9):
                    fails.append(
                        f"section {current} ends at {product*100:.1f}% absolute survival, "
                        f"below its {target*100:.4g}% budget: it lost more than half of the "
                        f"readers who reached it, or an earlier section overspent"
                    )
            current = n
            continue
        s = SURVIVAL.match(line)
        if s:
            v = int(s.group(1))
            if not 0 < v <= 100:
                fails.append(f"implausible survival figure {v}%")
            if v > floor:
                fails.append(
                    f"survival figure {v}% exceeds the {floor}% reserved band: "
                    f"90-95 is rare and must be argued, never a default"
                )
            product *= v / 100.0
            scored += 1
    if current is not None:
        target = 2.0 ** -(current)
        rows.append((current, product, target))
        if product < target * (1 - 1e-9):
            fails.append(
                f"section {current} ends at {product*100:.1f}% absolute survival, "
                f"below its {target*100:.4g}% budget"
            )

    print(f"{scored} scored passages in {path.name}")
    print(f"{'section':>8}  {'absolute':>9}  {'budget':>8}")
    for n, p, t in rows:
        mark = "ok" if p >= t * (1 - 1e-9) else "FAIL"
        print(f"{n:>8}  {p*100:>8.1f}%  {t*100:>7.4g}%  {mark}")
    if not scored:
        print("no Survival fields found: the budget cannot be checked", file=sys.stderr)
        return 1
    for f in fails:
        print(f"FAIL: {f}", file=sys.stderr)
    return 1 if fails else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("annotated", type=Path)
    ap.add_argument("--max-band", type=float, default=95,
                    help="highest legitimate per-passage figure (default 95)")
    sys.exit(check(ap.parse_args().annotated, ap.parse_args().max_band))
