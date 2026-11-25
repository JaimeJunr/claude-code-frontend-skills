#!/bin/sh
# The same gate as CI's `validate` job, in the same order (cheap first), minus
# the secret scan (pre-commit) and the install smoke (CI only).
# Used by the pre-push hook and by hand: sh scripts/check.sh
set -e
cd "$(dirname "$0")/.."

python3 scripts/sync.py --check
python3 -m unittest discover -s tests -q
python3 scripts/trigger_eval.py --check

# token_budget needs tiktoken; PEP 668 systems block a global pip install.
if python3 -c "import tiktoken" 2>/dev/null; then
  python3 scripts/token_budget.py
elif command -v uv >/dev/null; then
  uv run --quiet --with-requirements requirements-dev.txt python3 scripts/token_budget.py
else
  echo "check: tiktoken missing; install it or uv (pip install -r requirements-dev.txt)" >&2
  exit 1
fi

if command -v claude >/dev/null; then
  claude plugin validate . >/dev/null
  for p in plugins/*/; do claude plugin validate "$p" >/dev/null; done
  echo "plugin validate: ok"
else
  echo "check: claude CLI missing, plugin validate runs only in CI" >&2
fi
