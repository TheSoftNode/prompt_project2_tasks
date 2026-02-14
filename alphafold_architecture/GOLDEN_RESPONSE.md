Golden Response

Parameter Efficiency with Recycling

AlphaFold employs a recycling mechanism where the same parameters are reused across multiple iterations. This architectural choice fundamentally differs from the Transformer's single-pass processing and has significant implications for parameter efficiency.

To determine AlphaFold's architectural parameters, we examine the repository's configuration [4] where the MSA representation uses a channel dimension (msa_channel) of 256 (line 311) [4]. The feedforward dimension is calculated using the num_intermediate_factor of 4 (line 259) [4], giving 256 × 4 = 1024 for the intermediate feedforward layer dimension. From the Nature paper Figure 1e [1], AlphaFold uses 48 Evoformer blocks with 3 recycling iterations. The repository configuration confirms these values at line 241 (evoformer_num_block: 48) [4] and line 146 (num_recycle: 3) [4].

Architectural parameters extracted:

AlphaFold Evoformer (from Nature paper [1] and repository [4]):
Evoformer blocks: 48 [1][4]
Recycling iterations: 3 [1][4]
d_model (msa_channel): 256 [4]
d_ff: 1024 (calculated as 256 × 4) [4]

Transformer (big) (from Attention is all you need paper, Table 3 [3]):
Encoder layers: 6 [3]
d_model: 1024 [3]
d_ff: 4096 [3]

From the Transformer paper's architecture description (Sections 3.2.2 and 3.3) [3], the weights-only matrix-parameter count formula for a single encoder layer can be derived:

Per-layer weights = 4 × d_model² + 2 × d_model × d_ff

This counts only the Q/K/V/O projection matrices and FFN weight matrices, excluding biases and LayerNorm parameters [3].

Calculations:

AlphaFold MSA-path per block (msa_row_attention + msa_column_attention + msa_transition):
Two attention modules: 2 × (4 × 256²) = 524,288 weights
One FFN (msa_transition): 2 × 256 × 1024 = 524,288 weights
Per-block total: 1,048,576 weights
AlphaFold MSA-path total: 1,048,576 × 48 = 50,331,648 weights

Transformer encoder per-layer: (4 × 1024²) + (2 × 1024 × 4096) = 12,582,912 weights
Transformer encoder total: 12,582,912 × 6 = 75,497,472 weights

Parameter Efficiency Metric:

Since AlphaFold reuses parameters through recycling while Transformer does not, the effective sequential depth differs. To account for this, we propose a parameter efficiency metric:

Efficiency = Weights-Only Matrix Parameters / Effective Sequential Depth

Where effective sequential depth is:
AlphaFold effective depth: 48 blocks × 3 recycling = 144
Transformer effective depth: 6 layers

Both architectures are compared over analogous scopes (the Evoformer MSA-path weights covering msa_row_attention, msa_column_attention, and msa_transition for AlphaFold, and the encoder-stack weights covering attention and FFN for Transformer (big)), as these are the primary sequential processing stacks in each architecture.

AlphaFold: 50,331,648 / 144 = 349,525.33 weights per unit of depth
Transformer: 75,497,472 / 6 = 12,582,912 weights per unit of depth

AlphaFold achieves better parameter efficiency when accounting for effective depth, using 349,525.33 weights per unit of depth compared to Transformer's 12,582,912 weights per unit of depth.

Architecture Comparison: AlphaFold vs Transformer

AlphaFold's architecture represents a significant evolution from the original Transformer architecture, adapted specifically for the unique challenges of protein structure prediction. While the Transformer processes sequential text data, AlphaFold processes multiple sequence alignments (MSAs) and produces 3D structural coordinates.

The table below compares the architectural parameters of the AlphaFold Evoformer [1][4] with the original Transformer (big) model from the seminal "Attention is all you need" paper. It consists of 3 columns and 4 rows. The columns show: the architectural parameter name, the corresponding value for the AlphaFold Evoformer, and the corresponding value for the Transformer (big) model. The rows compare the number of blocks/layers, the model dimension (d_model), the feedforward dimension (d_ff), and the number of attention heads.

Architecture Comparison: AlphaFold vs Transformer

| Parameter                    | AlphaFold Evoformer | Transformer (big) |
| ---------------------------- | ------------------- | ----------------- |
| Number of blocks/layers      | 48                  | 6                 |
| Model dimension (d_model)    | 256                 | 1024              |
| Feedforward dimension (d_ff) | 1024                | 4096              |
| Number of attention heads    | 8                   | 16                |

In the first data row, the parameter name is "Number of blocks/layers", the AlphaFold Evoformer cell contains the value 48, and the Transformer (big) cell contains the value 6.

In the second data row, the parameter name is "Model dimension (d_model)", the AlphaFold Evoformer cell contains the value 256, and the Transformer (big) cell contains the value 1024.

In the third data row, the parameter name is "Feedforward dimension (d_ff)", the AlphaFold Evoformer cell contains the value 1024, and the Transformer (big) cell contains the value 4096.

In the fourth data row, the parameter name is "Number of attention heads", the AlphaFold Evoformer cell contains the value 8, and the Transformer (big) cell contains the value 16.

The key distinction is that AlphaFold uses many more blocks (48 Evoformer blocks) [1][4] compared to the Transformer's 6 encoder layers [3]. This deeper architecture allows AlphaFold to iteratively refine its understanding of evolutionary relationships and structural constraints encoded in multiple sequence alignments. However, each Evoformer block operates with smaller dimensions (d_model=256) [4] compared to the Transformer (big) model (d_model=1024) [3], making each block computationally lighter. The feedforward dimension ratio is consistent between both architectures, with AlphaFold using 1024 (4× the 256 model dimension) [4] while Transformer (big) uses 4096 (4× the 1024 model dimension) [3]. AlphaFold uses 8 attention heads per operation [4] while Transformer (big) uses 16 heads, reflecting the smaller model dimension in AlphaFold's design.

References

[1] Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., Ronneberger, O., ... & Hassabis, D. (2021). Highly accurate protein structure prediction with AlphaFold. _Nature_, 596(7873), 583-589. https://doi.org/10.1038/s41586-021-03819-2

[2] Evans, R., O'Neill, M., Pritzel, A., Antropova, N., Senior, A., Green, T., ... & Hassabis, D. (2021). Protein complex prediction with AlphaFold-Multimer. _bioRxiv_. https://doi.org/10.1101/2021.10.04.463034

[3] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is all you need. In _Advances in Neural Information Processing Systems_ (Vol. 30). https://arxiv.org/abs/1706.03762v7

[4] google-deepmind/alphafold. "AlphaFold Model Configuration." alphafold/model/config.py. GitHub.
https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py
