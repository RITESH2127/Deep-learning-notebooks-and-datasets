#!/usr/bin/env python3
"""Lightweight repository validation for the deep-learning notebook collection."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_NOTEBOOKS = 31
EXPECTED_DATASETS = 8


def fail(message: str) -> None:
    raise SystemExit(f"Validation failed: {message}")


def main() -> None:
    notebooks = sorted(ROOT.glob("*.ipynb"))
    datasets = sorted(ROOT.glob("*.csv"))

    if len(notebooks) != EXPECTED_NOTEBOOKS:
        fail(f"expected {EXPECTED_NOTEBOOKS} notebooks, found {len(notebooks)}")
    if len(datasets) != EXPECTED_DATASETS:
        fail(f"expected {EXPECTED_DATASETS} CSV datasets, found {len(datasets)}")

    for notebook in notebooks:
        try:
            data = json.loads(notebook.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(f"invalid notebook JSON in {notebook.name}: {exc}")
        if data.get("nbformat") not in (4, 5):
            fail(f"unsupported notebook format in {notebook.name}")

    required = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "requirements.txt",
        ROOT / "visualizations" / "repository-overview.svg",
        ROOT / "visualizations" / "learning-coverage.svg",
    ]
    for path in required:
        if not path.exists():
            fail(f"missing required file: {path.relative_to(ROOT)}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    local_links = re.findall(r"\]\((\./[^)#?]+)", readme)
    missing_links = []
    for link in local_links:
        target = (ROOT / link[2:]).resolve()
        try:
            target.relative_to(ROOT.resolve())
        except ValueError:
            missing_links.append(link)
            continue
        if not target.exists():
            missing_links.append(link)

    if missing_links:
        fail("broken local README links: " + ", ".join(sorted(set(missing_links))))

    print(f"Validated {len(notebooks)} notebooks, {len(datasets)} datasets, and README local links successfully.")


if __name__ == "__main__":
    main()
