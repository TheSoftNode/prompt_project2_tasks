# Protein Complex Paper Summary
**Source:** protien_complex.pdf
**Full Title:** Protein complex prediction with AlphaFold-Multimer
**First Authors:** Richard Evans, Michael O'Neill (equal contribution)
**Publication:** bioRxiv preprint (2021)
**DOI:** 10.1101/2021.10.04.463034

---

## Key Focus
This paper extends AlphaFold2 to predict protein complexes (multiple interacting protein chains) rather than single protein structures. It introduces AlphaFold-Multimer.

---

## Architectural Modifications for Multimer

### Changes from Monomer AlphaFold
1. **Modified input features:**
   - Paired MSA construction across chains
   - Cross-chain residue indexing
   - Chain-specific tokens and features

2. **Enhanced attention mechanisms:**
   - Cross-chain attention in Evoformer
   - Modified pair representation to handle inter-chain interactions

3. **Training adaptations:**
   - Trained on protein complex structures from PDB
   - Uses chain cropping strategies
   - Interface-focused loss functions

---

## Performance Metrics

### DockQ Score Results
- **Median DockQ on benchmark:** High accuracy for various complex types
- DockQ measures quality of protein-protein interfaces:
  - DockQ > 0.23: Acceptable
  - DockQ > 0.49: Medium quality
  - DockQ > 0.80: High quality

### Benchmark Performance
- Evaluated on diverse protein complex types:
  - Homo-oligomers
  - Hetero-oligomers
  - Antibody-antigen complexes
  - Difficult targets from CASP14

---

## Core Architecture (Inherited from AlphaFold2)

### Evoformer
- Retains 48 blocks architecture from monomer model
- Processes paired MSA across multiple chains
- Enhanced to handle cross-chain interactions

### Structure Module
- Similar 8-block structure prediction module
- Adapted to predict relative positions of multiple chains
- Uses same Invariant Point Attention mechanism

### Recycling
- Maintains 3 recycling iterations
- Critical for refining complex interfaces

---

## Answers to Verification Criteria

| Criterion | Value | Location in Paper |
|-----------|-------|-------------------|
| C3 - Paper title | Protein complex prediction with AlphaFold-Multimer | Page 1, Title |
| C4 - First author | Richard Evans | Page 1, Authors list (with equal contribution marker) |

---

## Key Differences from Monomer Model

### Input Processing
- Paired MSA sequences from multiple chains
- Chain identity embeddings
- Inter-chain residue-residue features

### Training Data
- PDB structures containing multiple chains
- Filtered for biological interfaces (not crystal packing)
- Includes both homo-oligomers and hetero-oligomers

### Evaluation Focus
- Interface accuracy (DockQ scores)
- Relative chain positioning
- Complex topology prediction

---

## Relevance to Main Prompt Questions

### Question 1 (Parameter Count):
- Uses same Evoformer architecture as monomer (48 blocks)
- Same d_model = 256, d_ff = 1024
- Parameter count formula applies identically

### Question 2 (Architecture Comparison):
- Architectural parameters identical to monomer AlphaFold
- Differences are in input/output processing, not core dimensions

### Question 3 (Repository Configuration):
- Multimer model shares same core configuration
- config.py contains both monomer and multimer settings
- Core architectural parameters unchanged

---

## Notes
- This paper primarily addresses the multimer prediction problem
- Core architectural parameters (blocks, dimensions, heads) remain the same as AlphaFold2 monomer
- Main innovations are in:
  1. Input feature construction for multiple chains
  2. Training data and loss functions
  3. Handling of cross-chain interactions
- For the purposes of comparing AlphaFold to Transformer architecture, the monomer Nature paper is the primary source
- This paper confirms that the same Evoformer architecture scales to complex prediction

---

## Additional Technical Details

### Paired MSA Construction
- Sequences paired across chains using taxonomic matching
- Maintains co-evolutionary signal between interacting proteins
- Critical for predicting interfaces accurately

### Chain Permutation
- Handles chain ordering ambiguity in homo-oligomers
- Uses permutation-invariant loss during training
- Ensures model learns symmetric interactions

### Confidence Metrics
- Extends pLDDT (predicted local distance difference test) to complexes
- Introduces interface confidence scores
- PAE (Predicted Aligned Error) for relative chain positioning
