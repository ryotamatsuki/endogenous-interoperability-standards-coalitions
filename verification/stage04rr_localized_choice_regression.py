"""Stage 4RR regression checks for the price-continuation reopen.

This file does NOT certify a global price equilibrium. It records two exact
facts at the hostile off-path IS history:

1. unrestricted all-product choice makes the published interior price
   candidate vulnerable to a large price cut;
2. an explicit localized two-bounding-product consideration set removes that
   exact deviation, while leaving active-set/global-equilibrium certification
   for Stage 5RR.
"""
from fractions import Fraction as F

# Hostile history: IS, s_I = 1/4, x = (2/5, 1/2, 5/6).
# Published interior price candidate and shares.
p2_old = F(43, 200)          # 0.215
q2_old = F(43, 150)
pi2_old = p2_old * q2_old

# Large deviation.
p2_dev = F(87, 500)          # 0.174

# Under unrestricted all-product Salop choice, independently reconstructed.
q2_all = F(81, 125)
pi2_all = p2_dev * q2_all

assert q2_all == F(81, 125)
assert pi2_all == F(14094, 125000)
assert pi2_all > pi2_old

# Under explicit localized competition, consumers on each arc compare only
# the two products bounding that arc.  At this history the deviation makes
# firm 2 capture the entire short (firm 1, firm 2) arc of length 1/10, while
# its boundary on the (firm 2, firm 3) arc is interior.
#
# IS has common pair friction tau = 3/4 and the network term is common across
# products, so it cancels in pairwise choice.
ell_12 = F(1, 10)
ell_23 = F(1, 3)
tau = F(3, 4)
p3 = F(57, 200)              # 0.285

# firm 2's share on arc (2,3):
y_23 = ell_23 / 2 + (p3 - p2_dev) / (2 * tau)
q2_local = ell_12 + y_23
pi2_local = p2_dev * q2_local

assert y_23 == F(361, 1500)
assert q2_local == F(511, 1500)
assert pi2_local == F(14819, 250000)
assert pi2_local < pi2_old

if __name__ == "__main__":
    print("old profit", float(pi2_old), pi2_old)
    print("all-product deviation demand/profit", float(q2_all), float(pi2_all))
    print("localized deviation demand/profit", float(q2_local), float(pi2_local))
    print("REGRESSION PASS: all-product counterexample reproduced; exact deviation defeated under explicit localized choice")
