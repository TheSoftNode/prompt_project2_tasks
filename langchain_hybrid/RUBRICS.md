# RUBRICS - LangChain Text Splitters Analysis - 47 Criteria

## Overview
- **Total Criteria**: 47 (all positive)
- **Domain**: Algorithmic Analysis - Text Splitter Architecture
- **Repository**: langchain-ai/langchain (text-splitters library)
- **Commit**: 72571185a8f51e353a2fe9143855f310c4d31e08
- **Task Type**: Research & Analysis (Scratch Routing)

---

## CRITERION 1 [Accuracy]
**Description:** States 4 as the count of default separators that RecursiveCharacterTextSplitter evaluates.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source:
```python
def __init__(
    self,
    separators: list[str] | None = None,
    keep_separator: bool | Literal["start", "end"] = True,
    is_separator_regex: bool = False,
    **kwargs: Any,
) -> None:
    super().__init__(keep_separator=keep_separator, **kwargs)
    self._separators = separators or ["\n\n", "\n", " ", ""]
    self._is_separator_regex = is_separator_regex
```
The default separators list ["\n\n", "\n", " ", ""] contains exactly 4 elements, representing a hierarchical fallback strategy from paragraph boundaries (double newline) to line boundaries (single newline) to word boundaries (space) to character-level splitting (empty string).
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 2 [Accuracy]
**Description:** States 1 as the count of default separators that CharacterTextSplitter evaluates.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source:
```python
def __init__(
    self,
    separator: str = "\n\n",
    is_separator_regex: bool = False,
    **kwargs: Any,
) -> None:
```
CharacterTextSplitter uses a single separator parameter with default value "\n\n", meaning it evaluates only 1 separator (paragraph boundaries), unlike RecursiveCharacterTextSplitter's hierarchical approach.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 3 [Accuracy]
**Description:** States 3 as the difference between RecursiveCharacterTextSplitter's separator count and CharacterTextSplitter's separator count.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** The calculation is: RecursiveCharacterTextSplitter's 4 default separators (count of list elements) minus CharacterTextSplitter's 1 default separator equals 3. This difference quantifies the algorithmic sophistication gap. RecursiveCharacterTextSplitter provides 3 additional fallback levels beyond the simple single-separator approach, enabling adaptive splitting across paragraph, line, word, and character boundaries.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 4 [Accuracy]
**Description:** States 4000 as the default chunk_size value in TextSplitter.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source:
```python
def __init__(
    self,
    chunk_size: int = 4000,
    chunk_overlap: int = 200,
    length_function: Callable[[str], int] = len,
    keep_separator: bool | Literal["start", "end"] = False,
    add_start_index: bool = False,
    strip_whitespace: bool = True,
) -> None:
```
The default chunk_size=4000 establishes the maximum target size for text chunks, measured by the length_function (default: character count).
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py

## CRITERION 5 [Accuracy]
**Description:** States 200 as the default chunk_overlap value in TextSplitter.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source:
```python
def __init__(
    self,
    chunk_size: int = 4000,
    chunk_overlap: int = 200,
    ...
) -> None:
```
The default chunk_overlap=200 creates a rolling window effect where consecutive chunks share 200 units (typically characters) of content, preventing context loss at chunk boundaries.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py

## CRITERION 6 [Accuracy]
**Description:** States "20:1" as the ratio of default chunk_size to default chunk_overlap.
**Weight:** Major
**Numerical Weight:** 6
**Rationale:** The calculation is: chunk_size (4000) divided by chunk_overlap (200) equals 20, expressed as the ratio 20:1. This ratio quantifies the designed duplication factor: 5% of each chunk overlaps with adjacent chunks (200/4000 = 0.05), balancing memory efficiency (95% unique content) against semantic continuity (5% overlap to preserve context across boundaries).
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py

## CRITERION 7 [Accuracy]
**Description:** States "Rust" as the first anomalous language name.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source:
```python
        if language == Language.RUST:
            return [
                # Split along function definitions
                "\nfn ",
                "\nconst ",
                "\nlet ",
                # Split along control flow statements
                "\nif ",
                "\nwhile ",
                "\nfor ",
                "\nloop ",
                "\nmatch ",
                "\nconst ",
                # Split by the normal type of lines
                "\n\n",
                "\n",
                " ",
                "",
            ]
```
The get_separators_for_language method in character.py shows Rust's separator list contains the duplicate string "\nconst " appearing at positions 5 and 10 (lines 459 and 467). This makes Rust the first anomalous language.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py#L455-L473

## CRITERION 8 [Accuracy]
**Description:** States "duplicate" as the first anomalous language's anomaly type.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The Rust language configuration contains the separator string "\nconst " appearing multiple times in the same list (positions 5 and 10), making this a duplicate-type anomaly rather than a missing-type anomaly.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py#L455-L473

## CRITERION 9 [Accuracy]
**Description:** States 13 as the first anomalous language's separator count.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Counting the total elements in the Rust separator list yields 13 total separators: "\nfn ", "\nconst ", "\nlet ", "\nif ", "\nwhile ", "\nfor ", "\nloop ", "\nmatch ", "\nconst ", "\n\n", "\n", " ", "".
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py#L455-L473

## CRITERION 10 [Accuracy]
**Description:** States "Haskell" as the second anomalous language name.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source:
```python
        if language == Language.HASKELL:
            return [
                # Split along function definitions
                "\nmain :: ",
                "\nmain = ",
                "\nlet ",
                "\nin ",
                "\ndo ",
                "\nwhere ",
                "\n:: ",
                "\n= ",
                # Split along type declarations
                "\ndata ",
                "\nnewtype ",
                "\ntype ",
                "\n:: ",
                # Split along module declarations
                "\nmodule ",
                # Split along import statements
                "\nimport ",
                "\nqualified ",
                "\nimport qualified ",
                # Split along typeclass declarations
                "\nclass ",
                "\ninstance ",
                # Split along case expressions
                "\ncase ",
                # Split along guards in function definitions
                "\n| ",
                # Split along record field declarations
                "\ndata ",
                "\n= {",
                "\n, ",
                # Split by the normal type of lines
                "\n\n",
                "\n",
                " ",
                "",
            ]
```
The get_separators_for_language method shows Haskell's separator list contains the duplicate string "\ndata " appearing at positions 10 and 27.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py#L708-L748

## CRITERION 11 [Accuracy]
**Description:** States "duplicate" as the second anomalous language's anomaly type.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Haskell's language configuration contains the separator string "\ndata " appearing multiple times (positions 10 and 27), making this a duplicate-type anomaly like Rust.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py#L708-L748

## CRITERION 12 [Accuracy]
**Description:** States 27 as the second anomalous language's separator count.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:**
Source:
```python
if language == Language.HASKELL:
    return [
        # Split along function definitions and bindings
        "\nmain :: ",
        "\nmain = ",
        "\nlet ",
        "\nin ",
        "\ndo ",
        "\nwhere ",
        "\n:: ",
        "\n= ",
        # Split along type declarations
        "\ndata ",
        "\nnewtype ",
        "\ntype ",
        "\n:: ",
        # Split along module declarations
        "\nmodule ",
        # Split along import statements
        "\nimport ",
        "\nqualified ",
        "\nimport qualified ",
        # Split along typeclass declarations
        "\nclass ",
        "\ninstance ",
        # Split along case expressions
        "\ncase ",
        # Split along guards in function definitions
        "\n| ",
        # Split along record field declarations
        "\ndata ",
        "\n= {",
        "\n, ",
        # Split by the normal type of lines
        "\n\n",
        "\n",
        " ",
        "",
    ]
```
Counting all elements in the Haskell separator list yields 27 total separators including the empty string at the end and the duplicated "\ndata " entries at positions 10 and 21.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py#L708-L748

## CRITERION 13 [Accuracy]
**Description:** States "LaTeX" as the third anomalous language name.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source:
```python
        if language == Language.LATEX:
            return [
                # First, try to split along Latex sections
                "\n\\\\chapter{",
                "\n\\\\section{",
                "\n\\\\subsection{",
                "\n\\\\subsubsection{",
                # Now split by environments
                "\n\\\\begin{enumerate}",
                "\n\\\\begin{itemize}",
                "\n\\\\begin{description}",
                "\n\\\\begin{list}",
                "\n\\\\begin{quote}",
                "\n\\\\begin{quotation}",
                "\n\\\\begin{verse}",
                "\n\\\\begin{verbatim}",
                # Now split by math environments
                "\n\\\\begin{align}",
                "$$",
                "$",
                # Now split by the normal type of lines
                " ",
                "",
            ]
```
The LaTeX language configuration is the only language implementation that completely omits the standard "\n\n" (double newline) paragraph separator that appears in all other language separator lists.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py#L536-L559

## CRITERION 14 [Accuracy]
**Description:** States "missing" as the third anomalous language's anomaly type.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** LaTeX's separator list completely omits the "\n\n" double newline separator that serves as the paragraph boundary marker in all 25 other language implementations. This is a missing-type anomaly, distinct from the duplicate-type anomalies in Rust and Haskell.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py#L536-L559

## CRITERION 15 [Accuracy]
**Description:** States 17 as the third anomalous language's separator count.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Counting the total elements in the LaTeX separator list yields 17 total separators.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py#L536-L559

## CRITERION 16 [Accuracy]
**Description:** States 4 as the outer for-loop iteration count for _merge_splits with given inputs.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** Source:
```python
def _merge_splits(self, splits: Iterable[str], separator: str) -> list[str]:
    # ... initialization ...
    for split in splits:  # Iterates over each split
        # Process split
```
Given inputs: splits = ["a"*100, "b"*50, "c"*150, "d"*75], the outer for-loop iterates once for each element in the splits list. The iteration sequence is:
- Iteration 1: Processes "a"*100
- Iteration 2: Processes "b"*50
- Iteration 3: Processes "c"*150
- Iteration 4: Processes "d"*75

Total outer for-loop iterations: 4
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py#L177-L228

## CRITERION 17 [Accuracy]
**Description:** States 3 as the total while-loop iteration count for _merge_splits with given inputs.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** Source:
```python
def _merge_splits(self, splits: Iterable[str], separator: str) -> list[str]:
    separator_len = self._length_function(separator)
    docs = []
    current_doc: list[str] = []
    total = 0
    for d in splits:
        len_ = self._length_function(d)
        if (
            total + len_ + (separator_len if len(current_doc) > 0 else 0)
            > self._chunk_size
        ):
            if total > self._chunk_size:
                logger.warning(
                    "Created a chunk of size %d, which is longer than the "
                    "specified %d",
                    total,
                    self._chunk_size,
                )
            if len(current_doc) > 0:
                doc = self._join_docs(current_doc, separator)
                if doc is not None:
                    docs.append(doc)
                # Keep on popping if:
                # - we have a larger chunk than in the chunk overlap
                # - or if we still have any chunks and the length is long
                while total > self._chunk_overlap or (
                    total + len_ + (separator_len if len(current_doc) > 0 else 0)
                    > self._chunk_size
                    and total > 0
                ):
                    total -= self._length_function(current_doc[0]) + (
                        separator_len if len(current_doc) > 1 else 0
                    )
                    current_doc = current_doc[1:]
        current_doc.append(d)
        total += len_ + (separator_len if len(current_doc) > 1 else 0)
    doc = self._join_docs(current_doc, separator)
    if doc is not None:
        docs.append(doc)
    return docs
```
The while-loop executes during outer loop iterations 3 and 4. Given splits = ["a"*100, "b"*50, "c"*150, "d"*75], separator = "--", chunk_size = 200, chunk_overlap = 50: Iteration 3 processes "c"*150 with current_doc ["a"*100, "b"*50] and total=152. Since 152+150+2=304 > 200, enters while-loop. First iteration: 152 > 50 so pops "a"*100, total=50. Second iteration: 50+150+2=202 > 200 and total > 0 so pops "b"*50, total=0, exits. Iteration 4 processes "d"*75 with current_doc ["c"*150] and total=150. Since 150+75+2=227 > 200, enters while-loop. Third iteration: 150 > 50 so pops "c"*150, total=0, exits. Total while-loop iterations: 2 + 1 = 3.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py#L152-L194

## CRITERION 18 [Accuracy]
**Description:** States 3 as the final docs list element count for _merge_splits with given inputs.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** Source:
```python
def _merge_splits(self, splits: Iterable[str], separator: str) -> list[str]:
    separator_len = self._length_function(separator)
    docs = []
    current_doc: list[str] = []
    total = 0
    for d in splits:
        len_ = self._length_function(d)
        if (
            total + len_ + (separator_len if len(current_doc) > 0 else 0)
            > self._chunk_size
        ):
            if total > self._chunk_size:
                logger.warning(
                    "Created a chunk of size %d, which is longer than the "
                    "specified %d",
                    total,
                    self._chunk_size,
                )
            if len(current_doc) > 0:
                doc = self._join_docs(current_doc, separator)
                if doc is not None:
                    docs.append(doc)
                # Keep on popping if:
                # - we have a larger chunk than in the chunk overlap
                # - or if we still have any chunks and the length is long
                while total > self._chunk_overlap or (
                    total + len_ + (separator_len if len(current_doc) > 0 else 0)
                    > self._chunk_size
                    and total > 0
                ):
                    total -= self._length_function(current_doc[0]) + (
                        separator_len if len(current_doc) > 1 else 0
                    )
                    current_doc = current_doc[1:]
        current_doc.append(d)
        total += len_ + (separator_len if len(current_doc) > 1 else 0)
    doc = self._join_docs(current_doc, separator)
    if doc is not None:
        docs.append(doc)
    return docs
```
Chunks are appended to docs during the for-loop when chunk_size is exceeded and at the end for remaining content. Given splits = ["a"*100, "b"*50, "c"*150, "d"*75], separator = "--", chunk_size = 200, chunk_overlap = 50: Iteration 3 processes "c"*150. Since 152+150+2 > 200, appends chunk 1 with "a"*100 + "--" + "b"*50 to docs. Iteration 4 processes "d"*75. Since 150+75+2 > 200, appends chunk 2 with "c"*150 to docs. After for-loop completes, remaining content "d"*75 is appended as chunk 3 to docs. Final docs contains 3 elements.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py#L152-L194

## CRITERION 19 [Accuracy]
**Description:** States 2 as the count of splitters using chunk_overlap for context preservation.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source 1 (CharacterTextSplitter and RecursiveCharacterTextSplitter class definitions):
```python
class CharacterTextSplitter(TextSplitter):
    """Splitting text that looks at characters."""

class RecursiveCharacterTextSplitter(TextSplitter):
    """Splitting text by recursively look at characters."""
```
Source 2 (TextSplitter base class with chunk_overlap):
```python
class TextSplitter(BaseDocumentTransformer, ABC):
    def __init__(
        self,
        chunk_size: int = 4000,
        chunk_overlap: int = 200,
        ...
    ) -> None:
```
CharacterTextSplitter and RecursiveCharacterTextSplitter both inherit from TextSplitter and use the chunk_overlap parameter for text duplication to preserve context across chunk boundaries. Count: 2.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py

## CRITERION 20 [Accuracy]
**Description:** States 1 as the count of splitters using Document.metadata for context preservation.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source:
```python
class MarkdownHeaderTextSplitter:
    """Splitting markdown files based on specified headers."""

    def aggregate_lines_to_chunks(self, lines: list[LineType]) -> list[Document]:
        """Combine lines with common metadata into chunks."""
        aggregated_chunks: list[LineType] = []
        for line in lines:
            if (
                aggregated_chunks
                and aggregated_chunks[-1]["metadata"] == line["metadata"]
            ):
                # Same headers = join text, keep common metadata
```
MarkdownHeaderTextSplitter uses Document.metadata to inject structural header information, preserving hierarchical context through metadata rather than text duplication. Count: 1.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/markdown.py

## CRITERION 21 [Accuracy]
**Description:** States "2:1" as the ratio of overlap-based splitters to metadata-based splitters.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** From C19 and C20, overlap-based count = 2 (CharacterTextSplitter, RecursiveCharacterTextSplitter), metadata-based count = 1 (MarkdownHeaderTextSplitter). Ratio = 2:1.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/markdown.py

## CRITERION 22 [Accuracy]
**Description:** States 4 as PythonCodeTextSplitter's inheritance depth.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source 1 (PythonCodeTextSplitter):
```python
# python.py
class PythonCodeTextSplitter(RecursiveCharacterTextSplitter):
    """Attempts to split the text along Python syntax."""
```
Source 2 (RecursiveCharacterTextSplitter):
```python
# character.py
class RecursiveCharacterTextSplitter(TextSplitter):
    """Splitting text by recursively look at characters."""
```
Source 3 (TextSplitter):
```python
# base.py
class TextSplitter(BaseDocumentTransformer, ABC):
    """Interface for splitting text into chunks."""
```
Inheritance chain: PythonCodeTextSplitter → RecursiveCharacterTextSplitter → TextSplitter → BaseDocumentTransformer. Depth = 4 levels.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/python.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py

## CRITERION 23 [Accuracy]
**Description:** States 2 as HTMLSemanticPreservingSplitter's inheritance depth.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source:
```python
# html.py
class HTMLSemanticPreservingSplitter(BaseDocumentTransformer):
    """Split HTML while preserving semantic structure."""
```
Inheritance chain: HTMLSemanticPreservingSplitter → BaseDocumentTransformer. When counting inheritance depth, we count each class in the chain as one level. HTMLSemanticPreservingSplitter is level 1, and BaseDocumentTransformer is level 2. Note that BaseDocumentTransformer itself inherits from object (Python's implicit base class), but we stop counting at the LangChain framework boundary. This differs from RecursiveJsonSplitter (1 level, no framework inheritance) and PythonCodeTextSplitter (4 levels with deeper chain through TextSplitter). Depth = 2 levels.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/html.py

## CRITERION 24 [Accuracy]
**Description:** States 1 as RecursiveJsonSplitter's inheritance depth.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source:
```python
# json.py
class RecursiveJsonSplitter:
    """Splits JSON data into smaller, structured chunks while preserving hierarchy."""
```
RecursiveJsonSplitter has no explicit parent class, implicitly inherits from object. When counting inheritance depth, we count the class itself as 1 level. Unlike HTMLSemanticPreservingSplitter (which has 2 levels: HTMLSemanticPreservingSplitter → BaseDocumentTransformer) or PythonCodeTextSplitter (which has 4 levels), RecursiveJsonSplitter stands alone with no LangChain framework inheritance. Depth = 1 level.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/json.py

## CRITERION 25 [Accuracy]
**Description:** States 7 as the sum of all three inheritance depths.
**Weight:** Critical
**Numerical Weight:** 8
**Rationale:** From C22, C23, C24: PythonCodeTextSplitter depth = 4, HTMLSemanticPreservingSplitter depth = 2, RecursiveJsonSplitter depth = 1. Sum = 4 + 2 + 1 = 7.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/python.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/html.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/json.py

## CRITERION 26 [Accuracy]
**Description:** States 111 as the total character count for Language.HTML's separator list.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source:
```python
if language == Language.HTML:
    return [
        # First, try to split along HTML tags
        "<body",
        "<div",
        "<p",
        "<br",
        "<li",
        "<h1",
        "<h2",
        "<h3",
        "<h4",
        "<h5",
        "<h6",
        "<span",
        "<table",
        "<tr",
        "<td",
        "<th",
        "<ul",
        "<ol",
        "<header",
        "<footer",
        "<nav",
        # Head
        "<head",
        "<style",
        "<script",
        "<meta",
        "<title",
        "",
    ]
```
Character counts (excluding empty string): 5+4+2+3+3+3+3+3+3+3+3+5+6+3+3+3+3+3+7+7+4+5+6+7+5+6 = 111 total characters.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py#L560-L591

## CRITERION 27 [Accuracy]
**Description:** States 22 as the total character count for Language.PYTHON's separator list.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source:
```python
if language == Language.PYTHON:
    return [
        # First, try to split along class definitions
        "\nclass ",
        "\ndef ",
        "\n\tdef ",
        # Now split by the normal type of lines
        "\n\n",
        "\n",
        " ",
        "",
    ]
```
Character counts (excluding empty string): 7+5+6+2+1+1 = 22 total characters.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py#L363-L374

## CRITERION 28 [Accuracy]
**Description:** States "111:22" as the HTML:PYTHON character count ratio.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** From C26 and C27: HTML character count = 111, PYTHON character count = 22. Ratio = 111:22. GCD(111, 22) = 1, so ratio cannot be simplified.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 29 [Accuracy]
**Description:** States that CharacterTextSplitter achieves O(n) time complexity.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source:
```python
class CharacterTextSplitter(TextSplitter):
    def split_text(self, text: str) -> list[str]:
        sep_pattern = (
            self._separator if self._is_separator_regex else re.escape(self._separator)
        )
        splits = _split_text_with_regex(
            text, sep_pattern, keep_separator=self._keep_separator
        )
        merge_sep = ""
        if not (self._keep_separator or is_lookaround):
            merge_sep = self._separator
        return self._merge_splits(splits, merge_sep)
```
CharacterTextSplitter performs one split operation (linear scan) and one merge operation (linear scan of splits), achieving O(n) time complexity.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 30 [Accuracy]
**Description:** States that RecursiveCharacterTextSplitter achieves O(n) time complexity.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source:
```python
class RecursiveCharacterTextSplitter(TextSplitter):
    def __init__(
        self,
        separators: list[str] | None = None,
        ...
    ) -> None:
        self._separators = separators or ["\n\n", "\n", " ", ""]

    def _split_text(self, text: str, separators: list[str]) -> list[str]:
        final_chunks = []
        separator = separators[-1]
        for i, s_ in enumerate(separators):
            if re.search(separator_, text):
                separator = s_
                new_separators = separators[i + 1 :]
                break
        splits = _split_text_with_regex(text, separator_, keep_separator=self._keep_separator)
        for s in splits:
            if self._length_function(s) < self._chunk_size:
                good_splits.append(s)
            else:
                if not new_separators:
                    final_chunks.append(s)
                else:
                    other_info = self._split_text(s, new_separators)
                    final_chunks.extend(other_info)
        return final_chunks
```
RecursiveCharacterTextSplitter achieves O(n) time complexity despite recursion because recursion depth is bounded by constant separator count (default 4), and each character is processed once per level. Overall: O(k×n) = O(n) where k is constant.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 31 [Accuracy]
**Description:** States that MarkdownHeaderTextSplitter achieves O(n) time complexity.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source:
```python
class MarkdownHeaderTextSplitter:
    def split_text(self, text: str) -> list[Document]:
        """Split markdown file."""
        lines = text.split("\n")
        lines_with_metadata: list[LineType] = []
        current_content: list[str] = []
        current_metadata: dict[str, str] = {}

        for line in lines:
            # Check each line for headers
            for sep, name in self.headers_to_split_on:
                if line.startswith(sep) and (
                    # Header with space: "### Some Header"
                    len(line) == len(sep) or line[len(sep)] == " "
                ):
                    # Process header
```
MarkdownHeaderTextSplitter performs a single linear pass through lines, checking each line for headers. Time complexity: O(n).
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/markdown.py

## CRITERION 32 [Accuracy]
**Description:** States 3 as the count of implementations maintaining linear time bounds.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** From C29, C30, C31: Source 1 (CharacterTextSplitter) achieves O(n) with single split and merge operations. Source 2 (RecursiveCharacterTextSplitter) achieves O(n) with bounded recursion depth of 4 separators. Source 3 (MarkdownHeaderTextSplitter) achieves O(n) with single linear pass through lines. Count of implementations with linear time complexity: 3.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/markdown.py

## CRITERION 33 [Image]
**Description:** Outputs the comparison in a table format.
**Weight:** Major
**Numerical Weight:** 4
**Rationale:** The prompt explicitly requests: "Create a comparison table showing three architectural dimensions for each of the three main splitters." The response must present the comparison as a structured table (markdown, HTML, or other tabular format) rather than as prose paragraphs or lists.
**Sources:** Prompt

## CRITERION 34 [Image]
**Description:** Formats the table with exactly 3 columns.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** The prompt specifies three dimensions: "Algorithm", "Time Complexity", "Context Preservation". The table must have exactly 3 columns to represent these three architectural dimensions.
**Sources:** Prompt

## CRITERION 35 [Image]
**Description:** Formats the table with exactly 3 data rows (excluding header).
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** The prompt requires comparing the three main splitters: CharacterTextSplitter, RecursiveCharacterTextSplitter, and MarkdownHeaderTextSplitter. The table must have exactly 3 data rows (one per splitter), excluding the header row.
**Sources:** Prompt

## CRITERION 36 [Image]
**Description:** Includes "Algorithm" as a column header in the comparison table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt specifies: "Label columns as: 'Algorithm', 'Time Complexity', 'Context Preservation'." The table must include "Algorithm" as one of the three column headers.
**Sources:** Prompt

## CRITERION 37 [Image]
**Description:** Includes "Time Complexity" as a column header in the comparison table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt specifies that "Time Complexity" should be one of the columns. The table must include "Time Complexity" as one of the three column headers.
**Sources:** Prompt

## CRITERION 38 [Image]
**Description:** Includes "Context Preservation" as a column header in the comparison table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt specifies that "Context Preservation" should be one of the columns. The table must include "Context Preservation" as one of the three column headers.
**Sources:** Prompt

## CRITERION 39 [Image]
**Description:** Includes CharacterTextSplitter as a row in the comparison table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt explicitly requests comparison of the three main splitters including CharacterTextSplitter. The table must include CharacterTextSplitter as one of the three algorithm rows.
**Sources:** Prompt

## CRITERION 40 [Image]
**Description:** Includes RecursiveCharacterTextSplitter as a row in the comparison table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt explicitly requests comparison of the three main splitters including RecursiveCharacterTextSplitter. The table must include RecursiveCharacterTextSplitter as one of the three algorithm rows.
**Sources:** Prompt

## CRITERION 41 [Image]
**Description:** Includes MarkdownHeaderTextSplitter as a row in the comparison table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt explicitly requests comparison of the three main splitters including MarkdownHeaderTextSplitter. The table must include MarkdownHeaderTextSplitter as one of the three algorithm rows.
**Sources:** Prompt

## CRITERION 42 [Image]
**Description:** States "O(n)" as CharacterTextSplitter's time complexity value in the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** CharacterTextSplitter performs one split operation and one merge operation, each processing characters linearly, achieving O(n) time complexity. The table cell for CharacterTextSplitter's Time Complexity column must display "O(n)".
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 43 [Image]
**Description:** States "O(n)" as RecursiveCharacterTextSplitter's time complexity value in the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** RecursiveCharacterTextSplitter iterates through at most 4 separators (bounded depth) with linear scanning at each level. Each character is visited a constant number of times, achieving O(n) time complexity. The table cell must display "O(n)".
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 44 [Image]
**Description:** States "O(n)" as MarkdownHeaderTextSplitter's time complexity value in the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** MarkdownHeaderTextSplitter performs one split operation on newlines, then one linear pass to identify headers. Each line is processed once, achieving O(n) time complexity. The table cell must display "O(n)".
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/markdown.py

## CRITERION 45 [Image]
**Description:** States "chunk_overlap (text duplication)" as CharacterTextSplitter's context preservation value in the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** CharacterTextSplitter inherits from TextSplitter and uses the chunk_overlap parameter to duplicate text across chunk boundaries. The table cell must display "chunk_overlap (text duplication)" or equivalent description.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py

## CRITERION 46 [Image]
**Description:** States "chunk_overlap (text duplication)" as RecursiveCharacterTextSplitter's context preservation value in the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** RecursiveCharacterTextSplitter inherits from TextSplitter and uses the chunk_overlap parameter to duplicate text across chunk boundaries. The table cell must display "chunk_overlap (text duplication)" or equivalent description.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py

## CRITERION 47 [Image]
**Description:** States "Document.metadata (structural injection)" as MarkdownHeaderTextSplitter's context preservation value in the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** MarkdownHeaderTextSplitter extracts structural header information and injects it into Document.metadata, preserving hierarchical context through metadata rather than text duplication. The table cell must display "Document.metadata (structural injection)" or equivalent description.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/markdown.py

---

## Summary

**Total Criteria:** 47 (all positive)
**Maximum Score:** 133 points

**Category Breakdown:**
- **Analytical Criteria (C1-C32):** 32 criteria testing separator counts, language anomalies, loop tracing, context preservation, inheritance depth, character ratios, and time complexity
- **Table Criteria (C33-C47):** 15 criteria testing table structure (3), column headers (3), row entries (3), and cell values (6)

**Weight Distribution:**
- **Critical (8 points):** 1 criterion (C25: inheritance depth sum)
- **Major (4-6 points):** 11 criteria (C3, C6, C16-C18, C21, C28, C32-C35)
- **Minor (2 points):** 35 criteria (C1-C2, C4-C5, C7-C15, C19-C20, C22-C24, C26-C27, C29-C31, C36-C47)

**Evaluation Methodology:**
Every criterion requires specific, verifiable answers. Analytical criteria (C1-C32) test deep understanding of algorithm implementation details. Table criteria (C33-C47) verify structural formatting and correct cell values for time complexity and context preservation mechanisms.
