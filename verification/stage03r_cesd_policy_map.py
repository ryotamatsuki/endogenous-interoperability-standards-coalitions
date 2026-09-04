from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, FrozenSet, Tuple

Pair = Tuple[int, int]
Bloc = FrozenSet[int]


def pairwise_frictions(partition: Tuple[Bloc, ...], depths: Dict[Bloc, float], t_bar: float):
    owner = {}
    for C in partition:
        for i in C:
            owner[i] = C

    tau = {}
    for i, j in [(1, 2), (1, 3), (2, 3)]:
        Ci, Cj = owner[i], owner[j]
        if Ci == Cj:
            tau[(i, j)] = t_bar - depths[Ci]
        else:
            tau[(i, j)] = t_bar + 0.5 * (depths[Ci] + depths[Cj])
    return tau


def main():
    t = 2.0
    s = 0.4
    z = 0.2

    IS = (frozenset({1, 2, 3}),)
    SU12 = (frozenset({1, 2}), frozenset({3}))
    SW = (frozenset({1}), frozenset({2}), frozenset({3}))

    tau_is = pairwise_frictions(IS, {IS[0]: s}, t)
    assert tau_is[(1, 2)] == tau_is[(1, 3)] == tau_is[(2, 3)] == t - s

    tau_su = pairwise_frictions(SU12, {SU12[0]: s, SU12[1]: z}, t)
    assert tau_su[(1, 2)] == t - s
    assert tau_su[(1, 3)] == tau_su[(2, 3)] == t + (s + z) / 2

    # Pure SU-depth redistribution when outsider specificity is zero.
    tau_su_zero_out = pairwise_frictions(SU12, {SU12[0]: s, SU12[1]: 0.0}, t)
    assert abs(sum(tau_su_zero_out.values()) - 3 * t) < 1e-12

    tau_sw = pairwise_frictions(
        SW,
        {SW[0]: 0.1, SW[1]: 0.2, SW[2]: 0.3},
        t,
    )
    assert tau_sw[(1, 2)] == t + 0.15
    assert tau_sw[(1, 3)] == t + 0.20
    assert tau_sw[(2, 3)] == t + 0.25

    # Zero-depth benchmark is partition invariant.
    for rho in [IS, SU12, SW]:
        depths = {C: 0.0 for C in rho}
        tau = pairwise_frictions(rho, depths, t)
        assert all(abs(x - t) < 1e-12 for x in tau.values())

    # Cross coefficient 1/2 from the pure-redistribution normalization:
    # one within-pair derivative -1 plus two cross-pair derivatives lambda sums to zero.
    lam = 0.5
    assert abs(-1 + 2 * lam) < 1e-12

    print("C-ESD policy-map checks: PASS")
    print("IS:", tau_is)
    print("SU12:", tau_su)
    print("SW:", tau_sw)


if __name__ == "__main__":
    main()
