# CRITERIA TO PROMPT QUESTION MAPPING

This document maps each criterion (1-33) to the exact prompt question it answers or handles.

---

## Question 1: Separator Analysis
**Prompt Question:** Analyze how RecursiveCharacterTextSplitter's _split_text method handles separator iteration compared to CharacterTextSplitter's split_text method. Examine the default separator configuration in each implementation and identify whether they use single or multiple separators. Determine the difference between the maximum number of separators evaluated during a split operation in the hierarchical implementation versus the simple implementation.

**Criteria:**
- **C1:** How many default separators does RecursiveCharacterTextSplitter evaluate?
- **C2:** How many default separators does CharacterTextSplitter evaluate?
- **C3:** What is the difference between the number of separators in RecursiveCharacterTextSplitter and CharacterTextSplitter?

---

## Question 2: Parameter Ratio
**Prompt Question:** Examine TextSplitter's __init__ method to identify the default parameter values for chunk_size and chunk_overlap. Analyze how these values control memory consumption when overlap creates content duplication across adjacent chunks. Calculate the ratio between the default chunk_size and default chunk_overlap to quantify the designed duplication factor.

**Criteria:**
- **C4:** What is the default chunk_size value in TextSplitter?
- **C5:** What is the default chunk_overlap value in TextSplitter?
- **C6:** What is the ratio of default chunk_size to default chunk_overlap?

---

## Question 3: Inheritance Count
**Prompt Question:** Survey the text-splitters library across character.py, markdown.py, python.py, latex.py, jsx.py, and html.py to identify all specialized splitter implementations. For each specialized class, determine which base class it inherits from. Categorize the inheritance patterns to reveal which base strategy the library architecture favors for extensibility. Count how many specialized splitter classes inherit from RecursiveCharacterTextSplitter.

**Criteria:**
- **C7:** How many specialized splitter classes inherit from RecursiveCharacterTextSplitter?

---

## Question 4: Architectural Obligations
**Prompt Question:** Examine TextSplitter's class definition to identify its parent classes and determine why multiple inheritance is used. Scan for @abstractmethod decorators to identify which methods subclasses must implement. Sum the architectural obligations by combining the count of parent classes TextSplitter inherits from plus the count of abstract methods it enforces.

**Criteria:**
- **C8:** How many parent classes does TextSplitter inherit from?
- **C9:** How many abstract methods does TextSplitter define?
- **C10:** What is the sum of parent classes and abstract methods for TextSplitter?

---

## Question 5: Context Preservation Ratio
**Prompt Question:** Analyze the context preservation mechanisms across CharacterTextSplitter, RecursiveCharacterTextSplitter, and MarkdownHeaderTextSplitter. Identify whether each implementation uses chunk_overlap for text duplication or Document.metadata for structural information injection. Categorize these as overlap-based or metadata-based strategies. Express the distribution as a ratio comparing separator-based splitters to metadata-based splitters.

**Criteria:**
- **C11:** How many of the three main splitters use separator-based overlap for context preservation?
- **C12:** How many of the three main splitters use metadata-based context preservation?
- **C13:** What is the ratio of separator-based splitters to metadata-based splitters?

---

## Question 6: Parameter Comparison
**Prompt Question:** Compare the parameter configurations between CharacterTextSplitter and RecursiveCharacterTextSplitter. Examine the default values for chunk_size, chunk_overlap, keep_separator, strip_whitespace, and add_start_index in both implementations. Identify which parameters have matching defaults and which differ. Count the parameters with mismatched default values.

**Criteria:**
- **C14:** Does chunk_size have different default values between CharacterTextSplitter and RecursiveCharacterTextSplitter?
- **C15:** Does chunk_overlap have different default values between CharacterTextSplitter and RecursiveCharacterTextSplitter?
- **C16:** Does keep_separator have different default values between CharacterTextSplitter and RecursiveCharacterTextSplitter?
- **C17:** Does strip_whitespace have different default values between CharacterTextSplitter and RecursiveCharacterTextSplitter?
- **C18:** Does add_start_index have different default values between CharacterTextSplitter and RecursiveCharacterTextSplitter?
- **C19:** How many parameters have different default values between CharacterTextSplitter and RecursiveCharacterTextSplitter?

---

## Question 7: List Variables
**Prompt Question:** Examine RecursiveCharacterTextSplitter's _split_text method implementation to identify all list variables created for accumulating results during chunk processing. Trace through the method to distinguish between intermediate accumulation structures and final output storage. Count the distinct list variables used for chunk accumulation before returning results.

**Criteria:**
- **C20:** How many distinct list variables does RecursiveCharacterTextSplitter's _split_text method use for chunk accumulation?

---

## Question 8: Time Complexity
**Prompt Question:** Analyze the loop structures and iteration patterns in CharacterTextSplitter.split_text, RecursiveCharacterTextSplitter._split_text, and MarkdownHeaderTextSplitter.split_text. For each implementation, determine whether every character is processed a constant or variable number of times. Identify which implementations achieve O(n) time complexity for documents of length n. Count the implementations that maintain linear time bounds.

**Criteria:**
- **C21:** Does CharacterTextSplitter achieve O(n) time complexity?
- **C22:** Does RecursiveCharacterTextSplitter achieve O(n) time complexity?
- **C23:** Does MarkdownHeaderTextSplitter achieve O(n) time complexity?
- **C24:** How many of the three main splitters achieve O(n) time complexity?

---

## Question 9: Adapter Functions
**Prompt Question:** Examine the import statements across the text-splitters library to identify async/sync adapter functions from asgiref.sync. Analyze how these adapters are used in ensure_sync methods to bridge execution contexts. Distinguish between adapter types based on their wrapping direction. Count the distinct adapter function types imported by the library.

**Criteria:**
- **C25:** How many distinct adapter function types are imported from asgiref.sync?

---

## Question 10: Comparison Table
**Prompt Question:** Create a comparison table showing five architectural dimensions for each of the three main splitters: algorithm name, time complexity for documents of length n, context preservation mechanism, base class inherited from, and number of default separators. Label columns as: "Algorithm", "Time Complexity", "Context Preservation", "Inherits From", "Separators".

**Criteria:**
- **C26:** Outputs the comparison in a table format?
- **C27:** Formats the table with 5 columns?
- **C28:** Formats the table with 3 rows (excluding header)?
- **C29:** Does the comparison table include "Algorithm" as a column header?
- **C30:** Does the comparison table include "Time Complexity" as a column header?
- **C31:** Does the comparison table include "Context Preservation" as a column header?
- **C32:** Does the comparison table include "Inherits From" as a column header?
- **C33:** Does the comparison table include "Separators" as a column header?
- **C34:** Does the comparison table include CharacterTextSplitter as a row?
- **C35:** Does the comparison table include RecursiveCharacterTextSplitter as a row?
- **C36:** Does the comparison table include MarkdownHeaderTextSplitter as a row?

---

## Summary

**Total Criteria:** 36
- **Analytical Criteria (Q1-Q9):** 25 criteria
- **Table Criteria (Q10):** 11 criteria
  - Table structure: 3 criteria (C26-C28)
  - Column headers: 5 criteria (C29-C33)
  - Row entries: 3 criteria (C34-C36)

Each criterion corresponds to a specific component answer required by the prompt questions.
