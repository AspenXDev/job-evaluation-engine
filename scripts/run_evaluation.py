"""CLI script to run a job evaluation.

Usage:
  python scripts/run_evaluation.py --job path/to/job.json --candidate path/to/candidate.json

Output is printed as JSON to stdout.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Ensure `src` is on path so we can import the engine package.
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from engine.job_parser import load_candidate_from_file, load_job_from_file
from engine.evaluator import evaluate_job


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Run job evaluation engine")
    parser.add_argument("--job", required=True, help="Path to job description JSON file")
    parser.add_argument("--candidate", required=True, help="Path to candidate profile JSON file")
    parser.add_argument("--output", help="Optional path to write JSON output")

    args = parser.parse_args(argv)

    job = load_job_from_file(args.job)
    candidate = load_candidate_from_file(args.candidate)

    result = evaluate_job(job, candidate)
    out = result.to_dict()

    out_json = json.dumps(out, indent=2, ensure_ascii=False)

    if args.output:
        Path(args.output).write_text(out_json, encoding="utf-8")
        print(f"Written evaluation output to {args.output}")
    else:
        print(out_json)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
