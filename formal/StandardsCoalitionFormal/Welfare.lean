import Mathlib

namespace StandardsCoalitionFormal

/-- Exact derivative dW_IS/dc for the symmetric affine-Bertrand continuation. -/
def isWelfareDerivative (a b c : ℝ) : ℝ :=
  -(a^2 * (2*b^2 + b*c + c^2)) / (4*b^2*(b + 2*c)^2)

/-- The exact IS welfare derivative is strictly negative for positive primitives. -/
theorem isWelfareDerivative_neg
    (a b c : ℝ) (ha : 0 < a) (hb : 0 < b) (hc : 0 < c) :
    isWelfareDerivative a b c < 0 := by
  have hsum : 0 < 2*b^2 + b*c + c^2 := by positivity
  have hnum : 0 < a^2 * (2*b^2 + b*c + c^2) := by positivity
  have hden : 0 < 4*b^2*(b + 2*c)^2 := by positivity
  have hneg : -(a^2 * (2*b^2 + b*c + c^2)) < 0 := neg_neg_of_pos hnum
  dsimp [isWelfareDerivative]
  exact div_neg_of_neg_of_pos hneg hden

/-- Two negative marginal links imply a positive welfare response to depth. -/
theorem welfareDepthDerivative_pos
    (dWdc dcds : ℝ) (hW : dWdc < 0) (hc : dcds < 0) :
    0 < dWdc * dcds := by
  exact mul_pos_of_neg_of_neg hW hc

end StandardsCoalitionFormal
