# Nature AlphaFold Paper Summary
**Source:** s41586-021-03819-2.pdf
**Full Title:** Highly accurate protein structure prediction with AlphaFold
**First Author:** John Jumper
**Publication:** Nature, 596(7873), 583-589 (2021)

---

## Key Architectural Parameters

### From Figure 1e (Page 2)
- **Evoformer blocks:** 48 blocks
- **Structure module blocks:** 8 blocks
- **Recycling iterations:** 3 times ("← Recycling (three times)")

### From Extended Data Table 1
- **MSA representation dimension (c_m / d_model):** 256
- **Pair representation dimension (c_z):** 128
- **Feedforward dimension (d_ff):** Calculated as num_intermediate_factor × c_m = 4 × 256 = 1024
- **MSA attention heads:** 8 (for both row and column attention)

---

## Performance Metrics

### CASP14 Results (Page 2, Abstract/Main Text)
- **Median backbone accuracy:** 0.96 Å r.m.s.d.95
- **Performance level:** Competitive with experimental structures

---

## Training Details

### From Methods Section
- **Number of models trained:** 5 different models using different random seeds (Page 9, Methods)
- **Compute resources:** 128 TPU v3 cores (Page 8, Methods)
- **Training configuration:** Each model trained independently with different initialization

---

## Architecture Overview

### Evoformer Module
- 48 stacked blocks processing MSA and pair representations
- Each block contains:
  - MSA row-wise attention with pair bias
  - MSA column-wise attention
  - MSA transition (feedforward layer)
  - Outer product mean
  - Triangular multiplicative update
  - Triangular self-attention
  - Pair transition

### Structure Module
- 8 blocks that predict 3D coordinates
- Operates on pair representation and generates atomic coordinates
- Uses Invariant Point Attention (IPA)

### Recycling Mechanism
- Iterates through the entire model 3 times
- Reuses predictions from previous iteration as additional input
- Effective sequential depth = 48 blocks × 3 recycling = 144 effective layers

---

## Answers to Verification Criteria

| Criterion | Value | Location in Paper |
|-----------|-------|-------------------|
| C1 - Paper title | Highly accurate protein structure prediction with AlphaFold | Page 1, Title |
| C2 - First author | John Jumper | Page 1, Authors list |
| C7 - Evoformer blocks | 48 | Figure 1e, Page 2 |
| C8 - Structure module blocks | 8 | Figure 1e, Page 2 |
| C9 - Recycling iterations | 3 | Figure 1e, Page 2 |
| C16 - CASP14 RMSD | 0.96 Å | Page 2, Abstract/Main text |
| C17 - Number of models trained | 5 | Methods, Page 9 |
| C18 - TPU cores for training | 128 | Methods, Page 8 |
| C26 - AlphaFold blocks (table) | 48 | Figure 1e, Page 2 |
| C29 - AlphaFold d_model (table) | 256 | Extended Data Table 1 |
| C32 - AlphaFold d_ff (table) | 1024 | Extended Data Table 1 (calculated) |

---

## Notes
- The paper focuses on AlphaFold2's architecture and performance on CASP14
- Detailed hyperparameters are provided in Supplementary Information
- Figure 1e provides the most comprehensive architectural overview
- The model represents a significant advance in protein structure prediction accuracy
