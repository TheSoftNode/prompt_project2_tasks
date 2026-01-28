# SCAFFOLD

## Sub-Prompt Answers Summary

1. Default chunk size: 4000
2. Default chunk overlap: 200
3. Default separator for Character TextSplitter: \n\n
4. Number of default separators in RecursiveCharacterTextSplitter: 4
5. Default separators: \n\n, \n, space, empty
6. Time complexity: O(n)
7. Data structure for good splits: list
8. Default keep_separator value: True
9. Default length function: len
10. Behavior when chunk_overlap exceeds chunk_size: ValueError raised
11. Minimum valid chunk_size: 1
12. Regex module used: re
13. Variable name for accumulated splits: good_splits
14. Space complexity: O(n)
15. Required method for all text splitters: split_text

## Comparison Table Summary

The task requires a comparison table with 5 columns comparing text chunking algorithms:

**Columns:**
- Algorithm type and strategy
- Time complexity for document of length n
- Context preservation method
- Optimal document type
- Separator handling approach

**Rows (Algorithms):**
- CharacterTextSplitter: Basic separator-based, O(n), fixed overlap, formatted prose, single separator
- RecursiveCharacterTextSplitter: Hierarchical splitting, O(n), overlap + boundaries, mixed formats, hierarchical fallback
- MarkdownHeaderTextSplitter: Structure-aware, O(n) + parsing, structural metadata, technical docs, header-based

**Key Insights:**
- All algorithms have linear time complexity O(n)
- Context preservation varies from simple overlap to structural metadata
- Different algorithms optimize for different document types
- Separator handling ranges from single pattern to hierarchical fallback strategies
