# Text Splitter Comparison Table

| Algorithm | Time Complexity | Context Preservation | Inherits From | Separators |
|:----------|:---------------|:---------------------|:--------------|:-----------|
| CharacterTextSplitter | O(n) | chunk_overlap (text duplication) | TextSplitter | 1 |
| RecursiveCharacterTextSplitter | O(n) | chunk_overlap (text duplication) | TextSplitter | 4 |
| MarkdownHeaderTextSplitter | O(n) | Document.metadata (structural injection) | None (standalone) | Variable (header-based) |

---

## Table Details

- **Algorithm**: The class name of each text splitter implementation
- **Time Complexity**: All three achieve O(n) linear time for documents of length n
- **Context Preservation**: Two strategies - chunk_overlap (text duplication) vs Document.metadata (structural injection)
- **Inherits From**: CharacterTextSplitter and RecursiveCharacterTextSplitter inherit from TextSplitter; MarkdownHeaderTextSplitter is a standalone class with no parent
- **Separators**: Number of default separators - CharacterTextSplitter (1), RecursiveCharacterTextSplitter (4), MarkdownHeaderTextSplitter (variable based on headers)
