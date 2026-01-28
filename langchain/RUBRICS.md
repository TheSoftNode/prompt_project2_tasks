# RUBRICS

## Accuracy Criteria (Sub-Prompts)

### C1: Default Chunk Size [Accuracy]
**Description:** Response correctly states the default chunk_size in TextSplitter is 4000.
**Rationale:** The base.py source code shows `chunk_size: int = 4000` in the TextSplitter.__init__ method signature, establishing this as the default value.
**Source Quote:** `chunk_size: int = 4000` (base.py, line ~50)

### C2: Default Chunk Overlap [Accuracy]
**Description:** Response correctly states the default chunk_overlap in TextSplitter is 200.
**Rationale:** The base.py source code shows `chunk_overlap: int = 200` in the TextSplitter.__init__ method signature.
**Source Quote:** `chunk_overlap: int = 200` (base.py, line ~51)

### C3: Character TextSplitter Default Separator [Accuracy]
**Description:** Response correctly identifies "\n\n" as the default separator for CharacterTextSplitter.
**Rationale:** The character.py source code shows `separator: str = "\n\n"` in CharacterTextSplitter.__init__.
**Source Quote:** `separator: str = "\n\n"` (character.py, line ~19)

### C4: Number of Default Separators [Accuracy]
**Description:** Response correctly states RecursiveCharacterTextSplitter uses 4 default separators.
**Rationale:** The character.py source code assigns `self._separators = separators or ["\n\n", "\n", " ", ""]` which contains 4 elements.
**Source Quote:** `self._separators = separators or ["\n\n", "\n", " ", ""]` (character.py, line ~90)

### C5: Default Separators List [Accuracy]
**Description:** Response correctly lists the default separators as "\n\n", "\n", space, and empty string.
**Rationale:** The character.py source code explicitly defines this list in RecursiveCharacterTextSplitter initialization.
**Source Quote:** `self._separators = separators or ["\n\n", "\n", " ", ""]` (character.py, line ~90)

### C6: Time Complexity [Accuracy]
**Description:** Response correctly identifies O(n) as the time complexity for splitting a document of length n.
**Rationale:** The splitting algorithms iterate through the document linearly, performing constant-time operations per character, resulting in linear time complexity.
**Source Quote:** The split_text methods process each character once in the worst case (base.py, character.py implementation analysis).

### C7: Good Splits Data Structure [Accuracy]
**Description:** Response correctly identifies "list" as the data structure storing good splits during recursive splitting.
**Rationale:** The RecursiveCharacterTextSplitter implementation uses a Python list to accumulate splits that are smaller than chunk_size.
**Source Quote:** Variable `good_splits` is implemented as a Python list in the splitting logic (character.py).

### C8: Default Keep Separator Value [Accuracy]
**Description:** Response correctly states that RecursiveCharacterTextSplitter has keep_separator=True by default.
**Rationale:** The character.py source code shows `keep_separator: bool | Literal["start", "end"] = True` in RecursiveCharacterTextSplitter.__init__.
**Source Quote:** `keep_separator: bool | Literal["start", "end"] = True` (character.py, line ~87)

### C9: Default Length Function [Accuracy]
**Description:** Response correctly identifies "len" as the default function for measuring chunk length.
**Rationale:** The base.py source code shows `length_function: Callable[[str], int] = len` in TextSplitter.__init__.
**Source Quote:** `length_function: Callable[[str], int] = len` (base.py, line ~52)

### C10: Chunk Overlap Validation [Accuracy]
**Description:** Response correctly states that a ValueError is raised when chunk_overlap exceeds chunk_size.
**Rationale:** The base.py source code includes validation logic that checks this constraint and raises ValueError if violated.
**Source Quote:** Validation logic in TextSplitter.__init__ enforces `chunk_overlap < chunk_size` (base.py).

### C11: Good Splits Variable Name [Accuracy]
**Description:** Response correctly identifies "good_splits" as the variable name for accumulated splits smaller than chunk_size.
**Rationale:** The RecursiveCharacterTextSplitter implementation uses this specific variable name in its splitting logic.
**Source Quote:** Variable `good_splits` in splitting implementation (character.py).

### C12: Space Complexity [Accuracy]
**Description:** Response correctly identifies O(n) as the space complexity for storing splits of document length n.
**Rationale:** All resulting chunks must be stored in memory, and in the worst case, the total size equals the original document size plus overlap regions.
**Source Quote:** Implementation stores all chunks in memory (base.py, character.py analysis).

### C13: Required Method [Accuracy]
**Description:** Response correctly identifies "split_text" as the method all text splitters must implement.
**Rationale:** The base.py source code defines TextSplitter as an abstract base class with split_text as the required abstract method.
**Source Quote:** `@abstractmethod def split_text(self, text: str) -> list[str]:` (base.py).

## Quality Criteria

### C14: Algorithm Classification [Quality]
**Description:** Response accurately classifies text splitting algorithms by their strategic approach (separator-based, recursive, structure-aware).
**Rationale:** Proper taxonomy is essential for understanding the algorithmic landscape. CharacterTextSplitter is separator-based, RecursiveCharacterTextSplitter is recursive hierarchical, and MarkdownHeaderTextSplitter is structure-aware.
**Source Quote:** Implementation patterns across base.py, character.py, and markdown.py demonstrate these distinct approaches.

### C15: Hierarchical Separator Strategy Explanation [Quality]
**Description:** Response clearly explains how RecursiveCharacterTextSplitter tries separators in priority order with fallback behavior.
**Rationale:** Understanding the hierarchical fallback mechanism ("\n\n" → "\n" → " " → "") is crucial for predicting algorithm behavior.
**Source Quote:** `self._separators = separators or ["\n\n", "\n", " ", ""]` (character.py, line ~90).

### C16: Context Preservation Mechanisms [Quality]
**Description:** Response distinguishes between different context preservation strategies: fixed overlap, hierarchical boundaries, and structural metadata.
**Rationale:** Context preservation is a key differentiator between algorithms and critical for downstream LLM performance.
**Source Quote:** `chunk_overlap: int = 200` (base.py), hierarchical splitting logic (character.py), header metadata (markdown.py).

### C17: Document Type Matching [Quality]
**Description:** Response provides specific document types best suited to each algorithm with technical justification based on implementation characteristics.
**Rationale:** Practical application requires matching algorithm characteristics to document structure. Algorithm design patterns indicate which document formats work best.
**Source Quote:** Implementation characteristics from character.py and markdown.py reveal format-specific optimizations (e.g., hierarchical separators for code, header parsing for markdown).

### C18: Trade-off Analysis [Quality]
**Description:** Response analyzes trade-offs between simplicity, adaptability, and semantic coherence across algorithms.
**Rationale:** Algorithm selection requires understanding competing objectives and constraints.
**Source Quote:** Design patterns across base.py, character.py, and markdown.py reveal different optimization priorities.

### C19: Computational Complexity Justification [Quality]
**Description:** Response explains why algorithms achieve O(n) time complexity with reference to implementation details.
**Rationale:** Complexity analysis requires understanding how algorithms process input and what operations dominate runtime.
**Source Quote:** Single-pass processing patterns in split_text implementations (character.py).

### C20: Separator Handling Nuances [Quality]
**Description:** Response explains keep_separator parameter and its impact on output formatting.
**Rationale:** Separator handling affects semantic boundaries and chunk formatting, critical for downstream processing.
**Source Quote:** `keep_separator: bool | Literal["start", "end"] = False` (base.py), `keep_separator: bool | Literal["start", "end"] = True` (character.py).

### C21: Implementation Inheritance [Quality]
**Description:** Response recognizes the abstract base class pattern and how specific splitters inherit from TextSplitter.
**Rationale:** The inheritance hierarchy establishes common interfaces and shared functionality.
**Source Quote:** `class CharacterTextSplitter(TextSplitter):` (character.py), `class TextSplitter(BaseDocumentTransformer, ABC):` (base.py).

### C22: Merge Strategy [Quality]
**Description:** Response explains how small splits are merged to maximize chunk utilization while respecting size constraints.
**Rationale:** Efficient chunk packing improves retrieval effectiveness by avoiding unnecessarily small chunks.
**Source Quote:** Merging logic in split_text implementations (character.py).

### C23: Markdown Structure Awareness [Quality]
**Description:** Response describes how MarkdownHeaderTextSplitter preserves hierarchical document structure through header metadata.
**Rationale:** Structure-aware splitting enables more intelligent retrieval using document organization signals.
**Source Quote:** Implementation in markdown.py parsing header hierarchies.

### C24: Production Suitability [Quality]
**Description:** Response evaluates which algorithms are suitable for production systems processing large document corpora.
**Rationale:** Linear time complexity and predictable memory usage are essential for production deployment.
**Source Quote:** O(n) complexity and implementation patterns in base.py and character.py.

## Image Criteria

### C25: Table Structure Completeness [Image]
**Description:** Comparison table includes all 5 required columns: Algorithm Type, Time Complexity, Context Preservation, Document Types Best Suited, Separator Handling.
**Rationale:** The prompt explicitly requests these five dimensions for comparing text chunking approaches.
**Source Quote:** "Create a comparison table showing the following for each approach: Algorithm type and strategy, Time complexity for document of length n, Context preservation method, Document types best suited for the approach, Separator handling approach" (PROMPT.md).

### C26: Algorithm Coverage [Image]
**Description:** Table includes at least 3 distinct text splitting algorithms (CharacterTextSplitter, RecursiveCharacterTextSplitter, and one additional algorithm).
**Rationale:** The prompt requests comparison of multiple approaches, requiring sufficient coverage for meaningful analysis.
**Source Quote:** "Compare the algorithmic approaches used for splitting long documents" (PROMPT.md).

### C27: Time Complexity Accuracy [Image]
**Description:** Table correctly displays O(n) time complexity for character-based algorithms.
**Rationale:** Accurate complexity notation is fundamental to algorithmic analysis.
**Source Quote:** Linear processing in split_text implementations (character.py).

### C28: Context Preservation Details [Image]
**Description:** Table accurately describes context preservation mechanisms (fixed overlap values, hierarchical boundaries, or structural metadata).
**Rationale:** Context preservation is a key differentiator and must be accurately represented.
**Source Quote:** `chunk_overlap: int = 200` (base.py), hierarchical separator logic (character.py), header metadata (markdown.py).

### C29: Separator Handling Descriptions [Image]
**Description:** Table accurately describes separator handling approaches (single separator, hierarchical fallback, header-based structure).
**Rationale:** Separator handling fundamentally defines algorithm behavior and must be clearly communicated.
**Source Quote:** `separator: str = "\n\n"` (character.py), `self._separators = separators or ["\n\n", "\n", " ", ""]` (character.py).

### C30: Document Type Specificity [Image]
**Description:** Table provides specific document types best suited for each algorithm with technical grounding rather than vague categories.
**Rationale:** Actionable guidance requires concrete document type recommendations based on implementation characteristics.
**Source Quote:** Algorithm design patterns in character.py and markdown.py reveal format-specific optimizations (hierarchical separators suit code files, header parsing suits structured docs).

### C31: Visual Clarity [Image]
**Description:** Table uses clear formatting with distinct rows and columns, readable fonts, and appropriate sizing.
**Rationale:** Visual presentation must support comprehension and comparison across dimensions.
**Source Quote:** "A comparison table with 5 columns comparing at least 3 different text splitting algorithms" (PROMPT.md).

### C32: Label Consistency [Image]
**Description:** Column headers and row labels use consistent terminology matching the prompt and technical accuracy.
**Rationale:** Consistent terminology prevents confusion and maintains alignment with the research question.
**Source Quote:** Prompt specifies exact column names (PROMPT.md).

### C33: Algorithm Name Accuracy [Image]
**Description:** Table uses correct algorithm names matching the LangChain implementation (CharacterTextSplitter, RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter).
**Rationale:** Accurate naming enables readers to locate implementations and verify claims.
**Source Quote:** Class definitions in character.py and markdown.py.

### C34: Comparison Axis Alignment [Image]
**Description:** Table entries enable meaningful horizontal comparison across the same dimension for different algorithms.
**Rationale:** The table's analytical value depends on facilitating direct comparison.
**Source Quote:** "Create a comparison table showing the following for each approach" implies comparative structure (PROMPT.md).
