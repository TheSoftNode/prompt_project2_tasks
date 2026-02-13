# Sub-prompts for Efficient Attention Mechanisms Analysis

This file contains atomic sub-prompts for each analytical criterion. Each sub-prompt corresponds to a specific verifiable answer from the papers.

---

## Question 1: Paper Identification (C1-C12)

Sub-prompt #1: What is the title of the Linformer paper?
Sub-prompt #1 Answer: Linformer: Self-Attention with Linear Complexity

Sub-prompt #2: Who is the first author of the Linformer paper?
Sub-prompt #2 Answer: Sinong Wang

Sub-prompt #3: What year was the Linformer paper published?
Sub-prompt #3 Answer: 2020

Sub-prompt #4: What is the publication type of Linformer?
Sub-prompt #4 Answer: arXiv preprint

Sub-prompt #5: What is the title of the Performer paper?
Sub-prompt #5 Answer: Rethinking Attention with Performers

Sub-prompt #6: Who is the first author of the Performer paper?
Sub-prompt #6 Answer: Krzysztof Choromanski

Sub-prompt #7: What year was the Performer paper published?
Sub-prompt #7 Answer: 2020

Sub-prompt #8: What is the publication type of Performer?
Sub-prompt #8 Answer: arXiv preprint

Sub-prompt #9: What is the title of the FlashAttention paper?
Sub-prompt #9 Answer: FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

Sub-prompt #10: Who is the first author of the FlashAttention paper?
Sub-prompt #10 Answer: Tri Dao

Sub-prompt #11: What year was FlashAttention published?
Sub-prompt #11 Answer: 2022

Sub-prompt #12: What conference accepted FlashAttention?
Sub-prompt #12 Answer: NeurIPS

---

## Question 2: Complexity and Technique Comparison

Note: Question 2 requires a table with 4 rows and 4 columns. Table criteria are documented separately in TABLE_CRITERIA.md.

---

## Question 3: Trade-offs Analysis (C13-C20)

Sub-prompt #13: What mathematical property does Linformer assume about the attention matrix?
Sub-prompt #13 Answer: Low-rank

Sub-prompt #14: What technique does Performer use for attention approximation?
Sub-prompt #14 Answer: Random Fourier features

Sub-prompt #15: What hardware memory hierarchy does FlashAttention optimize?
Sub-prompt #15 Answer: HBM to SRAM

Sub-prompt #16: What is Linformer's time complexity?
Sub-prompt #16 Answer: O(n)

Sub-prompt #17: What is Performer's time complexity?
Sub-prompt #17 Answer: O(n)

Sub-prompt #18: What is FlashAttention's time complexity?
Sub-prompt #18 Answer: O(n²)

Sub-prompt #19: Does Linformer produce exact attention?
Sub-prompt #19 Answer: No

Sub-prompt #20: Does FlashAttention produce exact attention?
Sub-prompt #20 Answer: Yes

---

## Criteria Mapping Summary

**Analytical Criteria (C1-C20):**

- **C1-C4**: Linformer paper details (title, author, year, venue)
- **C5-C8**: Performer paper details (title, author, year, venue)
- **C9-C12**: FlashAttention paper details (title, author, year, venue)
- **C13-C20**: Technical characteristics (complexity, exactness, techniques)

**Table Criteria (C21-C37):**

- **C21-C37**: Documented in TABLE_CRITERIA.md (17 criteria for the comparison table)

**Total analytical sub-prompts: 20**
- Q1: 12 sub-prompts (C1-C12) - Paper identification
- Q2: Table with 17 criteria documented in TABLE_CRITERIA.md
- Q3: 8 sub-prompts (C13-C20) - Technical analysis

**Grand Total: 37 criteria** (20 analytical + 17 table)
