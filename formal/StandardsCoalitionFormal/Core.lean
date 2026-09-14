import Mathlib

namespace StandardsCoalitionFormal

def bFixPoly (v : ℝ) : ℝ :=
  56953125 * v^6 + 1148478750 * v^5 - 39349972125 * v^4
    + 376745393700 * v^3 + 541587760155 * v^2
    - 66206241302370 * v + 454749808933693

def bFixQ (v : ℝ) : ℝ := 225 * v^2 + 2040 * v - 45929

def bFixNsu (v : ℝ) : ℝ :=
  474609375 * v^5 + 3638671875 * v^4 - 1344462104250 * v^3
    + 8653805637750 * v^2 + 214730792807115 * v - 1757235666063241

def bFixNis (v : ℝ) : ℝ := (15 * v - 157) * (15 * v + 443)

def bFixDsu (v : ℝ) : ℝ := 1500 * (375 * v - 3913) * (bFixQ v)^2

def bFixDis (v : ℝ) : ℝ := 6000 * (15 * v - 82)

def bFixDen (v : ℝ) : ℝ :=
  1200 * (15 * v - 82) * (375 * v - 3913) * (bFixQ v)^2

noncomputable def bFixWsu (v : ℝ) : ℝ := bFixNsu v / bFixDsu v

noncomputable def bFixWis (v : ℝ) : ℝ := bFixNis v / bFixDis v

noncomputable def bFixDelta (v : ℝ) : ℝ := bFixWsu v - bFixWis v

noncomputable def bFixFactored (v : ℝ) : ℝ :=
  (-(15 * v - 1) * bFixPoly v) / bFixDen v

theorem bFix_factorization (v : ℝ)
    (h15 : 15 * v - 82 ≠ 0)
    (h375 : 375 * v - 3913 ≠ 0)
    (hq : bFixQ v ≠ 0) :
    bFixDelta v = bFixFactored v := by
  have hDsu : bFixDsu v ≠ 0 := by
    unfold bFixDsu
    exact mul_ne_zero (mul_ne_zero (by norm_num) h375) (pow_ne_zero 2 hq)
  have hDis : bFixDis v ≠ 0 := by
    unfold bFixDis
    exact mul_ne_zero (by norm_num) h15
  have hDen : bFixDen v ≠ 0 := by
    unfold bFixDen
    exact mul_ne_zero
      (mul_ne_zero (mul_ne_zero (by norm_num) h15) h375)
      (pow_ne_zero 2 hq)
  have hDenSu :
      bFixDen v = bFixDsu v * (((4 : ℝ) / 5) * (15 * v - 82)) := by
    unfold bFixDen bFixDsu
    ring
  have hDenIs :
      bFixDen v = bFixDis v *
        (((1 : ℝ) / 5) * (375 * v - 3913) * (bFixQ v)^2) := by
    unfold bFixDen bFixDis
    ring
  have hSuMul :
      bFixWsu v * bFixDen v =
        bFixNsu v * (((4 : ℝ) / 5) * (15 * v - 82)) := by
    rw [hDenSu]
    unfold bFixWsu
    field_simp [hDsu]
  have hIsMul :
      bFixWis v * bFixDen v =
        bFixNis v * (((1 : ℝ) / 5) * (375 * v - 3913) * (bFixQ v)^2) := by
    rw [hDenIs]
    unfold bFixWis
    field_simp [hDis]
  have hPoly :
      bFixNsu v * (((4 : ℝ) / 5) * (15 * v - 82)) -
        bFixNis v * (((1 : ℝ) / 5) * (375 * v - 3913) * (bFixQ v)^2) =
      -(15 * v - 1) * bFixPoly v := by
    unfold bFixNsu bFixNis bFixQ bFixPoly
    ring
  have hDeltaMul :
      bFixDelta v * bFixDen v = -(15 * v - 1) * bFixPoly v := by
    unfold bFixDelta
    rw [sub_mul, hSuMul, hIsMul, hPoly]
  unfold bFixFactored
  exact (eq_div_iff hDen).2 hDeltaMul

theorem bFix_delta_at_cutoff : bFixDelta ((1 : ℝ) / 15) = 0 := by
  have h15 : 15 * ((1 : ℝ) / 15) - 82 ≠ 0 := by norm_num
  have h375 : 375 * ((1 : ℝ) / 15) - 3913 ≠ 0 := by norm_num
  have hq : bFixQ ((1 : ℝ) / 15) ≠ 0 := by norm_num [bFixQ]
  rw [bFix_factorization ((1 : ℝ) / 15) h15 h375 hq]
  norm_num [bFixFactored]

#print axioms bFix_factorization
#print axioms bFix_delta_at_cutoff

end StandardsCoalitionFormal
