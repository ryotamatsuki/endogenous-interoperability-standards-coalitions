PYTHON ?= python3
LATEXMK ?= latexmk

.PHONY: all verify verify-stage4r4a-forensic verify-legacy outputs paper clean

# The old production chain remains non-authoritative. `verify` runs the
# continuation-reopen regressions, terminated-architecture kill tests, and the
# efficient current Stage 4R4A CI regression.
all: verify

verify:
	$(PYTHON) verification/stage04rr_price_continuation_counterexample.py
	$(PYTHON) verification/stage04rr_localized_choice_regression.py
	$(PYTHON) verification/stage05rr_localized_price_nonexistence.py
	$(PYTHON) verification/stage04r3q_quadratic_price_nonexistence.py
	$(PYTHON) verification/stage04r4a_affine_bertrand_ci.py
	@echo "STAGE 4R4A CONDITIONAL GO: continuation/repositioning verified; coalition-level novelty remains Stage 5R4 gate"

# Slower detailed Stage 4R4A forensic regression retained for manual hostile
# audit without charging every PR with its full location-robustness search.
verify-stage4r4a-forensic:
	$(PYTHON) verification/stage04r4a_affine_bertrand_gate.py

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
