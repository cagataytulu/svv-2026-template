#!/usr/bin/env python3
"""
seed_bugs.py — generates a personal, uniquely-buggy copy of the course codebase
for a given student ID.

USAGE (run by the student):
    python seed_bugs.py <student_id>

What it does:
    1. Copies the clean reference_lib/ into student_build/<student_id>/
    2. Uses the student ID as a deterministic random seed
    3. Selects N bugs from bug_pool.py and injects them into the copy
    4. Writes an instructor-only answer key to instructor_keys/<student_id>.json
       (this file is NOT part of the student's repo / output)

Run it twice with the same ID -> identical bugs, every time (reproducible).
Run it with a different ID -> a different set of bugs (unique per student).
"""

import argparse
import json
import random
import shutil
import sys
from pathlib import Path

from bug_pool import BUG_POOL

REFERENCE_DIR = Path(__file__).parent / "reference_lib"
BUILD_ROOT = Path(__file__).parent / "student_build"
ANSWER_KEY_ROOT = Path(__file__).parent / "instructor_keys"
NUM_BUGS = 8


def seed_bugs(student_id: str, n: int = NUM_BUGS, verbose: bool = True):
    if not REFERENCE_DIR.exists():
        raise FileNotFoundError(f"Reference codebase not found at {REFERENCE_DIR}")

    output_dir = BUILD_ROOT / student_id
    if output_dir.exists():
        shutil.rmtree(output_dir)
    shutil.copytree(REFERENCE_DIR, output_dir)

    # Deterministic selection: same student_id -> same bugs, every run.
    rng = random.Random(student_id)
    chosen_bugs = rng.sample(BUG_POOL, n)

    injected = []
    for bug in chosen_bugs:
        target_file = output_dir / bug["file"]
        source = target_file.read_text()

        occurrences = source.count(bug["find"])
        if occurrences != 1:
            raise RuntimeError(
                f"[{bug['id']}] expected exactly 1 match for its target line in "
                f"{bug['file']}, found {occurrences}. Check bug_pool.py for a stale 'find' string."
            )

        patched = source.replace(bug["find"], bug["replace"])
        target_file.write_text(patched)
        injected.append(bug)

    # Save the answer key OUTSIDE the student's build folder — instructor eyes only.
    ANSWER_KEY_ROOT.mkdir(exist_ok=True)
    answer_key_path = ANSWER_KEY_ROOT / f"{student_id}.json"
    answer_key_path.write_text(json.dumps({
        "student_id": student_id,
        "num_bugs_seeded": len(injected),
        "bugs": injected,
    }, indent=2))

    if verbose:
        print(f"Seeded {len(injected)} bugs for student '{student_id}'.")
        print(f"  Personal codebase written to: {output_dir}")
        print(f"  Answer key (instructor-only): {answer_key_path}")

    return output_dir, injected


def main():
    parser = argparse.ArgumentParser(description="Generate a personal seeded-bug codebase.")
    parser.add_argument("student_id", help="Your student ID (used as the deterministic seed)")
    parser.add_argument("--num-bugs", type=int, default=NUM_BUGS, help="How many bugs to seed")
    args = parser.parse_args()

    try:
        seed_bugs(args.student_id, n=args.num_bugs)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
