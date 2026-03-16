"""Simple HTTP API server for the Job Evaluation Engine.

Usage:
  python scripts/api_server.py --host 0.0.0.0 --port 8000

Endpoints:
  POST /evaluate
    Request JSON: { "job": ..., "candidate": ... }
    Response JSON: evaluation output (schema-compliant)

This implementation uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any, Dict, Optional

from engine.job_parser import parse_candidate_profile, parse_job_description
from engine.evaluator import evaluate_job


class EvaluationHandler(BaseHTTPRequestHandler):
    def _send_json(self, code: int, body: Any) -> None:
        payload = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_POST(self) -> None:
        if self.path != "/evaluate":
            self._send_json(404, {"error": "Not Found"})
            return

        content_length = int(self.headers.get("Content-Length", "0"))
        raw_body = self.rfile.read(content_length).decode("utf-8")

        try:
            payload = json.loads(raw_body)
        except json.JSONDecodeError as e:
            self._send_json(400, {"error": "Invalid JSON", "details": str(e)})
            return

        job_raw = payload.get("job")
        candidate_raw = payload.get("candidate")

        if job_raw is None or candidate_raw is None:
            self._send_json(
                400,
                {"error": "Payload must include 'job' and 'candidate' fields."},
            )
            return

        try:
            job = parse_job_description(job_raw)
            candidate = parse_candidate_profile(candidate_raw)
            result = evaluate_job(job, candidate)
            self._send_json(200, result.to_dict())
        except Exception as e:
            self._send_json(500, {"error": "Evaluation failed", "details": str(e)})


def run_server(host: str, port: int) -> None:
    server = HTTPServer((host, port), EvaluationHandler)
    print(f"API server listening on http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down API server")
    finally:
        server.server_close()


def main(argv: Optional[Any] = None) -> int:
    parser = argparse.ArgumentParser(description="Run the job evaluation API server")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind")
    parser.add_argument("--port", type=int, default=8000, help="Port to listen on")
    args = parser.parse_args(argv)

    run_server(args.host, args.port)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
