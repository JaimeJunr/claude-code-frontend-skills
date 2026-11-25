#!/bin/sh
# Installs every plugin as a user would, in a clean config, and fails when one
# does not install: sh scripts/install_smoke.sh <source> [expected commit SHA]
# The marketplace has no versions: an installed plugin's version is the first
# 12 characters of the commit it came from, so the SHA proves what users get.
set -eu
source=${1:?usage: install_smoke.sh <path or git URL> [sha]}
sha=${2:-}
cd "$(dirname "$0")/.."
CLAUDE_CONFIG_DIR=$(mktemp -d)
export CLAUDE_CONFIG_DIR
trap 'rm -rf "$CLAUDE_CONFIG_DIR"' EXIT

claude plugin marketplace add "$source"
python3 -c 'import json; [print(p["name"]) for p in json.load(open(".claude-plugin/marketplace.json"))["plugins"]]' > "$CLAUDE_CONFIG_DIR/expected"
while read -r plugin; do
  claude plugin install "$plugin@frontend-stack" </dev/null
done < "$CLAUDE_CONFIG_DIR/expected"
claude plugin list --json > "$CLAUDE_CONFIG_DIR/installed.json"
python3 - "$CLAUDE_CONFIG_DIR" "$sha" <<'PY'
import json, sys
config, sha = sys.argv[1:]
expected = set(open(f"{config}/expected").read().split())
listed = json.load(open(f"{config}/installed.json"))
installed = {p["id"].split("@")[0]: p["version"] for p in listed}
broken = {p["id"]: p["errors"] for p in listed if p.get("errors")}
missing = sorted(expected - installed.keys())
wrong = {n: v for n, v in installed.items() if sha and v != sha[:12]}
if not expected or missing or wrong or broken:
    sys.exit(f"install smoke: missing {missing}, wrong version {wrong}, load errors {broken}, expected {len(expected)} plugins at {sha[:12] or 'any version'}")
print(f"install smoke: {len(expected)} plugins ok")
PY
