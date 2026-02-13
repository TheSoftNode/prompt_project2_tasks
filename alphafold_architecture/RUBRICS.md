CRITERION 1 [Accuracy]
Description: Identifies "3" as the number of recycling iterations AlphaFold uses according to the Nature paper
Weight: Critical
Numerical Weight: 5
Rationale: Source 1 (Nature paper Page 2, Figure 1e): "← Recycling (three times)"
Source 2 (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    'data': {
        'common': {
            [...]
            'max_extra_msa': 1024,
            'msa_cluster_features': True,
            'num_recycle': 3,
            'reduce_msa_clusters_by_max_templates': False,
            'resample_msa_in_recycling': True,
            [...]
        },
        [...]
    },
    [...]
})
```

AlphaFold employs 3 recycling iterations where the same parameters are reused across multiple iterations. The Nature paper Figure 1e on Page 2 shows the annotation "← Recycling (three times)" indicating that the Evoformer stack is applied three times with recycled representations. The repository configuration confirms this with the parameter num_recycle set to 3. This recycling mechanism fundamentally differs from the Transformer's single-pass processing and has significant implications for parameter efficiency.
Sources: https://doi.org/10.1038/s41586-021-03819-2, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L146

CRITERION 2 [Accuracy]
Description: Identifies "48" as the number of Evoformer blocks AlphaFold has
Weight: Critical
Numerical Weight: 5
Rationale: Source 1 (Nature paper Page 2, Figure 1e): "Evoformer (48 blocks)"
Source 2 (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    [...]
    'model': {
        'embeddings_and_evoformer': {
            'evoformer_num_block': 48,
            'evoformer': {
                [...]
            },
            [...]
        },
        [...]
    },
    [...]
})
```

AlphaFold uses exactly 48 Evoformer blocks as shown in Figure 1e of the Nature paper with the label "Evoformer (48 blocks)". The repository configuration confirms this architecture with evoformer_num_block set to 48. This deep architecture allows iterative refinement of evolutionary and structural information from multiple sequence alignments.
Sources: https://doi.org/10.1038/s41586-021-03819-2, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L241

CRITERION 3 [Accuracy]
Description: Identifies "256" as the d_model (msa_channel) for AlphaFold
Weight: Critical
Numerical Weight: 5
Rationale: Source 1 (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    [...]
    'model': {
        'embeddings_and_evoformer': {
            [...]
            'extra_msa_channel': 64,
            'extra_msa_stack_num_block': 4,
            'max_relative_feature': 32,
            'msa_channel': 256,
            'pair_channel': 128,
            [...]
        },
        [...]
    },
    [...]
})
```

Source 2 (Transformer paper Page 9, Table 3 - for comparison):
| Model | N | d_model | d_ff | h |
|-------|---|---------|------|---|
| big | 6 | 1024 | 4096 | 16|
The MSA representation uses a channel dimension (msa_channel) of 256 as specified in the repository configuration. This is AlphaFold's equivalent to d_model in the Transformer architecture, representing the primary hidden dimension for MSA processing. This dimension is smaller than Transformer (big)'s 1024 (from Table 3), allowing for the much deeper 48-block architecture while maintaining computational tractability.
Sources: https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L311, https://arxiv.org/abs/1706.03762v7

CRITERION 4 [Accuracy]
Description: Identifies "1024" as the d_ff for AlphaFold
Weight: Critical
Numerical Weight: 5
Rationale: Source 1 (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    [...]
    'model': {
        'embeddings_and_evoformer': {
            [...]
            'evoformer': {
                [...]
                'msa_transition': {
                    'dropout_rate': 0.0,
                    'num_intermediate_factor': 4,
                    'orientation': 'per_row',
                    'shared_dropout': True,
                },
                [...]
            },
            [...]
            'msa_channel': 256,
            [...]
        },
        [...]
    },
    [...]
})
```

Calculation: 256 × 4 = 1024

Source 2 (Transformer paper Page 9, Table 3 - for comparison):
| Model | N | d_model | d_ff | h |
|-------|---|---------|------|---|
| big | 6 | 1024 | 4096 | 16|
The feedforward dimension is calculated using the num_intermediate_factor of 4 multiplied by msa_channel of 256, giving 256 × 4 = 1024 for the intermediate feedforward layer dimension. This follows the standard transformer pattern where d_ff = expansion_factor × d_model, matching the 4× expansion ratio used in the original Transformer (Table 3 shows d_ff/d_model = 4096/1024 = 4).
Sources: https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L259, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L311, https://arxiv.org/abs/1706.03762v7

CRITERION 5 [Accuracy]
Description: Identifies "6" as the number of layers Transformer (big) has
Weight: Critical
Numerical Weight: 5
Rationale: Source 1 (Transformer paper Page 9, Table 3):
| Model | N | d_model | d_ff | h |
|-------|---|---------|------|---|
| big | 6 | 1024 | 4096 | 16|
Source 2 (Nature paper Page 2, Figure 1e): "Evoformer (48 blocks)"
Source 3 (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    [...]
    'model': {
        'embeddings_and_evoformer': {
            'evoformer_num_block': 48,
            [...]
        },
        [...]
    },
    [...]
})
```

The Transformer (big) model has N=6 layers in both the encoder and decoder stacks, as specified in Table 3 of the "Attention is all you need" paper on Page 9. The table entry for the "big" model shows N=6 as the number of layers. This is significantly fewer than AlphaFold's 48 blocks (confirmed by the Nature paper Figure 1e and config.py evoformer_num_block=48), reflecting different architectural design priorities - Transformers use fewer, wider layers while AlphaFold uses many more narrow layers with recycling.
Sources: https://arxiv.org/abs/1706.03762v7, https://doi.org/10.1038/s41586-021-03819-2, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L241

CRITERION 6 [Accuracy]
Description: Identifies "1024" as the d_model for Transformer (big)
Weight: Critical
Numerical Weight: 5
Rationale: Source 1 (Transformer paper Page 9, Table 3):
| Model | N | d_model | d_ff | h |
|-------|---|---------|------|---|
| big | 6 | 1024 | 4096 | 16|
Source 2 (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    [...]
    'model': {
        'embeddings_and_evoformer': {
            [...]
            'msa_channel': 256,
            [...]
        },
        [...]
    },
    [...]
})
```

The Transformer (big) model uses d_model = 1024 as specified in Table 3 on Page 9. This is the dimensionality of the input and output of each layer, and is 4x larger than AlphaFold's msa_channel dimension of 256 (confirmed by config.py), reflecting the tradeoff between depth (layers) and width (dimensions).
Sources: https://arxiv.org/abs/1706.03762v7, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L311

CRITERION 7 [Accuracy]
Description: Identifies "4096" as the d_ff for Transformer (big)
Weight: Critical
Numerical Weight: 5
Rationale: Source (Transformer paper Page 9, Table 3):
| Model | N | d_model | d_ff | h |
|-------|---|---------|------|---|
| big | 6 | 1024 | 4096 | 16|
The Transformer (big) model uses d_ff = 4096 for the inner dimension of the feedforward networks, as specified in Table 3 on Page 9. This is 4× the model dimension (4 × 1024 = 4096), following the standard transformer architecture pattern where the feedforward layer expands the representation before projecting back down.
Sources: https://arxiv.org/abs/1706.03762v7

CRITERION 8 [Accuracy]
Description: Identifies "4 × d_model² + 2 × d_model × d_ff" as the per-layer parameter formula derived from the Transformer architecture
Weight: Major
Numerical Weight: 4
Rationale: Source (Transformer paper Sections 3.2.2 and 3.3):
Section 3.2.2 (Multi-Head Attention): "MultiHead(Q, K, V) = Concat(head₁, ..., headₕ)W^O where headᵢ = Attention(QWᵢ^Q, KWᵢ^K, VWᵢ^V)"
This describes 4 weight matrices: W^Q, W^K, W^V (for queries, keys, values) and W^O (output projection)

Section 3.3 (Position-wise Feed-Forward Networks): "FFN(x) = max(0, xW₁ + b₁)W₂ + b₂"
This describes 2 weight matrices: W₁ and W₂

The per-layer parameter formula can be derived from the Transformer paper's architecture description. Section 3.2.2 describes multi-head attention with 4 weight matrices for Query, Key, Value, and Output projections, contributing 4 × d_model² parameters. Section 3.3 describes the position-wise feed-forward network with two linear transformations (W₁ and W₂), contributing 2 × d_model × d_ff parameters. Combined, the formula is: 4 × d_model² + 2 × d_model × d_ff.
Sources: https://arxiv.org/abs/1706.03762v7

CRITERION 9 [Accuracy]
Description: Calculates "37,748,736" as AlphaFold's total parameters
Weight: Major
Numerical Weight: 4
Rationale: Formula (derived from Transformer paper Sections 3.2.2 and 3.3): 4 × d_model² + 2 × d_model × d_ff
Where: 4 weight matrices in multi-head attention (W^Q, W^K, W^V, W^O) contribute 4 × d_model², and 2 weight matrices in feedforward (W₁, W₂) contribute 2 × d_model × d_ff.
Source (AlphaFold dimensions from config.py):

```python
CONFIG = ml_collections.ConfigDict({
    [...]
    'model': {
        'embeddings_and_evoformer': {
            'evoformer_num_block': 48,
            'evoformer': {
                [...]
                'msa_transition': {
                    [...]
                    'num_intermediate_factor': 4,
                    [...]
                },
                [...]
            },
            [...]
            'msa_channel': 256,  # d_model
            [...]
        },
        [...]
    },
    [...]
})
```

Calculated d_ff: msa_channel × num_intermediate_factor = 256 × 4 = 1024
Calculation:
Per-layer: (4 × 256²) + (2 × 256 × 1024) = (4 × 65,536) + (2 × 262,144) = 262,144 + 524,288 = 786,432 parameters
Total: 786,432 × 48 blocks = 37,748,736 parameters
Using the per-layer parameter formula with AlphaFold's dimensions (d_model=256, d_ff=1024), each Evoformer block contains 786,432 parameters. Multiplying by 48 blocks gives 37,748,736 total parameters for the Evoformer stack.
Sources: https://arxiv.org/abs/1706.03762v7, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L311, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L259, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L241

CRITERION 10 [Accuracy]
Description: Calculates "75,497,472" as Transformer (big)'s total parameters
Weight: Major
Numerical Weight: 4
Rationale: Formula (derived from Transformer paper Sections 3.2.2 and 3.3): 4 × d_model² + 2 × d_model × d_ff
Where: 4 weight matrices in multi-head attention (W^Q, W^K, W^V, W^O) contribute 4 × d_model², and 2 weight matrices in feedforward (W₁, W₂) contribute 2 × d_model × d_ff.
Source (Transformer (big) dimensions from Table 3, Page 9):
| Model | N | d_model | d_ff | h |
|-------|---|---------|------|---|
| big | 6 | 1024 | 4096 | 16|
Calculation:
Per-layer: (4 × 1024²) + (2 × 1024 × 4096) = (4 × 1,048,576) + (2 × 4,194,304) = 4,194,304 + 8,388,608 = 12,582,912 parameters
Total: 12,582,912 × 6 layers = 75,497,472 parameters
Using the per-layer parameter formula with Transformer (big)'s dimensions from Table 3 (d_model=1024, d_ff=4096), each layer contains 12,582,912 parameters. Multiplying by 6 layers gives 75,497,472 total parameters.
Sources: https://arxiv.org/abs/1706.03762v7

CRITERION 11 [Accuracy]
Description: Identifies "144" as the effective sequential depth for AlphaFold
Weight: Major
Numerical Weight: 4
Rationale: Source 1 (Nature paper Page 2, Figure 1e): "Evoformer (48 blocks)" and "← Recycling (three times)"
Source 2 (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    'data': {
        'common': {
            [...]
            'num_recycle': 3,
            [...]
        },
        [...]
    },
    'model': {
        'embeddings_and_evoformer': {
            'evoformer_num_block': 48,
            [...]
        },
        [...]
    },
    [...]
})
```

Calculation: 48 blocks × 3 recycling = 144
AlphaFold's effective sequential depth is calculated as 48 Evoformer blocks multiplied by 3 recycling iterations, giving an effective depth of 144. This represents the total number of sequential Evoformer applications during a forward pass.
Sources: https://doi.org/10.1038/s41586-021-03819-2, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L241, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L146

CRITERION 12 [Accuracy]
Description: Identifies "262,144" as the parameter efficiency metric value for AlphaFold
Weight: Major
Numerical Weight: 4
Rationale: AlphaFold total parameters (derived from Transformer paper formula 4×d_model²+2×d_model×d_ff applied to AlphaFold config.py values d_model=256, d_ff=1024, blocks=48):
Per-layer: (4×256²)+(2×256×1024) = 786,432; Total: 786,432×48 = 37,748,736 parameters
AlphaFold effective depth (from Nature paper Figure 1e "Evoformer (48 blocks)" and "← Recycling (three times)", confirmed by config.py):

```python
CONFIG = ml_collections.ConfigDict({
    'data': {
        'common': {
            [...]
            'num_recycle': 3,
            [...]
        },
        [...]
    },
    'model': {
        'embeddings_and_evoformer': {
            'evoformer_num_block': 48,
            [...]
        },
        [...]
    },
    [...]
})
```

Effective depth: 48 blocks × 3 recycling = 144
Calculation: 37,748,736 / 144 = 262,144 params per unit of depth
AlphaFold's parameter efficiency metric is calculated as total parameters divided by effective sequential depth, giving 262,144 params per unit of depth. This metric accounts for the recycling mechanism where the same parameters are reused multiple times.
Sources: https://doi.org/10.1038/s41586-021-03819-2, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L241, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L311, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L259, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L146, https://arxiv.org/abs/1706.03762v7

CRITERION 13 [Accuracy]
Description: Identifies "AlphaFold" as the architecture that achieves better parameter efficiency when accounting for depth
Weight: Major
Numerical Weight: 4
Rationale: AlphaFold parameter efficiency (derived from Transformer paper formula 4×d_model²+2×d_model×d_ff applied to config.py values d_model=256, d_ff=1024, blocks=48, recycling=3):
Total parameters: (4×256²+2×256×1024)×48 = 37,748,736; Effective depth: 48×3 = 144; Efficiency: 37,748,736/144 = 262,144 params per unit of depth
Transformer (big) parameter efficiency (from Transformer paper Table 3, Page 9: N=6, d_model=1024, d_ff=4096):
Total parameters: (4×1024²+2×1024×4096)×6 = 75,497,472; Effective depth: 6; Efficiency: 75,497,472/6 = 12,582,912 params per unit of depth
Source (Transformer paper Page 9, Table 3):
| Model | N | d_model | d_ff | h |
|-------|---|---------|------|---|
| big | 6 | 1024 | 4096 | 16|
Source (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    'data': {
        'common': {
            [...]
            'num_recycle': 3,
            [...]
        },
        [...]
    },
    'model': {
        'embeddings_and_evoformer': {
            'evoformer_num_block': 48,
            [...]
            'msa_channel': 256,
            [...]
        },
        [...]
    },
    [...]
})
```

Comparison:
AlphaFold: 262,144 params per unit
Transformer: 12,582,912 params per unit
Winner: AlphaFold (smaller is better)
AlphaFold achieves better parameter efficiency (262,144) compared to Transformer (12,582,912) when accounting for effective sequential depth. Despite having roughly half the total parameters (37.7M vs 75.5M), AlphaFold achieves 144 effective processing steps through recycling compared to Transformer's 6 layers, resulting in dramatically better parameter efficiency.
Sources: https://doi.org/10.1038/s41586-021-03819-2, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L241, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L311, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L259, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L146, https://arxiv.org/abs/1706.03762v7

CRITERION 14 [Accuracy]
Description: Identifies "O(n²·d)" as the per-layer computational complexity formula for self-attention in the Transformer paper
Weight: Major
Numerical Weight: 4
Rationale: Source (Transformer paper Page 7, Section 3.1, Table 1):
| Layer Type | Complexity per Layer | Sequential Operations | Maximum Path Length |
|------------|---------------------|----------------------|---------------------|
| Self-Attention | O(n²·d) | O(1) | O(1) |
| Recurrent | O(n·d²) | O(n) | O(n) |
| Convolutional | O(k·n·d²) | O(1) | O(logₖ(n)) |
The Transformer paper presents the per-layer computational complexity for self-attention as O(n²·d) in Table 1 (Section 3.1), where n is sequence length and d is model dimension. This formula shows that self-attention has quadratic complexity in sequence length, which provides the foundation for analyzing computational costs across different architectures.
Sources: https://arxiv.org/abs/1706.03762v7

CRITERION 15 [Accuracy]
Description: Identifies "48" as the number of Evoformer blocks in the repository configuration
Weight: Critical
Numerical Weight: 5
Rationale: Source 1 (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    [...]
    'model': {
        'embeddings_and_evoformer': {
            'evoformer_num_block': 48,
            [...]
        },
        [...]
    },
    [...]
})
```

Source 2 (Nature paper Page 2, Figure 1e - for verification): "Evoformer (48 blocks)"
The repository configuration file confirms evoformer_num_block set to 48. This matches the Nature paper Figure 1e specification, verifying that the implementation corresponds to the published architecture.
Sources: https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L241, https://doi.org/10.1038/s41586-021-03819-2

CRITERION 16 [Accuracy]
Description: Identifies "3" as the number of recycling iterations in the repository configuration
Weight: Critical
Numerical Weight: 5
Rationale: Source 1 (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    'data': {
        'common': {
            [...]
            'max_extra_msa': 1024,
            'msa_cluster_features': True,
            'num_recycle': 3,
            'reduce_msa_clusters_by_max_templates': False,
            [...]
        },
        [...]
    },
    [...]
})
```

Source 2 (Nature paper Page 2, Figure 1e - for verification): "← Recycling (three times)"
The repository configuration file confirms num_recycle set to 3. This matches the Nature paper Figure 1e annotation, verifying that the implementation's recycling mechanism corresponds to the published specification.
Sources: https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L146, https://doi.org/10.1038/s41586-021-03819-2

CRITERION 17 [Accuracy]
Description: Identifies "256" as the model dimension (msa_channel) in the repository configuration
Weight: Critical
Numerical Weight: 5
Rationale: Source (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    [...]
    'model': {
        'embeddings_and_evoformer': {
            [...]
            'extra_msa_channel': 64,
            'extra_msa_stack_num_block': 4,
            'max_relative_feature': 32,
            'msa_channel': 256,
            'pair_channel': 128,
            [...]
        },
        [...]
    },
    [...]
})
```

The repository configuration file specifies msa_channel as 256. This is the MSA representation dimension, which serves as AlphaFold's primary model dimension (equivalent to d_model in Transformers).
Sources: https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L311

CRITERION 18 [Accuracy]
Description: Identifies "512" as the max_msa_clusters value in the repository evaluation configuration
Weight: Major
Numerical Weight: 4
Rationale: Source (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    'data': {
        'eval': {
            [...]
            'fixed_size': True,
            'subsample_templates': False,  # We want top templates.
            'masked_msa_replace_fraction': 0.15,
            'max_msa_clusters': 512,
            'max_templates': 4,
            [...]
        },
        [...]
    },
    [...]
})
```

The repository configuration file specifies max_msa_clusters as 512. This represents the maximum number of MSA sequences (clusters) that AlphaFold processes, analogous to sequence length n in the Transformer. This value is used as the sequence length parameter when calculating computational complexity.
Sources: https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L234

CRITERION 19 [Accuracy]
Description: States "Yes" confirming repository's Evoformer blocks match the Nature paper specification
Weight: Critical
Numerical Weight: 5
Rationale: Source 1 (Nature paper Page 2, Figure 1e): "Evoformer (48 blocks)"
Source 2 (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    [...]
    'model': {
        'embeddings_and_evoformer': {
            'evoformer_num_block': 48,
            [...]
        },
        [...]
    },
    [...]
})
```

Verification: 48 = 48 ✓
The repository configuration (48 blocks) exactly matches the Nature paper Figure 1e specification ("Evoformer (48 blocks)"). This verification confirms that the implementation architecture matches the published paper.
Sources: https://doi.org/10.1038/s41586-021-03819-2, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L241

CRITERION 20 [Accuracy]
Description: States "Yes" confirming repository's recycling iterations match the Nature paper specification
Weight: Critical
Numerical Weight: 5
Rationale: Source 1 (Nature paper Page 2, Figure 1e): "← Recycling (three times)"
Source 2 (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    'data': {
        'common': {
            [...]
            'num_recycle': 3,
            [...]
        },
        [...]
    },
    [...]
})
```

Verification: 3 = 3 ✓
The repository configuration (3 iterations) exactly matches the Nature paper Figure 1e annotation ("← Recycling (three times)"). This verification confirms that the implementation's recycling mechanism matches the published specification.
Sources: https://doi.org/10.1038/s41586-021-03819-2, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L146

CRITERION 21 [Accuracy]
Description: Identifies "O(n² × d × blocks × recycling)" as the adapted formula for AlphaFold's total computational cost
Weight: Major
Numerical Weight: 4
Rationale: Source 1 (Transformer paper Page 7, Section 3.1, Table 1 - base formula):
| Layer Type | Complexity per Layer |
|------------|---------------------|
| Self-Attention | O(n²·d) |
This gives O(n²·d) per layer as the base self-attention complexity.
Source 2 (config.py - AlphaFold architecture parameters):

```python
CONFIG = ml_collections.ConfigDict({
    'data': {
        'common': {
            [...]
            'num_recycle': 3,  # recycling
            [...]
        },
        [...]
    },
    'model': {
        'embeddings_and_evoformer': {
            'evoformer_num_block': 48,  # blocks
            [...]
        },
        [...]
    },
    [...]
})
```

Adapted formula: O(n² × d × blocks × recycling) = O(n² × d × 48 × 3)
Since AlphaFold processes through 48 Evoformer blocks and recycles 3 times, the total computational cost formula adapts the Transformer's per-layer complexity O(n²·d) by multiplying by the number of blocks and recycling iterations. This accounts for AlphaFold's deeper architecture and the recycling mechanism where blocks are applied multiple times.
Sources: https://arxiv.org/abs/1706.03762v7, https://doi.org/10.1038/s41586-021-03819-2, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L241, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L146

CRITERION 22 [Accuracy]
Description: Calculates "9,663,676,416" as the computational cost for AlphaFold using n=512
Weight: Major
Numerical Weight: 4
Rationale: Formula (adapted from Transformer paper Table 1 self-attention complexity O(n²·d) extended to AlphaFold's architecture): O(n² × d × blocks × recycling)
Source (config.py - all parameter values):

```python
CONFIG = ml_collections.ConfigDict({
    'data': {
        'common': {
            [...]
            'num_recycle': 3,  # recycling
            [...]
        },
        'eval': {
            [...]
            'max_msa_clusters': 512,  # n
            [...]
        },
        [...]
    },
    'model': {
        'embeddings_and_evoformer': {
            'evoformer_num_block': 48,  # blocks
            [...]
            'msa_channel': 256,  # d
            [...]
        },
        [...]
    },
    [...]
})
```

Parameters: n=512 (max_msa_clusters), d=256 (msa_channel), blocks=48 (evoformer_num_block), recycling=3 (num_recycle)
Calculation: 512² × 256 × 48 × 3 = 262,144 × 256 × 48 × 3 = 67,108,864 × 48 × 3 = 3,221,225,472 × 3 = 9,663,676,416
Using n=512 (MSA cluster count from the eval configuration), the computational cost is calculated as 512² × 256 × 48 × 3 = 9,663,676,416 operations. This large value reflects AlphaFold's deep architecture (48 blocks) and recycling mechanism (3 iterations) applied to MSA processing.
Sources: https://arxiv.org/abs/1706.03762v7, https://doi.org/10.1038/s41586-021-03819-2, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L234, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L311, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L241, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L146

CRITERION 23 [Accuracy]
Description: Calculates "1,610,612,736" as the computational cost for Transformer (big) using n=512
Weight: Major
Numerical Weight: 4
Rationale: Formula (Transformer paper Page 7, Table 1): O(n²·d) per layer, extended to N layers: O(n² × d × N)
Source (Transformer paper Page 9, Table 3):
| Model | N | d_model | d_ff | h |
|-------|---|---------|------|---|
| big | 6 | 1024 | 4096 | 16|
Parameters: n=512 (same sequence length used for AlphaFold to enable fair comparison; AlphaFold config.py specifies max_msa_clusters=512 as its sequence length), d=1024 (d_model), N=6 (layers)
Calculation: 512² × 1024 × 6 = 262,144 × 1024 × 6 = 268,435,456 × 6 = 1,610,612,736
Using n=512 (same sequence length as AlphaFold for fair comparison), the computational cost is calculated as 512² × 1024 × 6 = 1,610,612,736 operations. This is significantly lower than AlphaFold despite Transformer's larger model dimension (1024 vs 256), because it has far fewer layers (6 vs 48) and no recycling mechanism.
Sources: https://arxiv.org/abs/1706.03762v7

CRITERION 24 [Accuracy]
Description: Calculates "6.0" as the computational cost ratio between AlphaFold and Transformer (big)
Weight: Major
Numerical Weight: 4
Rationale: Source 1 (config.py - AlphaFold parameters):

```python
CONFIG = ml_collections.ConfigDict({
    'data': {
        'common': {
            [...]
            'num_recycle': 3,  # recycling
            [...]
        },
        'eval': {
            [...]
            'max_msa_clusters': 512,  # n
            [...]
        },
        [...]
    },
    'model': {
        'embeddings_and_evoformer': {
            'evoformer_num_block': 48,  # blocks
            [...]
            'msa_channel': 256,  # d
            [...]
        },
        [...]
    },
    [...]
})
```

AlphaFold cost (formula O(n²×d×blocks×recycling), n=512, d=256, blocks=48, recycling=3): 512²×256×48×3 = 9,663,676,416
Source 2 (Transformer paper Page 9, Table 3 - Transformer parameters):
| Model | N | d_model | d_ff | h |
|-------|---|---------|------|---|
| big | 6 | 1024 | 4096 | 16|
Transformer cost (formula O(n²×d×N), n=512, d=1024, N=6): 512²×1024×6 = 1,610,612,736
Calculation: 9,663,676,416 / 1,610,612,736 = 6.0
The computational cost ratio is calculated by dividing AlphaFold's cost by Transformer's cost, giving exactly 6.0. This means AlphaFold is 6× more computationally expensive than Transformer (big) at the same sequence length.
Sources: https://arxiv.org/abs/1706.03762v7, https://doi.org/10.1038/s41586-021-03819-2, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L234, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L311, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L241, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L146

CRITERION 25 [Accuracy]
Description: States "More expensive" identifying AlphaFold as more computationally expensive than Transformer (big)
Weight: Major
Numerical Weight: 4
Rationale: Source 1 (config.py - AlphaFold parameters):

```python
CONFIG = ml_collections.ConfigDict({
    'data': {
        'common': {
            [...]
            'num_recycle': 3,  # recycling
            [...]
        },
        'eval': {
            [...]
            'max_msa_clusters': 512,  # n
            [...]
        },
        [...]
    },
    'model': {
        'embeddings_and_evoformer': {
            'evoformer_num_block': 48,  # blocks
            [...]
            'msa_channel': 256,  # d
            [...]
        },
        [...]
    },
    [...]
})
```

AlphaFold cost (formula O(n²×d×blocks×recycling), n=512, d=256, blocks=48, recycling=3): 512² × 256 × 48 × 3 = 9,663,676,416
Source 2 (Transformer paper Page 9, Table 3 - Transformer parameters):
| Model | N | d_model | d_ff | h |
|-------|---|---------|------|---|
| big | 6 | 1024 | 4096 | 16|
Transformer cost (formula O(n²×d×N), n=512, d=1024, N=6): 512² × 1024 × 6 = 1,610,612,736
Ratio: 9,663,676,416 / 1,610,612,736 = 6.0
Since the ratio is 6.0 (greater than 1.0), AlphaFold is more computationally expensive than Transformer (big). Specifically, AlphaFold is 6× more expensive, requiring 6 times as many operations for the same sequence length. This higher computational cost is justified by the complexity of protein structure prediction, which requires processing evolutionary information from MSAs and predicting 3D coordinates rather than simple sequence-to-sequence transformation.
Sources: https://arxiv.org/abs/1706.03762v7, https://doi.org/10.1038/s41586-021-03819-2, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L234, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L311, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L241, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L146

CRITERION 26 [Accuracy]
Description: States "Yes" verifying that repository parameters match the Nature paper specifications
Weight: Critical
Numerical Weight: 5
Rationale: Source 1 (Nature paper Page 2, Figure 1e):
"Evoformer (48 blocks)"
"← Recycling (three times)"
Source 2 (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    'data': {
        'common': {
            [...]
            'num_recycle': 3,
            [...]
        },
        [...]
    },
    'model': {
        'embeddings_and_evoformer': {
            'evoformer_num_block': 48,
            [...]
        },
        [...]
    },
    [...]
})
```

Verification:
Evoformer blocks: 48 (paper) = 48 (repository) ✓
Recycling iterations: 3 (paper) = 3 (repository) ✓
The repository parameters exactly match the Nature paper Figure 1e specifications. The configuration confirms 48 Evoformer blocks (matches "Evoformer (48 blocks)") and 3 recycling iterations (matches "← Recycling (three times)"). This verification ensures the implementation faithfully implements the published architecture.
Sources: https://doi.org/10.1038/s41586-021-03819-2, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L241, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L146

CRITERION 27 [Table Structure]
Description: Outputs the comparison in a table format
Weight: Critical
Numerical Weight: 5
Rationale: The prompt explicitly requests: "Create a comparison table with these four architectural parameters as rows, 'AlphaFold Evoformer' and 'Transformer (big)' as columns, and the corresponding values in each cell." The response must present the comparison as a properly formatted markdown table with pipe delimiters and header separators to be considered valid.
Sources: Prompt

CRITERION 28 [Table Structure]
Description: Formats the table with 3 columns
Weight: Critical
Numerical Weight: 5
Rationale: The prompt specifies: "Create a comparison table with these four architectural parameters as rows, 'AlphaFold Evoformer' and 'Transformer (big)' as columns." The table must have three columns: (1) Parameter name column, (2) AlphaFold Evoformer column, and (3) Transformer (big) column. The 3-column structure enables side-by-side comparison of the two architectures across multiple architectural parameters.
Sources: Prompt

CRITERION 29 [Table Structure]
Description: Formats the table with 4 data rows (excluding header)
Weight: Critical
Numerical Weight: 5
Rationale: The prompt specifies comparing exactly four architectural parameters: "number of blocks/layers, model dimension (d_model), feedforward dimension (d_ff), and number of attention heads." The table must have 4 data rows (plus 1 header row). More or fewer rows indicates either missing parameters or inclusion of incorrect parameters.
Sources: Prompt

CRITERION 30 [Table Structure]
Description: Includes "Architecture Comparison: AlphaFold vs Transformer" as the table title
Weight: Major
Numerical Weight: 4
Rationale: The prompt explicitly specifies: "The table should have... a title 'Architecture Comparison: AlphaFold vs Transformer' above it." The title provides context for the comparison and should appear immediately before or as part of the table.
Sources: Prompt

CRITERION 31 [Table Content]
Description: Includes "Parameter" (or equivalent label) as the first column header
Weight: Major
Numerical Weight: 4
Rationale: The prompt specifies the table has "four architectural parameters as rows" with a column for the parameter names alongside the two architecture columns. The first column header labels the row parameter names and must be present to make the table readable (e.g. "Parameter", "Architecture Parameter", or similar label).
Sources: Prompt

CRITERION 32 [Table Content]
Description: Includes "AlphaFold Evoformer" as the second column header
Weight: Major
Numerical Weight: 4
Rationale: The prompt explicitly specifies the table columns as: "'AlphaFold Evoformer' and 'Transformer (big)' as columns." The second column header should be "AlphaFold Evoformer" representing the AlphaFold architecture's main processing component.
Sources: Prompt

CRITERION 33 [Table Content]
Description: Includes "Transformer (big)" as the third column header
Weight: Major
Numerical Weight: 4
Rationale: The prompt explicitly specifies the table columns as: "'AlphaFold Evoformer' and 'Transformer (big)' as columns." The third column header should be "Transformer (big)" representing the Transformer model variant from the "Attention is all you need" paper.
Sources: Prompt

CRITERION 34 [Table Content]
Description: Includes "Number of blocks/layers" as Row 1 parameter name
Weight: Major
Numerical Weight: 4
Rationale: The prompt specifies comparing "number of blocks/layers" as the first architectural parameter. The parameter name should clearly indicate it refers to the count of repeated blocks or layers in each architecture.
Sources: Prompt

CRITERION 35 [Table Content]
Description: Includes "Model dimension (d_model)" as Row 2 parameter name
Weight: Major
Numerical Weight: 4
Rationale: The prompt specifies comparing "model dimension (d_model)" as the second architectural parameter. The parameter name should clearly reference "d_model" as this is the standard notation used in both papers.
Sources: Prompt

CRITERION 36 [Table Content]
Description: Includes "Feedforward dimension (d_ff)" as Row 3 parameter name
Weight: Major
Numerical Weight: 4
Rationale: The prompt specifies comparing "feedforward dimension (d_ff)" as the third architectural parameter. The parameter name should clearly reference "d_ff" as this is the standard notation.
Sources: Prompt

CRITERION 37 [Table Content]
Description: Includes "Number of attention heads" as Row 4 parameter name
Weight: Major
Numerical Weight: 4
Rationale: The prompt specifies comparing "number of attention heads" as the fourth architectural parameter. The parameter name should clearly indicate it refers to attention head count.
Sources: Prompt

CRITERION 38 [Table Content]
Description: Includes "48" as AlphaFold's "Number of blocks/layers" value in the table
Weight: Critical
Numerical Weight: 5
Rationale: Source 1 (Nature paper Page 2, Figure 1e): "Evoformer (48 blocks)"
Source 2 (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    [...]
    'model': {
        'embeddings_and_evoformer': {
            'evoformer_num_block': 48,
            [...]
        },
        [...]
    },
    [...]
})
```

The table cell for Row 1's AlphaFold Evoformer column must contain the value 48, matching the Nature paper Figure 1e ("Evoformer (48 blocks)") and config.py evoformer_num_block=48.
Sources: https://doi.org/10.1038/s41586-021-03819-2, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L241

CRITERION 39 [Table Content]
Description: Includes "6" as Transformer (big)'s "Number of blocks/layers" value in the table
Weight: Critical
Numerical Weight: 5
Rationale: Source (Transformer paper Page 9, Table 3):
| Model | N | d_model | d_ff | h |
|-------|---|---------|------|---|
| big | 6 | 1024 | 4096 | 16|
The table cell for Row 1's Transformer (big) column must contain the value 6, matching the Transformer paper Table 3 specification where N=6 for the "big" model.
Sources: https://arxiv.org/abs/1706.03762v7

CRITERION 40 [Table Content]
Description: Includes "256" as AlphaFold's "Model dimension (d_model)" value in the table
Weight: Critical
Numerical Weight: 5
Rationale: Source (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    [...]
    'model': {
        'embeddings_and_evoformer': {
            [...]
            'msa_channel': 256,
            [...]
        },
        [...]
    },
    [...]
})
```

The table cell for Row 2's AlphaFold Evoformer column must contain the value 256, matching config.py which specifies the MSA channel dimension (equivalent to d_model) as 256.
Sources: https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L311

CRITERION 41 [Table Content]
Description: Includes "1024" as Transformer (big)'s "Model dimension (d_model)" value in the table
Weight: Critical
Numerical Weight: 5
Rationale: Source (Transformer paper Page 9, Table 3):
| Model | N | d_model | d_ff | h |
|-------|---|---------|------|---|
| big | 6 | 1024 | 4096 | 16|
The table cell for Row 2's Transformer (big) column must contain the value 1024, matching the Transformer paper Table 3 where d_model=1024 for the "big" model.
Sources: https://arxiv.org/abs/1706.03762v7

CRITERION 42 [Table Content]
Description: Includes "1024" as AlphaFold's "Feedforward dimension (d_ff)" value in the table
Weight: Critical
Numerical Weight: 5
Rationale: Source (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    [...]
    'model': {
        'embeddings_and_evoformer': {
            [...]
            'evoformer': {
                [...]
                'msa_transition': {
                    'dropout_rate': 0.0,
                    'num_intermediate_factor': 4,
                    'orientation': 'per_row',
                    'shared_dropout': True,
                },
                [...]
            },
            [...]
            'msa_channel': 256,
            [...]
        },
        [...]
    },
    [...]
})
```

Calculation: msa_channel × num_intermediate_factor = 256 × 4 = 1024
The table cell for Row 3's AlphaFold Evoformer column must contain the value 1024, calculated from msa_channel (256) × num_intermediate_factor (4) = 1024.
Sources: https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L259, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L311

CRITERION 43 [Table Content]
Description: Includes "4096" as Transformer (big)'s "Feedforward dimension (d_ff)" value in the table
Weight: Critical
Numerical Weight: 5
Rationale: Source (Transformer paper Page 9, Table 3):
| Model | N | d_model | d_ff | h |
|-------|---|---------|------|---|
| big | 6 | 1024 | 4096 | 16|
The table cell for Row 3's Transformer (big) column must contain the value 4096, matching the Transformer paper Table 3 where d_ff=4096 for the "big" model.
Sources: https://arxiv.org/abs/1706.03762v7

CRITERION 44 [Table Content]
Description: Includes "8" as AlphaFold's "Number of attention heads" value in the table
Weight: Critical
Numerical Weight: 5
Rationale: Source (config.py):

```python
CONFIG = ml_collections.ConfigDict({
    [...]
    'model': {
        'embeddings_and_evoformer': {
            [...]
            'evoformer': {
                'msa_row_attention_with_pair_bias': {
                    'dropout_rate': 0.15,
                    'gating': True,
                    'num_head': 8,
                    'orientation': 'per_row',
                    'shared_dropout': True,
                },
                'msa_column_attention': {
                    'dropout_rate': 0.0,
                    'gating': True,
                    'num_head': 8,
                    'orientation': 'per_column',
                    'shared_dropout': True,
                },
                [...]
            },
            [...]
        },
        [...]
    },
    [...]
})
```

The table cell for Row 4's AlphaFold Evoformer column must contain the value 8, as specified in config.py for MSA attention mechanisms (both row and column attention use 8 heads).
Sources: https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L246, https://github.com/google-deepmind/alphafold/blob/59cbb686da5a5cf1764a347f7332d7026c1b65fb/alphafold/model/config.py#L253

CRITERION 45 [Table Content]
Description: Includes "16" as Transformer (big)'s "Number of attention heads" value in the table
Weight: Critical
Numerical Weight: 5
Rationale: Source (Transformer paper Page 9, Table 3):
| Model | N | d_model | d_ff | h |
|-------|---|---------|------|---|
| big | 6 | 1024 | 4096 | 16|
The table cell for Row 4's Transformer (big) column must contain the value 16, matching the Transformer paper Table 3 where h=16 for the "big" model.
Sources: https://arxiv.org/abs/1706.03762v7
