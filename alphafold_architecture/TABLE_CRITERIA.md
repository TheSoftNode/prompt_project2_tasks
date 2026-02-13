# Table Criteria for Question 2: Architecture Comparison

This document defines the evaluation criteria for the table in Question 2.

---

## Table Requirements

**Question 2** asks for: "Compare the AlphaFold architecture to the original Transformer (big) architecture in terms of number of blocks/layers, model dimension (d_model), feedforward dimension (d_ff), and number of attention heads. Create a comparison table with these four architectural parameters as rows, 'AlphaFold Evoformer' and 'Transformer (big)' as columns, and the corresponding values in each cell. The table should have a title 'Architecture Comparison: AlphaFold vs Transformer'."

---

## Structural Criteria (4 criteria: C19-C22)

### CRITERION 19 [Table Structure]
**Description:** Response contains a markdown table for Question 2.

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Question 2 explicitly requires creating a comparison table with 4 rows (architectural parameters) and 3 columns (parameter name + 2 architectures). The presence of a properly formatted markdown table is mandatory for answering this question. Without a table, the comparison data cannot be properly presented or evaluated. The table must use markdown syntax with pipe delimiters and header separators to be considered valid.

**Sources:** Not applicable - structural requirement

---

### CRITERION 20 [Table Structure]
**Description:** Table has exactly 3 columns.

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Question 2 specifies the table must have three columns: one for the parameter name, one for "AlphaFold Evoformer", and one for "Transformer (big)". A table with fewer or more columns fails to meet the specification. The 3-column structure enables side-by-side comparison of the two architectures across multiple dimensions.

**Sources:** Not applicable - structural requirement

---

### CRITERION 21 [Table Structure]
**Description:** Table has exactly 4 data rows (excluding header).

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Question 2 specifies comparing exactly four architectural parameters: (1) number of blocks/layers, (2) model dimension (d_model), (3) feedforward dimension (d_ff), and (4) number of attention heads. The table must have 4 data rows (plus 1 header row). More or fewer rows indicates either missing parameters or inclusion of incorrect parameters.

**Sources:** Not applicable - structural requirement

---

### CRITERION 22 [Table Structure]
**Description:** Table includes a title "Architecture Comparison: AlphaFold vs Transformer".

**Weight:** Major

**Numerical Weight:** 4

**Rationale:** Question 2 explicitly specifies the table "should have a title 'Architecture Comparison: AlphaFold vs Transformer'". The title provides context for the comparison and should appear immediately before or as part of the table. Minor variations in formatting (e.g., bold, heading level) are acceptable, but the core text must match.

**Sources:** Not applicable - structural requirement

---

## Content Criteria - Column Headers (2 criteria: C23-C24)

### CRITERION 23 [Table Content]
**Description:** Second column header is "AlphaFold Evoformer" or similar variant.

**Weight:** Major

**Numerical Weight:** 4

**Rationale:** Source (Nature paper, Figure 1e): "Evoformer (48 blocks)"
The second column represents the AlphaFold architecture, specifically the Evoformer component which is the main processing block. The column header should clearly identify this as "AlphaFold Evoformer", "AlphaFold", or "Evoformer". The Evoformer is the core architectural innovation in AlphaFold that processes multiple sequence alignments through attention mechanisms.

**Sources:** https://doi.org/10.1038/s41586-021-03819-2 (Nature paper, Figure 1)

---

### CRITERION 24 [Table Content]
**Description:** Third column header is "Transformer (big)" or similar variant.

**Weight:** Major

**Numerical Weight:** 4

**Rationale:** Source (Attention paper, Table 3): "big 6 1024 4096 16..."
The third column represents the Transformer (big) model from the "Attention is all you need" paper. The column header should clearly identify this as "Transformer (big)" or "Transformer big". The "(big)" designation is important as it distinguishes from the smaller "base" variant which has different hyperparameters.

**Sources:** https://arxiv.org/abs/1706.03762 (Attention paper, Table 3, page 9)

---

## Content Criteria - Row 1: Number of Blocks/Layers (3 criteria: C25-C27)

### CRITERION 25 [Table Content]
**Description:** Row 1 parameter name indicates "Number of blocks/layers" or similar.

**Weight:** Major

**Numerical Weight:** 4

**Rationale:** This row compares the depth of the two architectures. The parameter name should clearly indicate it refers to the count of repeated blocks or layers in each architecture. Acceptable variations include "Number of blocks", "Blocks/Layers", "Layer count", etc.

**Sources:** Not applicable - structural requirement

---

### CRITERION 26 [Table Content]
**Description:** Row 1, AlphaFold column shows "48" blocks.

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Source (Nature paper, Figure 1e): "Evoformer (48 blocks)"
Source (config.py, line 241): "'evoformer_num_block': 48"
AlphaFold uses exactly 48 Evoformer blocks as shown in Figure 1e of the Nature paper and confirmed in the repository's config.py file. This deep architecture allows iterative refinement of evolutionary and structural information from multiple sequence alignments. The value must be "48" (numeric values like "48 blocks" are acceptable).

**Sources:** https://doi.org/10.1038/s41586-021-03819-2 (Figure 1e), https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/config.py#L241

---

### CRITERION 27 [Table Content]
**Description:** Row 1, Transformer (big) column shows "6" layers.

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Source (Attention paper, Table 3, page 9): "big 6 1024 4096 16..."
The Transformer (big) model has N=6 layers in both the encoder and decoder stacks, as specified in Table 3 of the "Attention is all you need" paper. This is significantly fewer than AlphaFold's 48 blocks, reflecting different architectural design priorities. The value must be "6" (variations like "6 (encoder + decoder)" are acceptable).

**Sources:** https://arxiv.org/abs/1706.03762 (Table 3, page 9)

---

## Content Criteria - Row 2: Model Dimension (3 criteria: C28-C30)

### CRITERION 28 [Table Content]
**Description:** Row 2 parameter name indicates "Model dimension (d_model)" or similar.

**Weight:** Major

**Numerical Weight:** 4

**Rationale:** This row compares the primary hidden dimension used throughout each architecture. The parameter name should clearly reference "d_model" as this is the standard notation used in both papers. Acceptable variations include "Model dimension", "d_model", "Hidden dimension", etc.

**Sources:** Not applicable - structural requirement

---

### CRITERION 29 [Table Content]
**Description:** Row 2, AlphaFold column shows "256".

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Source (Repository config.py, line 311): 'msa_channel': 256. The MSA representation dimension (c_m or msa_channel) is 256, which is the primary model dimension for AlphaFold's MSA processing. This is smaller than Transformer (big)'s 1024, allowing for the much deeper 48-block architecture. While not explicitly stated in the Nature paper's main text, this value is defined in the repository configuration and would be documented in the paper's Supplementary Information. The value must be "256".

**Sources:** https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/config.py#L311

---

### CRITERION 30 [Table Content]
**Description:** Row 2, Transformer (big) column shows "1024".

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Source (Attention paper, Table 3, page 9): "big 6 1024 4096 16..."
The Transformer (big) model uses d_model = 1024 as specified in Table 3. This is the dimensionality of the input and output of each layer, and is 4x larger than AlphaFold's dimension, reflecting the tradeoff between depth (layers) and width (dimensions). The value must be "1024".

**Sources:** https://arxiv.org/abs/1706.03762 (Table 3, page 9)

---

## Content Criteria - Row 3: Feedforward Dimension (3 criteria: C31-C33)

### CRITERION 31 [Table Content]
**Description:** Row 3 parameter name indicates "Feedforward dimension (d_ff)" or similar.

**Weight:** Major

**Numerical Weight:** 4

**Rationale:** This row compares the dimension of the feedforward networks within each architecture. The parameter name should clearly reference "d_ff" as this is the standard notation. Acceptable variations include "Feedforward dimension", "d_ff", "FFN dimension", etc.

**Sources:** Not applicable - structural requirement

---

### CRITERION 32 [Table Content]
**Description:** Row 3, AlphaFold column shows "1024".

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Source (Repository config.py): This is a CALCULATED value from two configuration parameters: msa_channel = 256 (line 311) and num_intermediate_factor = 4 (line 259). The feedforward dimension equals 256 × 4 = 1024. This follows the standard transformer pattern where d_ff = expansion_factor × d_model, matching the 4× expansion ratio used in the original Transformer. The value must be "1024".

**Sources:** https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/config.py#L311 (msa_channel), https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/config.py#L259 (num_intermediate_factor)

---

### CRITERION 33 [Table Content]
**Description:** Row 3, Transformer (big) column shows "4096".

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Source (Attention paper, Table 3, page 9): "big 6 1024 4096 16..."
The Transformer (big) model uses d_ff = 4096 for the inner dimension of the feedforward networks. This is 4× the model dimension (4 × 1024 = 4096), following the standard transformer architecture pattern. The value must be "4096".

**Sources:** https://arxiv.org/abs/1706.03762 (Table 3, page 9)

---

## Content Criteria - Row 4: Attention Heads (3 criteria: C34-C36)

### CRITERION 34 [Table Content]
**Description:** Row 4 parameter name indicates "Number of attention heads" or similar.

**Weight:** Major

**Numerical Weight:** 4

**Rationale:** This row compares the number of parallel attention heads used in multi-head attention mechanisms. The parameter name should clearly indicate it refers to attention head count. Acceptable variations include "Attention heads", "Number of heads", "Head count", etc.

**Sources:** Not applicable - structural requirement

---

### CRITERION 35 [Table Content]
**Description:** Row 4, AlphaFold column shows "8".

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Source (config.py, lines 246 and 253): 'num_head': 8 for both msa_row_attention_with_pair_bias and msa_column_attention.
AlphaFold uses 8 attention heads in its MSA attention mechanisms, as specified in the configuration file. This is half the number used in Transformer (big), consistent with AlphaFold's smaller model dimension (256 vs 1024). The value must be "8".

**Sources:** https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/config.py#L246

---

### CRITERION 36 [Table Content]
**Description:** Row 4, Transformer (big) column shows "16".

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Source (Attention paper, Table 3, page 9): "big 6 1024 4096 16..."
The Transformer (big) model uses h = 16 parallel attention heads in each multi-head attention layer. This allows the model to jointly attend to information from different representation subspaces. The value must be "16".

**Sources:** https://arxiv.org/abs/1706.03762 (Table 3, page 9)

---

## Summary

**Total Criteria: 18**
- **Structural Criteria (C19-C22)**: 4 criteria
  - C19: Table presence (Critical, 5 points)
  - C20: 3 columns (Critical, 5 points)
  - C21: 4 data rows (Critical, 5 points)
  - C22: Title present (Major, 4 points)

- **Column Header Criteria (C23-C24)**: 2 criteria
  - C23: AlphaFold column header (Major, 4 points)
  - C24: Transformer column header (Major, 4 points)

- **Row 1: Blocks/Layers (C25-C27)**: 3 criteria
  - C25: Row label (Major, 4 points)
  - C26: AlphaFold = 48 (Critical, 5 points)
  - C27: Transformer = 6 (Critical, 5 points)

- **Row 2: d_model (C28-C30)**: 3 criteria
  - C28: Row label (Major, 4 points)
  - C29: AlphaFold = 256 (Critical, 5 points)
  - C30: Transformer = 1024 (Critical, 5 points)

- **Row 3: d_ff (C31-C33)**: 3 criteria
  - C31: Row label (Major, 4 points)
  - C32: AlphaFold = 1024 (Critical, 5 points)
  - C33: Transformer = 4096 (Critical, 5 points)

- **Row 4: Attention Heads (C34-C36)**: 3 criteria
  - C34: Row label (Major, 4 points)
  - C35: AlphaFold = 8 (Critical, 5 points)
  - C36: Transformer = 16 (Critical, 5 points)

**Weight Distribution:**
- Critical (5 points): 11 criteria
- Major (4 points): 7 criteria

**Total Possible Points: 83**

**Passing Threshold:** All structural criteria (C19-C21) must pass, and at least 11 out of 14 content criteria (C22-C36) must pass for the table to be considered correct.
