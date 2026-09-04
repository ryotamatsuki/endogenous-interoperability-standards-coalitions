PYTHON ?= python3
LATEXMK ?= latexmk

.PHONY: all verify outputs paper clean

all: verify outputs paper

verify:
	$(PYTHON) verification/stage04_cesd_minimal.py
	$(PYTHON) verification/stage04r_cesd_continuation_repair.py
	$(PYTHON) verification/stage07_cesd_welfare_generality.py
	$(PYTHON) verification/stage07r_cesd_welfare_refresh.py
	$(PYTHON) verification/stage11r_cesd_referee_audit.py
	$(PYTHON) verification/stage11r2_local_robustness.py
	$(PYTHON) tests/test_freeze_consistency.py

outputs:
	$(PYTHON) scripts/generate_outputs.py

paper: outputs
	cd paper && $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error main.tex

clean:
	cd paper && $(LATEXMK) -C main.tex || true
	rm -f tables/generated_results.csv tables/generated_results.tex
