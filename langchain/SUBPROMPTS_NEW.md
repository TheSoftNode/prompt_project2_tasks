# SUBPROMPTS - LangChain Text Splitters Analysis

---

## Sub-prompt #1: How many default separators does RecursiveCharacterTextSplitter evaluate?
**Answer:** 4

---

## Sub-prompt #2: How many default separators does CharacterTextSplitter evaluate?
**Answer:** 1

---

## Sub-prompt #3: What is the difference between the number of separators in RecursiveCharacterTextSplitter and CharacterTextSplitter?
**Answer:** 3

---

## Sub-prompt #4: What is the default chunk_size value in TextSplitter?
**Answer:** 4000

---

## Sub-prompt #5: What is the default chunk_overlap value in TextSplitter?
**Answer:** 200

---

## Sub-prompt #6: What is the ratio of default chunk_size to default chunk_overlap?
**Answer:** 20:1

---

## Sub-prompt #7: How many specialized splitter classes inherit from RecursiveCharacterTextSplitter?
**Answer:** 4

---

## Sub-prompt #8: How many parent classes does TextSplitter inherit from?
**Answer:** 2

---

## Sub-prompt #9: How many abstract methods does TextSplitter define?
**Answer:** 1

---

## Sub-prompt #10: What is the sum of parent classes and abstract methods for TextSplitter?
**Answer:** 3

---

## Sub-prompt #11: How many of the three main splitters use separator-based overlap for context preservation?
**Answer:** 2

---

## Sub-prompt #12: How many of the three main splitters use metadata-based context preservation?
**Answer:** 1

---

## Sub-prompt #13: What is the ratio of separator-based splitters to metadata-based splitters?
**Answer:** 2:1

---

## Sub-prompt #14: Does chunk_size have different default values between CharacterTextSplitter and RecursiveCharacterTextSplitter?
**Answer:** No (both inherit 4000 from TextSplitter)

---

## Sub-prompt #15: Does chunk_overlap have different default values between CharacterTextSplitter and RecursiveCharacterTextSplitter?
**Answer:** No (both inherit 200 from TextSplitter)

---

## Sub-prompt #16: Does keep_separator have different default values between CharacterTextSplitter and RecursiveCharacterTextSplitter?
**Answer:** Yes (False vs True)

---

## Sub-prompt #17: Does strip_whitespace have different default values between CharacterTextSplitter and RecursiveCharacterTextSplitter?
**Answer:** No (both inherit True from TextSplitter)

---

## Sub-prompt #18: Does add_start_index have different default values between CharacterTextSplitter and RecursiveCharacterTextSplitter?
**Answer:** No (both inherit False from TextSplitter)

---

## Sub-prompt #19: How many parameters have different default values between CharacterTextSplitter and RecursiveCharacterTextSplitter?
**Answer:** 1

---

## Sub-prompt #20: How many distinct list variables does RecursiveCharacterTextSplitter's _split_text method use for chunk accumulation?
**Answer:** 2

---

## Sub-prompt #21: Does CharacterTextSplitter achieve O(n) time complexity?
**Answer:** Yes

---

## Sub-prompt #22: Does RecursiveCharacterTextSplitter achieve O(n) time complexity?
**Answer:** Yes

---

## Sub-prompt #23: Does MarkdownHeaderTextSplitter achieve O(n) time complexity?
**Answer:** Yes

---

## Sub-prompt #24: How many of the three main splitters achieve O(n) time complexity?
**Answer:** 3

---

## Sub-prompt #25: How many distinct adapter function types are imported from asgiref.sync?
**Answer:** 2

---

## Summary

**Total Sub-prompts:** 25
**Breakdown:**
- Separator analysis (Q1): 3 sub-prompts (#1-3)
- Parameter ratio (Q2): 3 sub-prompts (#4-6)
- Inheritance count (Q3): 1 sub-prompt (#7)
- Architectural obligations (Q4): 3 sub-prompts (#8-10)
- Context preservation ratio (Q5): 3 sub-prompts (#11-13)
- Parameter comparison (Q6): 6 sub-prompts (#14-19)
- List variables (Q7): 1 sub-prompt (#20)
- Time complexity (Q8): 4 sub-prompts (#21-24)
- Adapter functions (Q9): 1 sub-prompt (#25)

**Note:** Table evaluation (Q10) is kept separate and will have its own criteria independent of these analytical sub-prompts.
