# CRITERIA TO PROMPT QUESTION MAPPING

This document maps each criterion (1-45) to the exact prompt question it answers or handles.

---

## Question 1: Language Separator Anomalies
**Prompt Question:** RecursiveCharacterTextSplitter's `get_separators_for_language` method defines separator lists for 26 language implementations. Among these, identify the THREE languages where separator lists contain either: (a) duplicate separator strings appearing multiple times, OR (b) the standard "\n\n" separator is completely absent. For each anomalous language, state: the language name, the type of anomaly (duplicate vs missing), and the exact separator count.

**Criteria:**
- **C1:** First anomalous language name
- **C2:** First anomalous language anomaly type (duplicate/missing)
- **C3:** First anomalous language separator count
- **C4:** Second anomalous language name
- **C5:** Second anomalous language anomaly type (duplicate/missing)
- **C6:** Second anomalous language separator count
- **C7:** Third anomalous language name
- **C8:** Third anomalous language anomaly type (duplicate/missing)
- **C9:** Third anomalous language separator count

---

## Question 2: _merge_splits Loop Analysis
**Prompt Question:** The `TextSplitter._merge_splits` method in base.py implements chunk merging using nested loop structures. Given inputs: `splits = ["a"*100, "b"*50, "c"*150, "d"*75]`, `separator = "--"` (length 2), `chunk_size = 200`, `chunk_overlap = 50`, calculate: (a) the exact number of outer for-loop iterations, (b) the exact total number of while-loop iterations across all for-loop iterations, (c) the number of elements in the final returned `docs` list.

**Criteria:**
- **C10:** Outer for-loop iteration count
- **C11:** Total while-loop iteration count
- **C12:** Final docs list element count

---

## Question 3: JSFrameworkTextSplitter Separator Count
**Prompt Question:** JSFrameworkTextSplitter's `split_text` method implements dynamic separator generation by extracting component tags from input text at runtime using the regex pattern `r"<\s*([a-zA-Z0-9]+)[^>]*>"`. The method concatenates four separator lists: dynamically extracted tags, 24 hardcoded JS separators, and additional fixed separators. For an input containing exactly 7 unique opening tags, calculate the total number of separators in the final concatenated list used for splitting.

**Criteria:**
- **C13:** Total separator count for input with 7 unique tags

---

## Question 4: Inheritance Depth Sum
**Prompt Question:** Inheritance depth analysis across the module reveals varying hierarchy complexity. Trace the complete inheritance chains for: (a) PythonCodeTextSplitter, (b) HTMLSemanticPreservingSplitter, (c) RecursiveJsonSplitter. For each, count the total levels from the class to the ultimate base (including BaseDocumentTransformer/ABC if present). Express the result as the sum of all three depth counts.

**Criteria:**
- **C14:** Sum of inheritance depths for PythonCodeTextSplitter + HTMLSemanticPreservingSplitter + RecursiveJsonSplitter

---

## Question 5: Recursion Depth Sum
**Prompt Question:** RecursiveCharacterTextSplitter's `_split_text` method and RecursiveJsonSplitter's `_json_split` method both implement recursive algorithms with different complexity characteristics. For the worst-case scenario: (a) a text with separator list length L=15 where each separator successfully splits into exactly 3 parts at each level - what is the maximum recursion depth for `_split_text`? (b) For a JSON object nested D=8 levels deep where each level contains exactly 1 key-value pair - what is the exact recursion depth for `_json_split`? Express as the sum of both depths.

**Criteria:**
- **C15:** Sum of max recursion depths for _split_text (L=15) + _json_split (D=8)

---

## Question 6: Parameter Override Count
**Prompt Question:** Multiple splitter classes override default parameter values from the TextSplitter base class. Compare the base class defaults (chunk_size=4000, chunk_overlap=200, keep_separator=False) against: RecursiveCharacterTextSplitter, JSFrameworkTextSplitter, SentenceTransformersTokenTextSplitter, and HTMLSemanticPreservingSplitter. Count the total number of parameter override instances across all four classes where a subclass specifies a different default value than the base class.

**Criteria:**
- **C16:** Total parameter override instances across 4 specified classes

---

## Question 7: Data Structure Mutation Counts
**Prompt Question:** HTMLHeaderTextSplitter's `_generate_documents` method implements stack-based DOM traversal instead of recursion. The algorithm uses specific data structure mutation operations: `clear()`, `pop()`, `extend()`, and `del` (dictionary deletion). Count the exact number of each mutation type that appears in the method's source code. Express as: (clear_count, pop_count, extend_count, del_count).

**Criteria:**
- **C17:** clear() count
- **C18:** pop() count
- **C19:** extend() count
- **C20:** del count

---

## Question 8: State Variable Lifecycle Product
**Prompt Question:** MarkdownHeaderTextSplitter's `split_text` method maintains seven state variables throughout execution: `lines_with_metadata`, `current_content`, `current_metadata`, `header_stack`, `initial_metadata`, `in_code_block`, and `opening_fence`. Analyze their lifecycle: (a) how many are initialized before the main loop, (b) how many are modified inside the loop, (c) how many are accessed after the loop completes. Express as the product: (before) × (inside) × (after).

**Criteria:**
- **C21:** Product of (before) × (inside) × (after)

---

## Question 9: Separator Character Ratio
**Prompt Question:** The separator character count reveals implementation complexity differences. Calculate the total number of characters (including spaces, excluding the empty string separator "") across all separator strings for: (a) Language.HTML's separator list, (b) Language.PYTHON's separator list. Express the result as the ratio HTML:PYTHON in simplest integer form.

**Criteria:**
- **C22:** HTML:PYTHON character count ratio in simplest form

---

## Question 10: Complexity Comparison Table
**Prompt Question:** Create a complexity comparison table with 5 columns and 4 rows. Compare RecursiveCharacterTextSplitter, RecursiveJsonSplitter, HTMLHeaderTextSplitter, and MarkdownHeaderTextSplitter. Columns: "Algorithm", "Recursion Type", "Max Depth Formula", "Primary Data Structure", "Worst-Case Complexity". For "Recursion Type" use: Direct Recursion, Indirect Recursion, Stack-Based Iteration, or None. For "Max Depth Formula" express in terms of relevant variables (e.g., "L" for separator count, "D" for JSON depth, "H" for DOM height). For "Worst-Case Complexity" use Big-O notation with clearly defined variables.

### Table Structure Criteria
**Criteria:**
- **C23:** Outputs comparison in table format
- **C24:** Table has exactly 5 columns
- **C25:** Table has exactly 4 data rows (excluding header)

### Column Header Criteria
**Criteria:**
- **C26:** Column header "Algorithm"
- **C27:** Column header "Recursion Type"
- **C28:** Column header "Max Depth Formula"
- **C29:** Column header "Primary Data Structure"
- **C30:** Column header "Worst-Case Complexity"

### Row Entry Criteria
**Criteria:**
- **C31:** Row for RecursiveCharacterTextSplitter
- **C32:** Row for RecursiveJsonSplitter
- **C33:** Row for HTMLHeaderTextSplitter
- **C34:** Row for MarkdownHeaderTextSplitter

### Cell Value Criteria (Selected Complex Cells)
**Criteria:**
- **C35:** RecursiveCharacterTextSplitter - Recursion Type value
- **C36:** RecursiveCharacterTextSplitter - Max Depth Formula value
- **C37:** RecursiveCharacterTextSplitter - Worst-Case Complexity value
- **C38:** RecursiveJsonSplitter - Recursion Type value
- **C39:** RecursiveJsonSplitter - Max Depth Formula value
- **C40:** RecursiveJsonSplitter - Worst-Case Complexity value
- **C41:** HTMLHeaderTextSplitter - Recursion Type value
- **C42:** HTMLHeaderTextSplitter - Max Depth Formula value
- **C43:** HTMLHeaderTextSplitter - Worst-Case Complexity value
- **C44:** MarkdownHeaderTextSplitter - Recursion Type value
- **C45:** MarkdownHeaderTextSplitter - Max Depth Formula value

**Note:** We evaluate 11 of the 20 total cell values (focusing on algorithmically complex cells: Recursion Type, Max Depth Formula, Worst-Case Complexity) to stay within 45 criteria limit. Algorithm names and Primary Data Structure cells are too straightforward to warrant separate criteria evaluation.

---

## Summary

**Total Criteria:** 45
- **Analytical Criteria (Q1-Q9):** 22 criteria
  - Q1: 9 criteria (C1-C9)
  - Q2: 3 criteria (C10-C12)
  - Q3: 1 criterion (C13)
  - Q4: 1 criterion (C14)
  - Q5: 1 criterion (C15)
  - Q6: 1 criterion (C16)
  - Q7: 4 criteria (C17-C20)
  - Q8: 1 criterion (C21)
  - Q9: 1 criterion (C22)
- **Table Criteria (Q10):** 23 criteria
  - Table structure: 3 criteria (C23-C25)
  - Column headers: 5 criteria (C26-C30)
  - Row entries: 4 criteria (C31-C34)
  - Cell values: 11 criteria (C35-C45)

Each criterion corresponds to a specific component answer required by the prompt questions. All questions focus on algorithmic analysis with exact, verifiable answers.
