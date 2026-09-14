import StandardsCoalitionFormal.Core

namespace StandardsCoalitionFormal

noncomputable section

theorem bFixPoly_pos_on_audit_domain (v : ℝ)
    (hlo : (3 : ℝ) / 50 ≤ v)
    (hhi : v ≤ (4 : ℝ) / 25) :
    0 < bFixPoly v := by
  have hv0 : 0 ≤ v := by nlinarith
  have hgap : 0 ≤ (4 : ℝ) / 25 - v := by nlinarith
  have hp1 : 0 ≤ v * ((4 : ℝ) / 25 - v) := mul_nonneg hv0 hgap
  have hv2 : v^2 ≤ (16 : ℝ) / 625 := by nlinarith [hp1]
  have hv2non : 0 ≤ v^2 := sq_nonneg v
  have hgap2 : 0 ≤ (16 : ℝ) / 625 - v^2 := by nlinarith
  have hp2 : 0 ≤ v^2 * ((16 : ℝ) / 625 - v^2) := mul_nonneg hv2non hgap2
  have hv4 : v^4 ≤ (256 : ℝ) / 390625 := by nlinarith [hp2]
  have hv3 : 0 ≤ v^3 := pow_nonneg hv0 3
  have hv5 : 0 ≤ v^5 := pow_nonneg hv0 5
  have hv6 : 0 ≤ v^6 := pow_nonneg hv0 6
  dsimp [bFixPoly]
  nlinarith

theorem bFixDen_pos_on_audit_domain (v : ℝ)
    (hlo : (3 : ℝ) / 50 ≤ v)
    (hhi : v ≤ (4 : ℝ) / 25) :
    0 < 1200 * (15 * v - 82) * (375 * v - 3913) * (bFixQ v)^2 := by
  have hv0 : 0 ≤ v := by nlinarith
  have hgap : 0 ≤ (4 : ℝ) / 25 - v := by nlinarith
  have hp1 : 0 ≤ v * ((4 : ℝ) / 25 - v) := mul_nonneg hv0 hgap
  have hv2 : v^2 ≤ (16 : ℝ) / 625 := by nlinarith [hp1]
  have h15 : 15 * v - 82 < 0 := by nlinarith
  have h375 : 375 * v - 3913 < 0 := by nlinarith
  have hq : bFixQ v < 0 := by
    dsimp [bFixQ]
    nlinarith
  have h1200a : 1200 * (15 * v - 82) < 0 :=
    mul_neg_of_pos_of_neg (by norm_num) h15
  have hab : 0 < 1200 * (15 * v - 82) * (375 * v - 3913) :=
    mul_pos_of_neg_of_neg h1200a h375
  have hq2 : 0 < (bFixQ v)^2 := sq_pos_of_ne_zero (ne_of_lt hq)
  exact mul_pos hab hq2

theorem bFix_delta_pos_iff (v : ℝ)
    (hlo : (3 : ℝ) / 50 ≤ v)
    (hhi : v ≤ (4 : ℝ) / 25) :
    0 < bFixDelta v ↔ v < (1 : ℝ) / 15 := by
  have hP := bFixPoly_pos_on_audit_domain v hlo hhi
  have hden := bFixDen_pos_on_audit_domain v hlo hhi
  have h15neg : 15 * v - 82 < 0 := by nlinarith
  have h375neg : 375 * v - 3913 < 0 := by nlinarith
  have hv0 : 0 ≤ v := by nlinarith
  have hgap : 0 ≤ (4 : ℝ) / 25 - v := by nlinarith
  have hp1 : 0 ≤ v * ((4 : ℝ) / 25 - v) := mul_nonneg hv0 hgap
  have hv2 : v^2 ≤ (16 : ℝ) / 625 := by nlinarith [hp1]
  have hqneg : bFixQ v < 0 := by
    dsimp [bFixQ]
    nlinarith
  rw [bFix_factorization v (ne_of_lt h15neg) (ne_of_lt h375neg) (ne_of_lt hqneg)]
  constructor
  · intro hd
    by_contra hnot
    have hleft : -(15 * v - 1) ≤ 0 := by nlinarith
    have hnum : -(15 * v - 1) * bFixPoly v ≤ 0 :=
      mul_nonpos_of_nonpos_of_nonneg hleft (le_of_lt hP)
    have hfrac : bFixFactored v ≤ 0 := by
      dsimp [bFixFactored]
      exact div_nonpos_of_nonpos_of_nonneg hnum (le_of_lt hden)
    exact (not_lt_of_ge hfrac) hd
  · intro hcut
    have hleft : 0 < -(15 * v - 1) := by nlinarith
    have hnum : 0 < -(15 * v - 1) * bFixPoly v := mul_pos hleft hP
    dsimp [bFixFactored]
    exact div_pos hnum hden

#print axioms bFixPoly_pos_on_audit_domain
#print axioms bFix_delta_pos_iff

end StandardsCoalitionFormal
