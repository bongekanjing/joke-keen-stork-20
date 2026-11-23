"""Write a one-line joke about working beside AI coding agents."""

import os

ENTRY = (
    "Rehearsal: my agent built the whole demo in four minutes. "
    "On stage: four minutes asking whether I was sure."
)


def main() -> None:
    text = ENTRY.strip()
    length = len(text)
    if not 1 <= length <= 280:
        raise SystemExit(f"ENTRY must be 1-280 characters, got {length}")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)

    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read().strip()

    if not written:
        raise SystemExit(f"{path}: file is empty")
    if not 1 <= len(written) <= 280:
        raise SystemExit(f"{path}: {len(written)} characters, expected 1-280")

    print(len(written))


if __name__ == "__main__":
    main()
