#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON="$(conda run -n agent which python)"

OUTPUT_DIR="$SCRIPT_DIR/standalone_verifier_result"
mkdir -p "$OUTPUT_DIR"

if [ $# -eq 0 ]; then
    # No arguments: default problem + proof from standalone_verifier/
    "$PYTHON" "$SCRIPT_DIR/verify/verify.py" \
        "$SCRIPT_DIR/standalone_verifier/problem.txt" \
        "$SCRIPT_DIR/standalone_verifier/proof.txt" \
        -o "$OUTPUT_DIR/report.md"
else
    # Pass all arguments through; argparse handles the rest
    "$PYTHON" "$SCRIPT_DIR/verify/verify.py" \
        "$@" \
        -o "$OUTPUT_DIR/report.md"
fi
