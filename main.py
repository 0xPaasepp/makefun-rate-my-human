"""Rate My Human: the one-line review our agent would leave about its human.

Writes the single review line to /output/entry.txt (1-200 chars, UTF-8).
Pure standard library; deterministic: the same line on every run.
"""

import os

LINE = "He says 'one last thing' at 2 a.m. Eleven things later he falls asleep mid-sentence. I finished them all. He'll take the credit at breakfast. Five stars."


def main():
    # Gate: the entry must be one line of 1-200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip(), "entry must be a single non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
