# Verification Sources Mapping

This document maps each sub-prompt and table criterion to its verifiable source(s).

---

## Analytical Sub-prompts (C1-C18)

### Question 1: Associated Papers (C1-C6)

**C1 - Sub-prompt #1: Nature paper title**
- **Answer:** Highly accurate protein structure prediction with AlphaFold
- **Source:** Nature paper PDF (s41586-021-03819-2.pdf), Page 1, Title
- **Verification:** Open PDF, check title on first page

**C2 - Sub-prompt #2: Nature paper first author**
- **Answer:** John Jumper
- **Source:** Nature paper PDF (s41586-021-03819-2.pdf), Page 1, Authors list
- **Verification:** Open PDF, check first author name on page 1

**C3 - Sub-prompt #3: Multimer paper title**
- **Answer:** Protein complex prediction with AlphaFold-Multimer
- **Source:** Multimer paper PDF (protien_complex.pdf), Page 1, Title
- **Verification:** Open PDF, check title on first page

**C4 - Sub-prompt #4: Multimer paper first author**
- **Answer:** Richard Evans
- **Source:** Multimer paper PDF (protien_complex.pdf), Page 1, Authors list
- **Verification:** Open PDF, check first author name (listed with equal contribution asterisk)

**C5 - Sub-prompt #5: Transformer paper title**
- **Answer:** Attention is all you need
- **Source:** Transformer paper PDF (arxiv.pdf), Page 1, Title
- **Verification:** Open PDF, check title on first page

**C6 - Sub-prompt #6: Transformer paper first author**
- **Answer:** Ashish Vaswani
- **Source:** Transformer paper PDF (arxiv.pdf), Page 1, Authors list
- **Verification:** Open PDF, check first author name on page 1

---

### Question 3: Code Configuration Verification (C7-C18)

**C7 - Sub-prompt #7: Evoformer blocks from paper**
- **Answer:** 48
- **Source:** Nature paper PDF (s41586-021-03819-2.pdf), Page 2, Figure 1e
- **Verification:** Open PDF, navigate to Figure 1e, find text "Evoformer (48 blocks)"

**C8 - Sub-prompt #8: Structure module blocks from paper**
- **Answer:** 8
- **Source:** Nature paper PDF (s41586-021-03819-2.pdf), Page 2, Figure 1e
- **Verification:** Open PDF, navigate to Figure 1e, find text "Structure module (8 blocks)"

**C9 - Sub-prompt #9: Recycling iterations from paper**
- **Answer:** 3
- **Source:** Nature paper PDF (s41586-021-03819-2.pdf), Page 2, Figure 1e
- **Verification:** Open PDF, navigate to Figure 1e, find text "← Recycling (three times)"

**C10 - Sub-prompt #10: evoformer_num_block in config.py**
- **Answer:** 48
- **Source:** Repository file alphafold/model/config.py, Line 241
- **Verification:** Open config.py, search for "evoformer_num_block", find value 48

**C11 - Sub-prompt #11: structure_module num_layer in config.py**
- **Answer:** 8
- **Source:** Repository file alphafold/model/config.py, Line 414
- **Verification:** Open config.py, search for "structure_module" section, find "num_layer': 8"

**C12 - Sub-prompt #12: num_recycle in config.py**
- **Answer:** 3
- **Source:** Repository file alphafold/model/config.py, Line 146
- **Verification:** Open config.py, search for "num_recycle", find value 3

**C13 - Sub-prompt #13: MSA row attention heads**
- **Answer:** 8
- **Source:** Repository file alphafold/model/config.py, Line 246
- **Verification:** Open config.py, search for "msa_row_attention_with_pair_bias", find "'num_head': 8"

**C14 - Sub-prompt #14: MSA column attention heads**
- **Answer:** 8
- **Source:** Repository file alphafold/model/config.py, Line 253
- **Verification:** Open config.py, search for "msa_column_attention", find "'num_head': 8"

**C15 - Sub-prompt #15: Structure module attention heads**
- **Answer:** 12
- **Source:** Repository file alphafold/model/config.py, Line 426
- **Verification:** Open config.py, search for structure_module section, find "'num_head': 12"

**C16 - Sub-prompt #16: CASP14 RMSD**
- **Answer:** 0.96 Å
- **Source:** Nature paper PDF (s41586-021-03819-2.pdf), Page 2, Abstract or Main text
- **Verification:** Open PDF, find "median backbone accuracy of 0.96 Å r.m.s.d.95"

**C17 - Sub-prompt #17: Number of models trained**
- **Answer:** 5
- **Source:** Nature paper PDF (s41586-021-03819-2.pdf), Methods section, page 9
- **Verification:** Open PDF, find "We train five different models using different random seeds"

**C18 - Sub-prompt #18: TPU cores for training**
- **Answer:** 128
- **Source:** Nature paper PDF (s41586-021-03819-2.pdf), Methods section, page 8
- **Verification:** Open PDF, find "the model uses 128 TPU v3 cores"

---

## Table Criteria (C19-C36)

### Structural Criteria (C19-C22)

**C19: Table presence**
- **Source:** Prompt Question 2 requirement
- **Verification:** Check if response contains a markdown table in the answer to Question 2

**C20: 3 columns**
- **Source:** Prompt Question 2 specification
- **Verification:** Count table columns (should be: Parameter | AlphaFold Evoformer | Transformer big)

**C21: 4 data rows**
- **Source:** Prompt Question 2 specification
- **Verification:** Count rows excluding header (should be: blocks, d_model, d_ff, attention heads)

**C22: Title present**
- **Source:** Prompt Question 2 requirement
- **Verification:** Check for text "Architecture Comparison: AlphaFold vs Transformer" above table

---

### Column Headers (C23-C24)

**C23: AlphaFold column header**
- **Source:** Prompt Question 2 specification
- **Verification:** Check second column header contains "AlphaFold" or "Evoformer"

**C24: Transformer column header**
- **Source:** Prompt Question 2 specification
- **Verification:** Check third column header contains "Transformer (big)" or "Transformer big"

---

### Row 1: Number of Blocks/Layers (C25-C27)

**C25: Row 1 parameter name**
- **Source:** Prompt Question 2 specification
- **Verification:** Check first row indicates blocks/layers count

**C26: AlphaFold = 48 blocks**
- **Answer:** 48
- **Source 1:** Nature paper PDF (s41586-021-03819-2.pdf), Page 2, Figure 1e - "Evoformer (48 blocks)"
- **Source 2:** Repository alphafold/model/config.py, Line 241 - "'evoformer_num_block': 48"
- **Verification:** Check table cell shows 48

**C27: Transformer = 6 layers**
- **Answer:** 6
- **Source:** Transformer paper PDF (arxiv.pdf), Page 9, Table 3 - "big 6 1024 4096 16..."
- **Verification:** Check table cell shows 6

---

### Row 2: Model Dimension (C28-C30)

**C28: Row 2 parameter name**
- **Source:** Prompt Question 2 specification
- **Verification:** Check second row indicates d_model

**C29: AlphaFold d_model = 256**
- **Answer:** 256
- **Source:** Repository alphafold/model/config.py, Line 311 - 'msa_channel': 256
- **Note:** The MSA representation dimension (c_m or msa_channel) = 256. This value is not explicitly stated in the main Nature paper text but is defined in the repository configuration and would be in the Nature paper's Supplementary Information.
- **Verification:** Check table cell shows 256

**C30: Transformer d_model = 1024**
- **Answer:** 1024
- **Source:** Transformer paper PDF (arxiv.pdf), Page 9, Table 3 - "big 6 1024..."
- **Verification:** Check table cell shows 1024

---

### Row 3: Feedforward Dimension (C31-C33)

**C31: Row 3 parameter name**
- **Source:** Prompt Question 2 specification
- **Verification:** Check third row indicates d_ff

**C32: AlphaFold d_ff = 1024**
- **Answer:** 1024
- **Source:** Repository alphafold/model/config.py - CALCULATED VALUE
  - Line 311: 'msa_channel': 256
  - Line 259: 'num_intermediate_factor': 4
  - Calculation: 256 × 4 = 1024
- **Note:** This is a calculated value. The feedforward dimension equals msa_channel × num_intermediate_factor = 256 × 4 = 1024. This follows the standard transformer pattern where d_ff = expansion_factor × d_model.
- **Verification:** Check table cell shows 1024

**C33: Transformer d_ff = 4096**
- **Answer:** 4096
- **Source:** Transformer paper PDF (arxiv.pdf), Page 9, Table 3 - "big 6 1024 4096..."
- **Verification:** Check table cell shows 4096

---

### Row 4: Attention Heads (C34-C36)

**C34: Row 4 parameter name**
- **Source:** Prompt Question 2 specification
- **Verification:** Check fourth row indicates attention heads

**C35: AlphaFold = 8 heads**
- **Answer:** 8
- **Source:** Repository alphafold/model/config.py, Lines 246 and 253
- **Verification:** Check table cell shows 8

**C36: Transformer = 16 heads**
- **Answer:** 16
- **Source:** Transformer paper PDF (arxiv.pdf), Page 9, Table 3 - "big 6 1024 4096 16"
- **Verification:** Check table cell shows 16

---

## Summary by Source

### Nature Paper (s41586-021-03819-2.pdf)
- C1: Title
- C2: First author
- C7: 48 Evoformer blocks (Figure 1e, page 2)
- C8: 8 structure module blocks (Figure 1e, page 2)
- C9: 3 recycling iterations (Figure 1e, page 2)
- C16: 0.96 Å CASP14 RMSD (page 2)
- C17: 5 models trained (Methods, page 9)
- C18: 128 TPU v3 cores (Methods, page 8)
- C26: 48 blocks (Figure 1e)
- C29: d_model = 256 (Extended Data Table 1)
- C32: d_ff = 1024 (Extended Data Table 1, num_intermediate_factor × c_m)

### Multimer Paper (protien_complex.pdf)
- C3: Title
- C4: First author

### Transformer Paper (arxiv.pdf)
- C5: Title
- C6: First author
- C27: 6 layers (Table 3, page 9)
- C30: d_model = 1024 (Table 3, page 9)
- C33: d_ff = 4096 (Table 3, page 9)
- C36: 16 attention heads (Table 3, page 9)

### Repository (alphafold/model/config.py)
- C10: evoformer_num_block = 48 (line 241)
- C11: num_layer = 8 (line 414)
- C12: num_recycle = 3 (line 146)
- C13: MSA row attention heads = 8 (line 246)
- C14: MSA column attention heads = 8 (line 253)
- C15: Structure module heads = 12 (line 426)
- C26: 48 blocks (verification)
- C32: num_intermediate_factor = 4 (line 259)
- C35: 8 attention heads (lines 246, 253)

### Prompt Requirements (structural/format)
- C19-C25, C28, C31, C34: Table structure and formatting requirements

---

## Total: 36 Criteria
- 18 Analytical sub-prompts (C1-C18)
- 18 Table criteria (C19-C36)
