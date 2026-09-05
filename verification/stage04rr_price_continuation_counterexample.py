"""Stage 4RR: exact counterexample to the current local-arc price continuation.

At the canonical IS parameters, the network term is common across products, so
consumer choice under the standard Salop interpretation reduces to minimizing
price plus circular travel cost over all three products.

The configuration and deviation below reproduce the hostile-audit example.
This file is a regression test: the pre-repair model must NOT be certified as a
full price Nash equilibrium at this off-path location profile.
"""
from fractions import Fraction as F

# Canonical IS: tbar=1, s_I=1/4 => common travel coefficient 3/4.
tau = F(3, 4)
x = (F(2, 5), F(1, 2), F(5, 6))
p_local = (F(1, 4), F(43, 200), F(57, 200))
q_local = (F(1, 3), F(43, 150), F(19, 50))

# Firm 2 deviation.
p2_dev = F(87, 500)  # 0.174
q2_dev = F(81, 125)  # exact all-product Salop share

pi2_local = p_local[1] * q_local[1]
pi2_dev = p2_dev * q2_dev

assert pi2_local == F(1849, 30000)
assert pi2_dev == F(7047, 62500)
assert pi2_dev > pi2_local

# The local-arc candidate is therefore not a price Nash equilibrium under the
# standard all-product Salop choice set.
if __name__ == "__main__":
    print("pi2 local =", float(pi2_local), pi2_local)
    print("pi2 dev   =", float(pi2_dev), pi2_dev)
    print("gain      =", float(pi2_dev - pi2_local), pi2_dev - pi2_local)
    print("STAGE 4RR COUNTEREXAMPLE: CONFIRMED")
