# VERIFIED VALUES FROM ALL SOURCES

## 1. FROM REPOSITORY (config.py)

**File:** `/Users/apple/Desktop/TECHDEVJS/rsk-cli/project2_tasks/alphafold_architecture/Repo/alphafold/model/config.py`

### Monomer Config (CONFIG):
- **Line 146:** `'num_recycle': 3` ✅
- **Line 241:** `'evoformer_num_block': 48` ✅
- **Line 311:** `'msa_channel': 256` ✅ (This is d_model for MSA)
- **Line 246:** `'num_head': 8` (msa_row_attention)
- **Line 252:** `'num_head': 8` (msa_column_attention)
- **Line 259:** `'num_intermediate_factor': 4` (msa_transition - this means d_ff = 4 × d_model = 1024)
- **Line 414:** `'num_layer': 8` (structure_module) ✅

### Multimer Config (CONFIG_MULTIMER):
- **Line 463:** `'evoformer_num_block': 48` ✅
- **Line 544:** `'msa_channel': 256` ✅
- **Line 657:** `'num_layer': 8` (structure_module) ✅
- **Line 677:** `'num_recycle': 20` (Note: Multimer uses 20, Monomer uses 3)

## 2. FROM NATURE ALPHAFOLD PAPER (s41586-021-03819-2.pdf)

**Source:** Page 2, Figure 1e

- **Evoformer blocks:** 48 ✅
  - Exact text: "Evoformer (48 blocks)"
- **Recycling iterations:** 3 ✅
  - Exact text: "← Recycling (three times)"
- **Structure module blocks:** 8 ✅
  - Exact text: "Structure module (8 blocks)"

**NOT FOUND in Nature paper:**
- d_model (msa_channel) = 256
- d_ff = 1024
- Number of attention heads = 8

## 3. FROM TRANSFORMER PAPER (arxiv.pdf - Attention Is All You Need)

**Source:** Page 9, Table 3 (Variations on the Transformer architecture)

### Transformer (big) - Bottom row of Table 3:
- **N (layers):** 6 ✅
- **d_model:** 1024 ✅
- **d_ff:** 4096 ✅
- **h (attention heads):** 16 ✅
- **d_k = d_v:** 64 ✅ (d_model / h = 1024 / 16 = 64)

### Transformer (base) - Row labeled "base":
- **N:** 6
- **d_model:** 512
- **d_ff:** 2048
- **h:** 8
- **d_k = d_v:** 64

**Source:** Page 5, Section 3.3 (Position-wise Feed-Forward Networks)
- **Formula:** FFN(x) = max(0, xW₁ + b₁)W₂ + b₂
- **Text:** "The dimensionality of input and output is d_model = 512, and the inner-layer has dimensionality d_ff = 2048"

**Source:** Page 6, Table 1 (Complexity per Layer)
- **Self-Attention complexity:** O(n² · d)
- **Recurrent complexity:** O(n · d²)

## 4. SUMMARY OF ALL VERIFIED VALUES

### AlphaFold Evoformer (from config.py + Nature paper):
| Parameter | Value | Source | Location |
|-----------|-------|--------|----------|
| Blocks | 48 | config.py + Nature | Line 241 + Fig 1e |
| d_model (msa_channel) | 256 | config.py | Line 311 |
| d_ff | 1024 | config.py | Line 259 (4 × 256) |
| Attention heads | 8 | config.py | Lines 246, 252 |
| Recycling | 3 | config.py + Nature | Line 146 + Fig 1e |
| Structure module layers | 8 | config.py + Nature | Line 414 + Fig 1e |

### Transformer (big) (from arxiv.pdf):
| Parameter | Value | Source | Location |
|-----------|-------|--------|----------|
| Layers (N) | 6 | Table 3 | Page 9 |
| d_model | 1024 | Table 3 | Page 9 |
| d_ff | 4096 | Table 3 | Page 9 |
| Attention heads (h) | 16 | Table 3 | Page 9 |
| d_k = d_v | 64 | Table 3 | Page 9 |

## 5. PARAMETER FORMULA (from Transformer paper)

**Cannot find explicit parameter count formula in the paper.**

The paper does NOT provide a formula like:
`params_per_layer = 2 × d_model² + 2 × d_model × d_ff`

However, we can derive it from standard Transformer architecture:
- Self-attention: 4 × d_model² (Q, K, V, O projections)
- Feed-forward: 2 × d_model × d_ff (two linear layers)
- **Total per layer ≈ 4 × d_model² + 2 × d_model × d_ff**

## 6. COMPUTATIONAL COMPLEXITY FORMULA

**Source:** Page 6, Table 1

- **Self-Attention:** O(n² · d) per layer
- Where n = sequence length, d = representation dimension (d_model)

For AlphaFold: n = MSA depth, d = 256
For Transformer: n = sentence length, d = 1024
