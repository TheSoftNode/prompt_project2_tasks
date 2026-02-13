# CRITERIA BREAKDOWN - LangChain Text Splitters

**Target:** Maximum 45 criteria total

---

## Question 1: Language Separator Anomalies (9 criteria)

**Sub-criteria:**
- C1: First anomalous language name
- C2: First anomalous language anomaly type (duplicate/missing)
- C3: First anomalous language separator count
- C4: Second anomalous language name
- C5: Second anomalous language anomaly type
- C6: Second anomalous language separator count
- C7: Third anomalous language name
- C8: Third anomalous language anomaly type
- C9: Third anomalous language separator count

**Criteria Count: 9**

---

## Question 2: _merge_splits Loop Analysis (3 criteria)

**Sub-criteria:**
- C10: Outer for-loop iteration count
- C11: Total while-loop iteration count
- C12: Final docs list element count

**Criteria Count: 3**

---

## Question 3: JSFrameworkTextSplitter Separator Count (1 criterion)

**Sub-criteria:**
- C13: Total separator count for input with 7 unique tags

**Criteria Count: 1**

---

## Question 4: Inheritance Depth Sum (1 criterion)

**Sub-criteria:**
- C14: Sum of inheritance depths for PythonCodeTextSplitter + HTMLSemanticPreservingSplitter + RecursiveJsonSplitter

**Criteria Count: 1**

---

## Question 5: Recursion Depth Sum (1 criterion)

**Sub-criteria:**
- C15: Sum of max recursion depths for _split_text (L=15) + _json_split (D=8)

**Criteria Count: 1**

---

## Question 6: Parameter Override Count (1 criterion)

**Sub-criteria:**
- C16: Total parameter override instances across 4 specified classes

**Criteria Count: 1**

---

## Question 7: Data Structure Mutation Counts (4 criteria)

**Sub-criteria:**
- C17: clear() count
- C18: pop() count
- C19: extend() count
- C20: del count

**Criteria Count: 4**

---

## Question 8: State Variable Lifecycle Product (1 criterion)

**Sub-criteria:**
- C21: Product of (before) × (inside) × (after)

**Criteria Count: 1**

---

## Question 9: Separator Character Ratio (1 criterion)

**Sub-criteria:**
- C22: HTML:PYTHON character count ratio in simplest form

**Criteria Count: 1**

---

## Question 10: Complexity Comparison Table (23 criteria)

### Table Structure Criteria (3 criteria)
- C23: Outputs comparison in table format
- C24: Table has exactly 5 columns
- C25: Table has exactly 4 data rows (excluding header)

### Column Header Criteria (5 criteria)
- C26: Column header "Algorithm"
- C27: Column header "Recursion Type"
- C28: Column header "Max Depth Formula"
- C29: Column header "Primary Data Structure"
- C30: Column header "Worst-Case Complexity"

### Row Entry Criteria (4 criteria)
- C31: Row for RecursiveCharacterTextSplitter
- C32: Row for RecursiveJsonSplitter
- C33: Row for HTMLHeaderTextSplitter
- C34: Row for MarkdownHeaderTextSplitter

### Cell Value Criteria (11 criteria - selected complex cells only)
- C35: RecursiveCharacterTextSplitter - Recursion Type value
- C36: RecursiveCharacterTextSplitter - Max Depth Formula value
- C37: RecursiveCharacterTextSplitter - Worst-Case Complexity value

- C38: RecursiveJsonSplitter - Recursion Type value
- C39: RecursiveJsonSplitter - Max Depth Formula value
- C40: RecursiveJsonSplitter - Worst-Case Complexity value

- C41: HTMLHeaderTextSplitter - Recursion Type value
- C42: HTMLHeaderTextSplitter - Max Depth Formula value
- C43: HTMLHeaderTextSplitter - Worst-Case Complexity value

- C44: MarkdownHeaderTextSplitter - Recursion Type value
- C45: MarkdownHeaderTextSplitter - Max Depth Formula value

**Criteria Count: 23** (3 structure + 5 headers + 4 rows + 11 key cell values)

**Note:** We evaluate 11 of the 20 total cell values (focusing on algorithmically complex cells: Recursion Type, Max Depth Formula, Worst-Case Complexity) to stay within 45 criteria limit. Algorithm names and Primary Data Structure are too straightforward to warrant separate criteria.

---

## TOTAL CRITERIA SUMMARY

| Question | Type | Criteria Count | Running Total |
|----------|------|----------------|---------------|
| Q1 | Analytical | 9 | 9 |
| Q2 | Analytical | 3 | 12 |
| Q3 | Analytical | 1 | 13 |
| Q4 | Analytical | 1 | 14 |
| Q5 | Analytical | 1 | 15 |
| Q6 | Analytical | 1 | 16 |
| Q7 | Analytical | 4 | 20 |
| Q8 | Analytical | 1 | 21 |
| Q9 | Analytical | 1 | 22 |
| Q10 (Structure) | Table | 3 | 25 |
| Q10 (Headers) | Table | 5 | 30 |
| Q10 (Rows) | Table | 4 | 34 |
| Q10 (Cells) | Table | 11 | **45** |

**TOTAL: 45 CRITERIA** ✅ (Exactly at limit!)

**Analytical Questions:** 9 (Q1-Q9) = 22 criteria
**Table Question:** 1 (Q10) = 23 criteria
**Grand Total:** 45 criteria

---

## Notes

- All questions have exact, verifiable answers
- No open-ended questions
- All require deep algorithmic analysis
- Questions require reading 5+ files
- Complexity designed for 70% failure rate
- **Exactly 45 criteria used (perfect fit!)**
