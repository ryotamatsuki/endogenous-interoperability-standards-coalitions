import Mathlib

namespace StandardsCoalitionFormal

noncomputable section

def bFixPoly (v : ℝ) : ℝ :=
  56953125 * v^6 + 1148478750 * v^5 - 39349972125 * v^4
    + 376745393700 * v^3 + 541587760155 * v^2
    - 66206241302370 * v + 454749808933693

def bFixQ (v : ℝ) : ℝ := 225 * v^2 + 2040 * v - 45929

def bFixWsu (v : ℝ) : ℝ :=
  (474609375 * v^5 + 3638671875 * v^4 - 1344462104250 * v^3
    + 8653805637750 * v^2 + 214730792807115 * v - 1757235666063241) /
  (1500 * (375 * v - 3913) * (bFixQ v)^2)

def bFixWis (v : ℝ) : ℝ :=
  ((15 * v - 157) * (15 * v + 443)) / (6000 * (15 * v - 82))

def bFixDelta (v : ℝ) : ℝ := bFixWsu v - bFixWis v

def bFixFactored (v : ℝ) : ℝ :=
  (-(15 * v - 1) * bFixPoly v) /
  (1200 * (15 * v - 82) * (375 * v - 3913) * (bFixQ v)^2)

theorem bFix_factorization (v : ℝ)
    (h15 : 15 * v - 82 ≠ 0)
    (h375 : 375 * v - 3913 ≠ 0)
    (hq : bFixQ v ≠ 0) :
    bFixDelta v = bFixFactored v := by
  simp [bFixDelta, bFixWsu, bFixWis, bFixFactored, bFixPoly, bFixQ]
  field_simp [h15, h375, hq]
  ring

theorem bFix_delta_at_cutoff : bFixDelta ((1 : ℝ) / 15) = 0 := by
  have h15 : 15 * ((1 : ℝ) / 15) - 82 ≠ 0 := by norm_num
  have h375 : 375 * ((1 : ℝ) / 15) - 3913 ≠ 0 := by norm_num
  have hq : bFixQ ((1 : ℝ) / 15) ≠ 0 := by norm_num [bFixQ]
  rw [bFix_factorization ((1 : ℝ) / 15) h15 h375 hq]
  norm_num [bFixFactored]

#print axioms bFix_factorization
#print axioms bFix_delta_at_cutoff

end StandardsCoalitionFormal
