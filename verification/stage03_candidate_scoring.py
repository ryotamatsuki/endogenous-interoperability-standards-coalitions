"""Stage 3 candidate scoring and reduced-form coherence diagnostic.

This script is not a model proof. It reproduces the ex-ante weighted scores in
reviews/STAGE_03_MECHANISM_SEARCH_2026-09-04.md and checks the algebraic
feasibility of coalition-scope implementation crowd-out.
"""

from __future__ import annotations

import sympy as sp

WEIGHTS = {
    "prior_survival": 0.25,
    "theorem_sharpness": 0.20,
    "tractability": 0.20,
    "clarity": 0.15,
    "welfare": 0.10,
    "institutional": 0.10,
}

CANDIDATES = {
    "C1 coalition-scope competition exposure": [8, 9, 7, 9, 8, 9],
    "C2 bilateral implementation free-riding": [7, 8, 8, 9, 8, 8],
    "C3 national-incidence rent shifting": [6.5, 8.5, 6.5, 7.5, 10, 8],
    "C4 implementation economies of scope": [5, 6, 9, 9, 7, 8],
    "C5 formal-floor/private-top-up crowd-out": [3, 8, 8, 9, 8, 9],
    "C6 continuous selective erosion": [3, 6, 9, 9, 8, 8],
    "C7 directional one-way interoperability": [6, 8, 4, 7, 7, 8],
    "C8 switching/data-portability continuation": [3, 8, 3, 7, 8, 9],
    "C9 pairwise topology/endogenous links": [2, 9, 2, 6, 9, 8],
    "C10 modular complement-access": [4, 7, 5, 7, 7, 8],
}


def weighted_scores():
    w = list(WEIGHTS.values())
    return {
        name: sum(x * y for x, y in zip(scores, w))
        for name, scores in CANDIDATES.items()
    }


def crowdout_identity():
    b, kappa, chi = sp.symbols("b kappa chi", positive=True)
    a_one_partner = b / (kappa + chi)
    a_two_partners = 2 * b / (kappa + 4 * chi)
    difference = sp.factor(a_two_partners - a_one_partner)
    expected = -b * (2 * chi - kappa) / ((chi + kappa) * (4 * chi + kappa))
    assert sp.simplify(difference - expected) == 0
    return difference


def diagnostic_reversal_example():
    # Reduced-form diagnostic only. h stands for an inherited formal-regime
    # welfare wedge already present in B0/B3-type standards models; it is not
    # proposed as a new Stage-4 mechanism.
    b = 0.1
    chi = 0.1
    kappa = 0.1
    consumer_value = 0.22564102564102564
    h = 0.1

    def a_star(partners):
        return b * partners / (kappa + chi * partners**2)

    def profit(partners, a):
        return b * partners * a - 0.5 * (kappa + chi * partners**2) * a**2

    def welfare(partners, a):
        return profit(partners, a) + consumer_value * partners * a - h * partners

    a1 = a_star(1)
    a2 = a_star(2)
    delta_full = welfare(2, 1.0) - welfare(1, 1.0)
    delta_endo = welfare(2, a2) - welfare(1, a1)

    assert 0 < a2 < a1 < 1
    assert delta_full > 0
    assert delta_endo < 0
    return a1, a2, delta_full, delta_endo


if __name__ == "__main__":
    for name, score in sorted(weighted_scores().items(), key=lambda kv: -kv[1]):
        print(f"{name}: {score:.2f}")

    print("crowd-out identity:", crowdout_identity())
    print("diagnostic reversal:", diagnostic_reversal_example())
