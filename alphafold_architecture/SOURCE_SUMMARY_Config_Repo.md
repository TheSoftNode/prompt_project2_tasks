# AlphaFold Repository Config Summary
**Source:** alphafold/model/config.py
**Repository:** google-deepmind/alphafold
**File:** [config.py](Repo/alphafold/model/config.py)

---

## Overview
This file contains configuration dictionaries for both monomer (CONFIG) and multimer (CONFIG_MULTIMER) AlphaFold models. Both configurations share the same core architectural parameters.

---

## Key Architectural Parameters

### Global Configuration (Monomer)

**Line 146:** `'num_recycle': 3`
- Number of recycling iterations through the model
- Matches Nature paper specification

**Line 241:** `'evoformer_num_block': 48`
- Number of Evoformer blocks in the main stack
- Matches Nature paper Figure 1e specification

---

### MSA Representation Dimensions

**Line 311:** `'msa_channel': 256`
- MSA representation dimension (equivalent to d_model)
- This is the primary model dimension for AlphaFold

**Line 312:** `'pair_channel': 128`
- Pair representation dimension (c_z)
- Used for pairwise residue-residue features

**Line 308:** `'extra_msa_channel': 64`
- Dimension for extra MSA stack processing

**Line 316:** `'seq_channel': 384`
- Sequence representation dimension

---

### Evoformer MSA Row Attention Configuration

**Lines 243-249:** `'msa_row_attention_with_pair_bias'`
```python
{
    'dropout_rate': 0.15,
    'gating': True,
    'num_head': 8,  # Line 246 - Number of attention heads
    'orientation': 'per_row',
    'shared_dropout': True,
}
```

---

### Evoformer MSA Column Attention Configuration

**Lines 250-256:** `'msa_column_attention'`
```python
{
    'dropout_rate': 0.0,
    'gating': True,
    'num_head': 8,  # Line 253 - Number of attention heads
    'orientation': 'per_column',
    'shared_dropout': True,
}
```

---

### MSA Transition (Feedforward) Configuration

**Lines 257-262:** `'msa_transition'`
```python
{
    'dropout_rate': 0.0,
    'num_intermediate_factor': 4,  # Line 259 - Expansion factor for d_ff
    'orientation': 'per_row',
    'shared_dropout': True,
}
```

**Calculated d_ff:**
- d_ff = msa_channel × num_intermediate_factor
- d_ff = 256 × 4 = 1024

---

### Structure Module Configuration

**Line 414:** `'num_layer': 8`
- Number of structure module blocks/layers
- Matches Nature paper Figure 1e specification

**Line 425:** `'num_channel': 384`
- Structure module channel dimension

**Line 426:** `'num_head': 12`
- Number of attention heads in structure module IPA (Invariant Point Attention)

**Line 427:** `'num_layer_in_transition': 3`
- Number of layers in structure module transition (feedforward) blocks

**Lines 428-431:** IPA head dimensions
```python
'num_point_qk': 4,    # Point attention query/key dimension
'num_point_v': 8,     # Point attention value dimension
'num_scalar_qk': 16,  # Scalar attention query/key dimension
'num_scalar_v': 16,   # Scalar attention value dimension
```

---

### Multimer Configuration

**Line 463:** `'evoformer_num_block': 48` (CONFIG_MULTIMER)
- Same as monomer configuration
- Confirms architectural consistency

**Line 475:** `'num_head': 8` (Multimer MSA row attention)
- Same as monomer

**Line 468:** `'num_head': 8` (Multimer MSA column attention)
- Same as monomer

**Line 481:** `'num_intermediate_factor': 4` (Multimer MSA transition)
- Same as monomer, d_ff = 1024

---

## Additional Architectural Details

### Outer Product Mean
**Line 267:** `'num_outer_channel': 32`
- Channels used in outer product mean operation

### Triangle Attention
**Lines 271-283:** Triangle attention configurations
- Starting node attention: 4 heads (Line 274)
- Ending node attention: 4 heads (Line 281)
- Note: These are separate from MSA attention heads

### Triangle Multiplication
**Lines 285-300:** Triangle multiplication configurations
- Intermediate channels: 128
- Used for pair representation updates

---

## Answers to Verification Criteria

| Criterion | Value | Line Number | Variable Name |
|-----------|-------|-------------|---------------|
| C10 - Evoformer blocks (repo) | 48 | 241 | `evoformer_num_block` |
| C11 - Structure module layers (repo) | 8 | 414 | `num_layer` |
| C12 - Recycling iterations (repo) | 3 | 146 | `num_recycle` |
| C13 - MSA row attention heads | 8 | 246 | `num_head` (msa_row_attention) |
| C14 - MSA column attention heads | 8 | 253 | `num_head` (msa_column_attention) |
| C15 - Structure module attention heads | 12 | 426 | `num_head` (structure_module) |
| C26 - AlphaFold blocks (table) | 48 | 241 | `evoformer_num_block` |
| C29 - AlphaFold d_model (table) | 256 | 311 | `msa_channel` |
| C32 - AlphaFold d_ff (table) | 1024 | 259, 311 | Calculated: `msa_channel` × `num_intermediate_factor` |
| C35 - AlphaFold attention heads (table) | 8 | 246, 253 | `num_head` |

---

## Verification Against Nature Paper

### ✓ Matches Paper Specifications
1. **Evoformer blocks:** 48 (Line 241) ✓ matches Nature paper Figure 1e
2. **Structure module layers:** 8 (Line 414) ✓ matches Nature paper Figure 1e
3. **Recycling iterations:** 3 (Line 146) ✓ matches Nature paper Figure 1e
4. **MSA channel (d_model):** 256 (Line 311) ✓ matches Nature paper Extended Data
5. **Feedforward expansion:** 4× (Line 259) ✓ standard transformer pattern
6. **MSA attention heads:** 8 (Lines 246, 253) ✓ matches paper specifications

### Repository-Paper Consistency
All core architectural parameters in the repository configuration file match the specifications provided in the Nature 2021 AlphaFold paper, confirming implementation fidelity.

---

## Computational Complexity Parameters (for Question 3)

### Effective Sequential Depth
- Evoformer blocks: 48
- Recycling iterations: 3
- **Effective depth:** 48 × 3 = 144 sequential passes

### Model Dimension Scaling
- AlphaFold d_model: 256
- Self-attention complexity: O(n² · d)
- Per-layer computational cost ∝ d_model

### Comparison with Transformer (big)
- Transformer d_model: 1024 (from Transformer paper)
- AlphaFold d_model: 256
- **Per-layer cost ratio:** 1024 / 256 = 4×
  - Transformer (big) has 4× computational cost per layer
  - But AlphaFold has 48 blocks vs Transformer's 6 layers
  - Effective depth: 144 (48×3) vs 6
  - **Total depth ratio:** 144 / 6 = 24×

---

## Notes
- The configuration is structured using ml_collections.ConfigDict
- Both monomer (CONFIG) and multimer (CONFIG_MULTIMER) share identical core architectural parameters
- Differences between monomer and multimer are mainly in input processing and training, not architecture
- All values are directly verifiable in the source file with exact line numbers
- Configuration matches published Nature paper specifications exactly
