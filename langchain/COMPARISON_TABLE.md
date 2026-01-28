# Text Chunking Algorithm Comparison

| Algorithm | Time Complexity | Context Preservation | Document Types Best Suited | Separator Handling |
|-----------|----------------|---------------------|---------------------------|-------------------|
| **CharacterTextSplitter** | O(n) | Fixed overlap (200 chars) | Formatted prose, academic papers, technical documentation | Single separator (`\n\n`) |
| **RecursiveCharacterTextSplitter** | O(n) | Overlap + hierarchical boundaries | Code files, mixed-format documents, unstructured text | Hierarchical fallback (`\n\n` → `\n` → ` ` → `""`) |
| **MarkdownHeaderTextSplitter** | O(n) + parsing | Structural metadata (header hierarchy) | Technical docs, APIs, structured knowledge bases | Header-based structure preservation |

---

## Notes

- **n** represents document length in characters
- All algorithms achieve linear time complexity for the splitting phase
- Context preservation strategies range from simple character overlap to hierarchical structural metadata
- Separator handling approaches vary from single-pattern matching to adaptive hierarchical fallback
- Algorithm selection should prioritize document characteristics over complexity considerations
