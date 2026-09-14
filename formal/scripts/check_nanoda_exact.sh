#!/usr/bin/env bash
set -euo pipefail

# Stage 7.5A independent-kernel replay.
# The lean-action bundled NanoDa module auto-detection currently expects an
# obsolete [package] TOML section. We therefore keep the proof module explicit
# and pin both external checker inputs to immutable commits.

MODULE="StandardsCoalitionFormal"
LEAN4EXPORT_COMMIT="076e8e57707e813375e8f9da8bf989799ace9680"
NANODA_REPO="https://github.com/robsimmons/nanoda_lib.git"
NANODA_COMMIT="68d5ca9db226849b41a6fff59d796ff19d0a8840"
EXPORT_DIR="_lean4export_stage075a"
NANODA_DIR="_nanoda_stage075a"
EXPORT_FILE="_nanoda_stage075a.ndjson"
CONFIG_FILE="_nanoda_stage075a.json"

cleanup() {
  rm -rf "$EXPORT_DIR" "$NANODA_DIR" "$EXPORT_FILE" "$CONFIG_FILE"
}
trap cleanup EXIT

cleanup

echo "Lean toolchain: $(cat lean-toolchain)"
echo "Lean4Export commit: $LEAN4EXPORT_COMMIT"
echo "NanoDa commit: $NANODA_COMMIT"
echo "Replay module: $MODULE"

git clone --quiet https://github.com/leanprover/lean4export.git "$EXPORT_DIR"
git -C "$EXPORT_DIR" checkout --quiet "$LEAN4EXPORT_COMMIT"
# Build the exporter against exactly the project's pinned Lean release.
cp lean-toolchain "$EXPORT_DIR/lean-toolchain"
(
  cd "$EXPORT_DIR"
  lake build
)

git clone --quiet "$NANODA_REPO" "$NANODA_DIR"
git -C "$NANODA_DIR" checkout --quiet "$NANODA_COMMIT"
(
  cd "$NANODA_DIR"
  cargo build --release
)

lake env "$EXPORT_DIR/.lake/build/bin/lean4export" "$MODULE" > "$EXPORT_FILE"

echo "Export bytes: $(wc -c < "$EXPORT_FILE")"
echo "Export lines: $(wc -l < "$EXPORT_FILE")"

cat > "$CONFIG_FILE" <<EOF
{
  "export_file_path": "$EXPORT_FILE",
  "use_stdin": false,
  "permitted_axioms": [
    "propext",
    "Classical.choice",
    "Quot.sound",
    "Lean.trustCompiler"
  ],
  "unpermitted_axiom_hard_error": true,
  "nat_extension": true,
  "string_extension": true,
  "print_success_message": true
}
EOF

"$NANODA_DIR/target/release/nanoda_bin" "$CONFIG_FILE"
echo "Independent NanoDa replay PASS for $MODULE"
