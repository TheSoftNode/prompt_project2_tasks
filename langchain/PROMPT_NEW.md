# PROMPT

**Subdomain:** Algorithmic Analysis

**Routing:** Scratch

---

## Main Prompt

The langchain-ai/langchain repository implements multiple text splitting algorithms in its text-splitters library as of January 28, 2026. Three primary implementations use different strategies: CharacterTextSplitter applies separators directly, RecursiveCharacterTextSplitter tries separators hierarchically with fallback logic, and MarkdownHeaderTextSplitter parses document structure. Multiple specialized splitters extend these base implementations, applying domain-specific separator patterns while reusing core logic. Understanding which implementation patterns dominate the library architecture requires comparing separator strategies, analyzing inheritance hierarchies, and categorizing context preservation mechanisms across all implementations.

Examine CharacterTextSplitter, RecursiveCharacterTextSplitter, and MarkdownHeaderTextSplitter alongside their specialized subclasses. Determine architectural patterns by comparing separator handling approaches, inheritance relationships, and complexity characteristics:

1. Analyze how RecursiveCharacterTextSplitter's _split_text method handles separator iteration compared to CharacterTextSplitter's split_text method. Examine the default separator configuration in each implementation and identify whether they use single or multiple separators. Determine the difference between the maximum number of separators evaluated during a split operation in the hierarchical implementation versus the simple implementation.

2. Examine TextSplitter's __init__ method to identify the default parameter values for chunk_size and chunk_overlap. Analyze how these values control memory consumption when overlap creates content duplication across adjacent chunks. Calculate the ratio between the default chunk_size and default chunk_overlap to quantify the designed duplication factor.

3. Survey the text-splitters library across character.py, markdown.py, python.py, latex.py, jsx.py, and html.py to identify all specialized splitter implementations. For each specialized class, determine which base class it inherits from. Categorize the inheritance patterns to reveal which base strategy the library architecture favors for extensibility. Count how many specialized splitter classes inherit from RecursiveCharacterTextSplitter.

4. Examine TextSplitter's class definition to identify its parent classes and determine why multiple inheritance is used. Scan for @abstractmethod decorators to identify which methods subclasses must implement. Sum the architectural obligations by combining the count of parent classes TextSplitter inherits from plus the count of abstract methods it enforces.

5. Analyze the context preservation mechanisms across CharacterTextSplitter, RecursiveCharacterTextSplitter, and MarkdownHeaderTextSplitter. Identify whether each implementation uses chunk_overlap for text duplication or Document.metadata for structural information injection. Categorize these as overlap-based or metadata-based strategies. Express the distribution as a ratio comparing separator-based splitters to metadata-based splitters.

6. Compare the parameter configurations between CharacterTextSplitter and RecursiveCharacterTextSplitter. Examine the default values for chunk_size, chunk_overlap, keep_separator, strip_whitespace, and add_start_index in both implementations. Identify which parameters have matching defaults and which differ. Count the parameters with mismatched default values.

7. Examine RecursiveCharacterTextSplitter's _split_text method implementation to identify all list variables created for accumulating results during chunk processing. Trace through the method to distinguish between intermediate accumulation structures and final output storage. Count the distinct list variables used for chunk accumulation before returning results.

8. Analyze the loop structures and iteration patterns in CharacterTextSplitter.split_text, RecursiveCharacterTextSplitter._split_text, and MarkdownHeaderTextSplitter.split_text. For each implementation, determine whether every character is processed a constant or variable number of times. Identify which implementations achieve O(n) time complexity for documents of length n. Count the implementations that maintain linear time bounds.

9. Create a comparison table showing five architectural dimensions for each of the three main splitters: algorithm name, time complexity for documents of length n, context preservation mechanism, base class inherited from, and number of default separators. Label columns as: "Algorithm", "Time Complexity", "Context Preservation", "Inherits From", "Separators".

---

## Expected Image

A comparison table with 5 columns and 3 rows comparing CharacterTextSplitter, RecursiveCharacterTextSplitter, and MarkdownHeaderTextSplitter across the specified architectural dimensions.
