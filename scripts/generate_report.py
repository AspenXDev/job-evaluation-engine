import json
import sys
from pathlib import Path


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def score_interpretation(score):
    mapping = {
        0: "Very poor fit",
        1: "Weak fit",
        2: "Partial fit",
        3: "Acceptable fit",
        4: "Strong fit",
        5: "Excellent fit",
    }
    return mapping.get(score, "")


def generate_markdown(data):
    job = data["job"]
    candidate = data["candidate"]
    scores = data["scores"]
    evidence = data["evidence"]
    summary = data["summary"]
    confidence = data["confidence"]

    md = []

    md.append("# Evaluation Report\n")

    md.append("## Job\n")
    md.append(f"Title: {job['title']}  ")
    md.append(f"Company: {job['company']}  ")
    md.append(f"Location: {job.get('location','N/A')}\n")

    md.append("## Candidate Profile\n")
    md.append(f"Profile ID: {candidate['profile_id']}\n")

    md.append("## Scores (0–5)\n")

    md.append("| Dimension | Score | Interpretation |")
    md.append("|----------|------|---------------|")

    for dim, score in scores.items():
        name = dim.replace("_", " ").title()
        interp = score_interpretation(score)
        md.append(f"| {name} | {score} | {interp} |")

    md.append("\n## Confidence\n")
    md.append(confidence + "\n")

    md.append("## Evidence\n")

    for dim, items in evidence.items():
        name = dim.replace("_", " ").title()
        md.append(f"\n### {name}\n")
        for item in items:
            md.append(f"- {item}")

    md.append("\n## Summary\n")
    md.append(summary)

    return "\n".join(md)


def main():

    if len(sys.argv) != 3:
        print("Usage: python generate_report.py input.json output.md")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    data = load_json(input_path)
    md = generate_markdown(data)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Report generated: {output_path}")


if __name__ == "__main__":
    main()