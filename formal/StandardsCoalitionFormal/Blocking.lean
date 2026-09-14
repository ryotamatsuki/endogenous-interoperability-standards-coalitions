import Mathlib

namespace StandardsCoalitionFormal

/-- Every member of the deviating coalition must strictly gain. -/
def StrictBlock (S : Finset (Fin 3)) (oldW newW : Fin 3 → ℝ) : Prop :=
  ∀ i ∈ S, oldW i < newW i

theorem no_strict_block_if_member_not_gain
    (S : Finset (Fin 3)) (oldW newW : Fin 3 → ℝ)
    (i : Fin 3) (hi : i ∈ S) (hweak : newW i ≤ oldW i) :
    ¬ StrictBlock S oldW newW := by
  intro hblock
  have hgain := hblock i hi
  linarith

theorem pair_strict_block
    (oldW newW : Fin 3 → ℝ) (i j : Fin 3)
    (hi : oldW i < newW i)
    (hj : oldW j < newW j) :
    StrictBlock {i, j} oldW newW := by
  intro k hk
  simp only [Finset.mem_insert, Finset.mem_singleton] at hk
  rcases hk with rfl | rfl
  · exact hi
  · exact hj

end StandardsCoalitionFormal
