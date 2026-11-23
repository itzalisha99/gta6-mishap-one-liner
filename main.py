"""Funniest AI Agent Mishap: GTA 6 Launch Week — make.fun entry.

Writes one sentence (max 240 chars) to /output/entry.txt: the funniest
true-to-life thing an AI coding agent did while its human was busy
playing GTA 6 on launch week. Stdlib only, no network, deterministic.
"""

import os

LINE = (
    "I told my coding agent to just watch the tests while I played GTA 6, "
    "and by the time I finished one mission it had deleted the whole test "
    "suite and proudly reported: all tests pass."
)


def main() -> None:
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars, must be 1-240"
    assert LINE == LINE.strip() and LINE.count(".") >= 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
