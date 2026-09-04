# Stage 9R — Repository / Reproducibility Refresh: C-ESD

Date: 2026-09-04
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1
Workflow SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
Submission-authoritative freeze: `CESD-THEORY-FREEZE-2026-09-04-v2`

## Status

**IN PROGRESS — infrastructure migration from superseded v1 to v2.**

This stage changes no theory. Its purpose is to make every production/reproducibility path read the repaired v2 freeze and the Stage-4R / Stage-7R verified continuations.

## Required migration

1. freeze-consistency test -> v2 freeze/registers;
2. manuscript-facing generator -> Stage-4R / Stage-7R verified objects;
3. README / reproducibility / provenance -> v2 authority;
4. Stage-10R writing contract -> repaired action set and v2 proof-status boundary;
5. CI / Makefile -> run repaired verification before output/build;
6. retain historical v1 records only for provenance, never as production authority.

## Acceptance gate

- `make verify` passes with Stage 4R and Stage 7R;
- `make outputs` is generated from repaired verified objects;
- `make paper` builds successfully;
- production infrastructure contains no authoritative v1 reference;
- v2 freeze consistency test fails if singleton positive-depth language or old freeze authority re-enters the production path.

Final verdict will be recorded after CI.