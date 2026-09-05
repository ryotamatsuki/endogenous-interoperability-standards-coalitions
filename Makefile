PYTHON ?= python3
LATEXMK ?= latexmk

.PHONY: all verify verify-legacy outputs paper clean

# During Stage 4RR the old production chain is not submission-authoritative.
# `verify` checks the reopen regression and repository consistency only.
all: verify

verify:
	$(PYTHON) verification/stage04rr_price_continuation_counterexample.py
	@echo "STAGE 4RR MAJOR-REOPEN: legacy SPNE certification is suspended"

# Historical/conditional checks retained for provenance.  These reproduce the
# maintained adjacent-interior branch but MUST NOT be interpreted as proving
# the unrestricted price/location continuation after the Stage 4RR counterexample.
verify-legacy:
	$(PYTHON) verification/stage04_cesd_minimal.py
	$(PYTHON) verification/stage04r_cesd_continuation_repair.py
	$(PYTHON) verification/stage07_cesd_welfare_generality.py
	$(PYTHON) verification/stage07r_cesd_welfare_refresh.py
	$(PYTHON) verification/stage11r_cesd_referee_audit.py
	$(PYTHON) verification/stage11r2_local_robustness.py
	$(PYTHON) tests/test_freeze_consistency.py

# Manuscript-facing outputs and PDF can still be regenerated for forensic
# comparison, but they are not submission-authoritative while Stage 4RR is open.
outputs:
	$(PYTHON) scripts/generate_outputs.py

paper: outputs
	cd paper && $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error main.tex

clean:
	cd paper && $(LATEXMK) -C main.tex || true
	rm -f tables/generated_results.csv tables/generated_results.tex
