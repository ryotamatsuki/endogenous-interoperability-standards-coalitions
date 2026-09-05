PYTHON ?= python3
LATEXMK ?= latexmk

.PHONY: all verify verify-legacy outputs paper clean

# The old production chain remains non-authoritative. `verify` runs the
# continuation-reopen regressions and exact continuation kill tests.
all: verify

verify:
	$(PYTHON) verification/stage04rr_price_continuation_counterexample.py
	$(PYTHON) verification/stage04rr_localized_choice_regression.py
	$(PYTHON) verification/stage05rr_localized_price_nonexistence.py
	$(PYTHON) verification/stage04r3q_quadratic_price_nonexistence.py
	@echo "STAGE 4R3Q NO-GO: pure-quadratic localized architecture has no pure price continuation at the hostile feasible IS history"

# Historical/conditional checks retained for provenance. These reproduce the
# former maintained branch but MUST NOT be interpreted as SPNE certification.
verify-legacy:
	$(PYTHON) verification/stage04_cesd_minimal.py
	$(PYTHON) verification/stage04r_cesd_continuation_repair.py
	$(PYTHON) verification/stage07_cesd_welfare_generality.py
	$(PYTHON) verification/stage07r_cesd_welfare_refresh.py
	$(PYTHON) verification/stage11r_cesd_referee_audit.py
	$(PYTHON) verification/stage11r2_local_robustness.py
	$(PYTHON) tests/test_freeze_consistency.py

# Manuscript-facing outputs and PDF can still be regenerated for forensic
# comparison, but they are not submission-authoritative while theory is open.
outputs:
	$(PYTHON) scripts/generate_outputs.py

paper: outputs
	cd paper && $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error main.tex

clean:
	cd paper && $(LATEXMK) -C main.tex || true
	rm -f tables/generated_results.csv tables/generated_results.tex
