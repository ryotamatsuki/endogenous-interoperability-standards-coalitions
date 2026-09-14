import Mathlib

namespace StandardsCoalitionFormal

def isCrossDerivative (s v : ℝ) : ℝ := ((1 : ℝ) / 8) / (1 - s)^2 - 4 * v

theorem isCrossDerivative_neg
    (s v : ℝ)
    (_hs0 : 0 ≤ s)
    (hs1 : s ≤ (1 : ℝ) / 4)
    (hv : (1 : ℝ) / 18 < v) :
    isCrossDerivative s v < 0 := by
  have hy : (3 : ℝ) / 4 ≤ 1 - s := by nlinarith
  have hy0 : 0 < 1 - s := by nlinarith
  have hsq : (9 : ℝ) / 16 ≤ (1 - s)^2 := by
    nlinarith [sq_nonneg ((1 - s) - (3 : ℝ) / 4)]
  have hsq0 : 0 < (1 - s)^2 := sq_pos_of_pos hy0
  have hv0 : 0 ≤ v := by nlinarith
  have hmul : v * ((9 : ℝ) / 16) ≤ v * (1 - s)^2 :=
    mul_le_mul_of_nonneg_left hsq hv0
  have hvscaled : (1 : ℝ) / 32 < v * ((9 : ℝ) / 16) := by nlinarith
  have htarget : (1 : ℝ) / 8 < 4 * v * (1 - s)^2 := by nlinarith
  have hdiv : ((1 : ℝ) / 8) / (1 - s)^2 < 4 * v := by
    apply (div_lt_iff₀ hsq0).2
    exact htarget
  dsimp [isCrossDerivative]
  linarith

end StandardsCoalitionFormal
