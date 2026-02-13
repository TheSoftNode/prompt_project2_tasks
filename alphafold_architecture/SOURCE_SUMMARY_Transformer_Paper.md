# Transformer Paper Summary
**Source:** arxiv.pdf
**Full Title:** Attention is all you need
**First Author:** Ashish Vaswani
**Publication:** Advances in Neural Information Processing Systems (NIPS 2017)
**arXiv:** 1706.03762

---

## Key Architectural Parameters

### From Table 3 (Page 9) - Transformer (big) Configuration
- **Number of layers (N):** 6
- **Model dimension (d_model):** 1024
- **Feedforward dimension (d_ff):** 4096
- **Number of attention heads (h):** 16
- **Attention key/value dimension (d_k = d_v):** 64 (calculated as d_model / h = 1024 / 16)

### From Table 3 (Page 9) - Transformer (base) Configuration
- **Number of layers (N):** 6
- **Model dimension (d_model):** 512
- **Feedforward dimension (d_ff):** 2048
- **Number of attention heads (h):** 8
- **Attention key/value dimension (d_k = d_v):** 64

---

## Parameter Count Formula

### From Section 3.3 - Multi-Head Attention
For a single encoder layer, parameters include:

1. **Multi-Head Attention parameters:**
   - Query projection: d_model × d_model
   - Key projection: d_model × d_model
   - Value projection: d_model × d_model
   - Output projection: d_model × d_model
   - Total attention params: 4 × d_model²

2. **Feedforward Network parameters:**
   - First layer: d_model × d_ff
   - Second layer: d_ff × d_model
   - Total FFN params: 2 × d_model × d_ff

3. **Per-layer parameter count:**
   - Total = 4 × d_model² + 2 × d_model × d_ff

### For Transformer (big):
- Attention params per layer: 4 × 1024² = 4,194,304
- FFN params per layer: 2 × 1024 × 4096 = 8,388,608
- Total per layer: 12,582,912
- Total for 6 layers: 75,497,472

---

## Computational Complexity

### From Section 3.1 - Self-Attention Complexity
- **Self-Attention:** O(n² · d)
  - n = sequence length
  - d = representation dimension (d_model)

- **Per-layer complexity comparison:**
  - Self-Attention: O(n² · d)
  - Recurrent: O(n · d²)
  - Convolutional: O(k · n · d²)

### Key Insight
The quadratic dependence on sequence length (n²) makes self-attention expensive for long sequences, but it allows parallel computation across the sequence dimension.

---

## Architecture Components

### Encoder
- Stack of N = 6 identical layers
- Each layer has two sub-layers:
  1. Multi-head self-attention mechanism
  2. Position-wise fully connected feedforward network
- Residual connections around each sub-layer
- Layer normalization after each sub-layer

### Decoder
- Stack of N = 6 identical layers
- Each layer has three sub-layers:
  1. Masked multi-head self-attention
  2. Multi-head attention over encoder output
  3. Position-wise fully connected feedforward network
- Residual connections and layer normalization

### Position-wise Feedforward Networks (Section 3.3)
- FFN(x) = max(0, xW₁ + b₁)W₂ + b₂
- Two linear transformations with ReLU activation
- d_ff = 2048 for base model, 4096 for big model

---

## Answers to Verification Criteria

| Criterion | Value | Location in Paper |
|-----------|-------|-------------------|
| C5 - Paper title | Attention is all you need | Page 1, Title |
| C6 - First author | Ashish Vaswani | Page 1, Authors list |
| C27 - Transformer layers (table) | 6 | Table 3, Page 9 |
| C30 - Transformer d_model (table) | 1024 | Table 3, Page 9 |
| C33 - Transformer d_ff (table) | 4096 | Table 3, Page 9 |
| C36 - Transformer attention heads (table) | 16 | Table 3, Page 9 |
| Parameter formula (C7) | 4×d_model² + 2×d_model×d_ff | Section 3.3 |
| Complexity formula (C38) | O(n²·d) | Section 3.1, Table 1 |

---

## Notes for Cross-Paper Analysis

### For Question 1 (Parameter Count):
- Use the parameter formula: 4×d_model² + 2×d_model×d_ff per layer
- Multiply by number of layers to get total parameters
- Apply this formula to both Transformer (big) and AlphaFold Evoformer

### For Question 3 (Computational Complexity):
- Self-attention complexity: O(n²·d)
- Compare how d_model affects computational cost:
  - Transformer (big): d_model = 1024 → cost ∝ 1024
  - AlphaFold: d_model = 256 → cost ∝ 256
  - Per-layer cost ratio: 1024/256 = 4×
- Consider effective depth:
  - Transformer: 6 layers
  - AlphaFold: 48 blocks × 3 recycling = 144 effective layers

---

## Key Contributions
- Eliminated recurrence and convolutions entirely
- Relies solely on attention mechanisms
- Achieves state-of-the-art translation results
- Significantly more parallelizable than recurrent models
- Introduced the scaled dot-product attention mechanism
