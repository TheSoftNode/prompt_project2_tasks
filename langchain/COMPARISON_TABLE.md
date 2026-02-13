# Text Splitter Complexity Comparison Table

| Algorithm | Recursion Type | Max Depth Formula | Primary Data Structure | Worst-Case Complexity |
|:----------|:---------------|:------------------|:-----------------------|:----------------------|
| RecursiveCharacterTextSplitter | Direct Recursion | L (separator count) | List (good_splits, final_chunks) | O(n × L) where n=text length, L=separators |
| RecursiveJsonSplitter | Indirect Recursion | D (JSON nesting depth) | Dictionary (nested structure) | O(n × D) where n=nodes, D=depth |
| HTMLHeaderTextSplitter | Stack-Based Iteration | H (DOM tree height) | Stack (explicit for DFS) | O(n) where n=DOM nodes |
| MarkdownHeaderTextSplitter | None (Linear Scan) | 1 (single pass) | List (lines_with_metadata) | O(n × h) where n=lines, h=headers |

---

## Table Details

### Column Descriptions

- **Algorithm**: The class name of each text splitter implementation being compared
- **Recursion Type**: The algorithmic approach used for traversal/splitting
  - Direct Recursion: Method calls itself with reduced problem size
  - Indirect Recursion: Recursion through shared state mutation
  - Stack-Based Iteration: Explicit stack data structure instead of call stack
  - None (Linear Scan): Single-pass iteration without recursion or stack
- **Max Depth Formula**: Mathematical expression for maximum recursion/iteration depth
  - L: Number of separators in the separator list
  - D: JSON object nesting depth
  - H: DOM tree height (longest path from root to leaf)
  - 1: Constant depth (single pass)
- **Primary Data Structure**: Main data structure used for accumulation/traversal
- **Worst-Case Complexity**: Big-O notation expressing worst-case time complexity with variable definitions

### Row Descriptions

**RecursiveCharacterTextSplitter**: Implements hierarchical text splitting using recursive fallback through separator list. Each recursion level tries one separator, recursing with remaining separators if chunks are too large. Maximum depth equals separator list length.

**RecursiveJsonSplitter**: Implements JSON structure decomposition through indirect recursion. Mutates shared chunks list while recursing through nested dictionary values. Maximum depth equals JSON nesting depth.

**HTMLHeaderTextSplitter**: Implements DOM traversal using explicit stack-based iteration instead of recursion. Performs depth-first search with stack management for header-based document segmentation. Maximum depth equals DOM tree height.

**MarkdownHeaderTextSplitter**: Implements single-pass linear scanning without recursion or stack. Processes document line-by-line maintaining header state. Constant depth (single iteration) but complexity grows with header count.

### Complexity Analysis

All implementations exhibit polynomial or linear time complexity:
- **RecursiveCharacterTextSplitter**: O(n × L) - linear in text length, multiplied by separator count
- **RecursiveJsonSplitter**: O(n × D) - linear in node count, multiplied by nesting depth
- **HTMLHeaderTextSplitter**: O(n) - pure linear time in DOM node count
- **MarkdownHeaderTextSplitter**: O(n × h) - linear in line count, multiplied by header count
