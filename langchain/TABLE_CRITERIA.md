# TABLE CRITERIA - LangChain Text Splitters Complexity Comparison

---

## Table Structure Criteria

### Sub-prompt #23: Outputs the comparison in a table format?
**Answer:** Yes

---

### Sub-prompt #24: Formats the table with 5 columns?
**Answer:** Yes

---

### Sub-prompt #25: Formats the table with 4 rows (excluding header)?
**Answer:** Yes

---

## Column Header Criteria

### Sub-prompt #26: Does the comparison table include "Algorithm" as a column header?
**Answer:** Yes

---

### Sub-prompt #27: Does the comparison table include "Recursion Type" as a column header?
**Answer:** Yes

---

### Sub-prompt #28: Does the comparison table include "Max Depth Formula" as a column header?
**Answer:** Yes

---

### Sub-prompt #29: Does the comparison table include "Primary Data Structure" as a column header?
**Answer:** Yes

---

### Sub-prompt #30: Does the comparison table include "Worst-Case Complexity" as a column header?
**Answer:** Yes

---

## Row Entry Criteria

### Sub-prompt #31: Does the comparison table include RecursiveCharacterTextSplitter as a row?
**Answer:** Yes

---

### Sub-prompt #32: Does the comparison table include RecursiveJsonSplitter as a row?
**Answer:** Yes

---

### Sub-prompt #33: Does the comparison table include HTMLHeaderTextSplitter as a row?
**Answer:** Yes

---

### Sub-prompt #34: Does the comparison table include MarkdownHeaderTextSplitter as a row?
**Answer:** Yes

---

## Cell Value Criteria (Selected Complex Cells)

### Sub-prompt #35: What is RecursiveCharacterTextSplitter's Recursion Type?
**Answer:** Direct Recursion

---

### Sub-prompt #36: What is RecursiveCharacterTextSplitter's Max Depth Formula?
**Answer:** L (separator count)

---

### Sub-prompt #37: What is RecursiveCharacterTextSplitter's Worst-Case Complexity?
**Answer:** O(n × L) where n=text length, L=separators

---

### Sub-prompt #38: What is RecursiveJsonSplitter's Recursion Type?
**Answer:** Indirect Recursion

---

### Sub-prompt #39: What is RecursiveJsonSplitter's Max Depth Formula?
**Answer:** D (JSON nesting depth)

---

### Sub-prompt #40: What is RecursiveJsonSplitter's Worst-Case Complexity?
**Answer:** O(n × D) where n=nodes, D=depth

---

### Sub-prompt #41: What is HTMLHeaderTextSplitter's Recursion Type?
**Answer:** Stack-Based Iteration

---

### Sub-prompt #42: What is HTMLHeaderTextSplitter's Max Depth Formula?
**Answer:** H (DOM tree height)

---

### Sub-prompt #43: What is HTMLHeaderTextSplitter's Worst-Case Complexity?
**Answer:** O(n) where n=DOM nodes

---

### Sub-prompt #44: What is MarkdownHeaderTextSplitter's Recursion Type?
**Answer:** None (Linear Scan)

---

### Sub-prompt #45: What is MarkdownHeaderTextSplitter's Max Depth Formula?
**Answer:** 1 (single pass)

---

## Summary

**Total Table Criteria:** 23 (C23-C45)

**Breakdown:**
- **Table structure (3 criteria):** #23-25
  - Table format exists (#23)
  - Correct column count: 5 (#24)
  - Correct row count: 4 (#25)
- **Column headers (5 criteria):** #26-30
  - Algorithm (#26)
  - Recursion Type (#27)
  - Max Depth Formula (#28)
  - Primary Data Structure (#29)
  - Worst-Case Complexity (#30)
- **Row entries (4 criteria):** #31-34
  - RecursiveCharacterTextSplitter (#31)
  - RecursiveJsonSplitter (#32)
  - HTMLHeaderTextSplitter (#33)
  - MarkdownHeaderTextSplitter (#34)
- **Cell values (11 criteria):** #35-45
  - RecursiveCharacterTextSplitter: Recursion Type (#35), Max Depth Formula (#36), Worst-Case Complexity (#37)
  - RecursiveJsonSplitter: Recursion Type (#38), Max Depth Formula (#39), Worst-Case Complexity (#40)
  - HTMLHeaderTextSplitter: Recursion Type (#41), Max Depth Formula (#42), Worst-Case Complexity (#43)
  - MarkdownHeaderTextSplitter: Recursion Type (#44), Max Depth Formula (#45)

**Note:** These 23 table criteria (C23-C45) are evaluated separately from the 22 analytical sub-prompts (C1-C22). Together they total 45 criteria.

**Cell Evaluation Strategy:** We evaluate 11 of the 20 total cell values, focusing on algorithmically complex cells (Recursion Type, Max Depth Formula, Worst-Case Complexity) while omitting straightforward cells (Algorithm names and Primary Data Structure) to stay within the 45 criteria limit.
