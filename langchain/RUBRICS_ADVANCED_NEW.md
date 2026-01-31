# RUBRICS_ADVANCED - LangChain Text Splitters Analysis - 47 Criteria

## Overview
- **Total Criteria**: 47 (all positive)
- **Domain**: Algorithmic Analysis - Text Chunking Strategies
- **Repository**: langchain-ai/langchain (text-splitters library)
- **Commit**: 72571185a8f51e353a2fe9143855f310c4d31e08
- **Task Type**: Research & Analysis (Scratch Routing)

---

## CRITERION 1 [Accuracy]
**Description:** States 4 as the count of default separators that RecursiveCharacterTextSplitter evaluates.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source: "
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
"
The default separators list `["\n\n", "\n", " ", ""]` contains exactly 4 elements, representing a hierarchical fallback strategy from paragraph boundaries (double newline) to line boundaries (single newline) to word boundaries (space) to character-level splitting (empty string).
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 2 [Accuracy]
**Description:** States 1 as the count of default separators that CharacterTextSplitter evaluates.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source: "
```python
def __init__(
    self,
    separator: str = "\n\n",
    is_separator_regex: bool = False,
    **kwargs: Any,
) -> None:
```
"
CharacterTextSplitter uses a single separator parameter with default value `"\n\n"`, meaning it evaluates only 1 separator (paragraph boundaries), unlike RecursiveCharacterTextSplitter's hierarchical approach.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 3 [Accuracy]
**Description:** States 3 as the difference between RecursiveCharacterTextSplitter's separator count and CharacterTextSplitter's separator count.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** Source 1 (RecursiveCharacterTextSplitter): "
```python
self._separators = separators or ["\n\n", "\n", " ", ""]
```
"
Source 2 (CharacterTextSplitter): "
```python
separator: str = "\n\n"
```
"
The calculation is: RecursiveCharacterTextSplitter's 4 default separators (count of list elements) minus CharacterTextSplitter's 1 default separator equals 3. This difference quantifies the algorithmic sophistication gap—RecursiveCharacterTextSplitter provides 3 additional fallback levels beyond the simple single-separator approach, enabling adaptive splitting across paragraph, line, word, and character boundaries.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 4 [Accuracy]
**Description:** States 4000 as the default chunk_size value in TextSplitter.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source: "
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
"
The default chunk_size=4000 establishes the maximum target size for text chunks, measured by the length_function (default: character count).
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py

## CRITERION 5 [Accuracy]
**Description:** States 200 as the default chunk_overlap value in TextSplitter.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source: "
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
"
The default chunk_overlap=200 creates a rolling window effect where consecutive chunks share 200 units (typically characters) of content, preventing context loss at chunk boundaries.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py

## CRITERION 6 [Accuracy]
**Description:** States "20:1" as the ratio of default chunk_size to default chunk_overlap.
**Weight:** Major
**Numerical Weight:** 6
**Rationale:** Source: "
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
"
The calculation is: chunk_size (4000) divided by chunk_overlap (200) equals 20, expressed as the ratio 20:1. This ratio quantifies the designed duplication factor: 5% of each chunk overlaps with adjacent chunks (200/4000 = 0.05), balancing memory efficiency (95% unique content) against semantic continuity (5% overlap to preserve context across boundaries).
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py

## CRITERION 7 [Accuracy]
**Description:** States 4 as the count of specialized splitter classes that inherit from RecursiveCharacterTextSplitter.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** Source 1: "
```python
class PythonCodeTextSplitter(RecursiveCharacterTextSplitter):
    \"\"\"Attempts to split the text along Python syntax.\"\"\"
```
"
Source 2: "
```python
class LatexTextSplitter(RecursiveCharacterTextSplitter):
    \"\"\"Attempts to split the text along Latex-formatted layout elements.\"\"\"
```
"
Source 3: "
```python
class MarkdownTextSplitter(RecursiveCharacterTextSplitter):
    \"\"\"Attempts to split the text along Markdown-formatted headings.\"\"\"
```
"
Source 4: "
```python
class JSFrameworkTextSplitter(RecursiveCharacterTextSplitter):
    \"\"\"Text splitter that handles React (JSX), Vue, and Svelte code.\"\"\"
```
"

Four specialized classes inherit from RecursiveCharacterTextSplitter: PythonCodeTextSplitter, LatexTextSplitter, MarkdownTextSplitter, and JSFrameworkTextSplitter. This count demonstrates that RecursiveCharacterTextSplitter serves as the preferred architectural foundation for domain-specific extensions.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/python.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/latex.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/markdown.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/jsx.py

## CRITERION 8 [Accuracy]
**Description:** States 2 as the count of parent classes that TextSplitter inherits from.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** Source: "
```python
from abc import ABC, abstractmethod
from langchain_core.documents import BaseDocumentTransformer, Document

class TextSplitter(BaseDocumentTransformer, ABC):
    \"\"\"Interface for splitting text into chunks.\"\"\"
```
"
TextSplitter inherits from exactly 2 parent classes: BaseDocumentTransformer (providing document transformation protocol) and ABC (Abstract Base Class from Python's abc module, making TextSplitter abstract).
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py

## CRITERION 9 [Accuracy]
**Description:** States 1 as the count of abstract methods that TextSplitter defines.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** Source: "
```python
@abstractmethod
def split_text(self, text: str) -> list[str]:
    \"\"\"Split text into multiple components.

    Args:
        text: The text to split.

    Returns:
        A list of text chunks.
    \"\"\"
```
"
TextSplitter defines exactly 1 abstract method: `split_text`. The @abstractmethod decorator enforces that all concrete subclasses must implement this method.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py

## CRITERION 10 [Accuracy]
**Description:** States 3 as the sum of parent classes and abstract methods for TextSplitter.
**Weight:** Critical
**Numerical Weight:** 8
**Rationale:** Source 1 (parent classes): "
```python
from abc import ABC, abstractmethod
from langchain_core.documents import BaseDocumentTransformer, Document

class TextSplitter(BaseDocumentTransformer, ABC):
    \"\"\"Interface for splitting text into chunks.\"\"\"
```
"
Source 2 (abstract method): "
```python
@abstractmethod
def split_text(self, text: str) -> list[str]:
    \"\"\"Split text into multiple components.

    Args:
        text: The text to split.

    Returns:
        A list of text chunks.
    \"\"\"
```
"
The calculation is: 2 parent classes (BaseDocumentTransformer + ABC) plus 1 abstract method (split_text) equals 3 total architectural obligations. This sum quantifies the contract complexity that TextSplitter imposes—subclasses must implement 1 abstract method while conforming to 2 parent class interfaces, establishing the architectural foundation for all text splitter implementations.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py

## CRITERION 11 [Accuracy]
**Description:** States 2 as the count of splitters using separator-based overlap for context preservation.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** Source: "
```python
class TextSplitter(BaseDocumentTransformer, ABC):
    def __init__(
        self,
        chunk_size: int = 4000,
        chunk_overlap: int = 200,  # <-- overlap parameter for text duplication
        length_function: Callable[[str], int] = len,
        keep_separator: bool | Literal["start", "end"] = False,
        add_start_index: bool = False,
        strip_whitespace: bool = True,
    ) -> None:
```

```python
class CharacterTextSplitter(TextSplitter):
    # Inherits chunk_overlap from TextSplitter
    pass

class RecursiveCharacterTextSplitter(TextSplitter):
    # Inherits chunk_overlap from TextSplitter
    pass
```
"
CharacterTextSplitter and RecursiveCharacterTextSplitter both inherit from TextSplitter and use the chunk_overlap parameter to duplicate text across adjacent chunks. The overlap creates a sliding window where the last chunk_overlap characters of one chunk become the first chunk_overlap characters of the next chunk, preserving context through text duplication. Count: 2 splitters.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py

## CRITERION 12 [Accuracy]
**Description:** States 1 as the count of splitters using metadata-based context preservation.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** Source: "
```python
def split_text(self, text: str) -> list[Document]:
    lines_with_metadata: list[LineType] = []
    current_metadata: dict[str, str] = {}
    # ... header extraction logic ...
    return [
        Document(page_content=chunk['content'], metadata=chunk['metadata'])
        for chunk in aggregated_chunks
    ]
```
"
MarkdownHeaderTextSplitter uses Document.metadata to inject structural header information, preserving hierarchical context through metadata rather than text duplication. Count: 1 splitter.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/markdown.py

## CRITERION 13 [Accuracy]
**Description:** States "2:1" as the ratio of separator-based splitters to metadata-based splitters.
**Weight:** Major
**Numerical Weight:** 6
**Rationale:** Source 1 (separator-based): "
```python
# CharacterTextSplitter and RecursiveCharacterTextSplitter both inherit from TextSplitter
class TextSplitter(BaseDocumentTransformer, ABC):
    def __init__(
        self,
        chunk_size: int = 4000,
        chunk_overlap: int = 200,  # <-- text duplication parameter
        ...
    ) -> None:
```
"
Source 2 (metadata-based): "
```python
def split_text(self, text: str) -> list[Document]:
    lines_with_metadata: list[LineType] = []
    current_metadata: dict[str, str] = {}  # <-- metadata injection
    # ... header extraction logic ...
    return [
        Document(page_content=chunk['content'], metadata=chunk['metadata'])
        for chunk in aggregated_chunks
    ]
```
"
The calculation is: 2 separator-based splitters (CharacterTextSplitter, RecursiveCharacterTextSplitter using chunk_overlap) divided by 1 metadata-based splitter (MarkdownHeaderTextSplitter using Document.metadata) equals the ratio 2:1. This ratio reveals that overlap-based strategies dominate the architecture—twice as many implementations use text duplication versus structural metadata injection for context preservation.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/markdown.py

## CRITERION 14 [Accuracy]
**Description:** States that keep_separator has different default values between CharacterTextSplitter and RecursiveCharacterTextSplitter.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source 1 (TextSplitter base): "
```python
keep_separator: bool | Literal["start", "end"] = False
```
"
Source 2 (RecursiveCharacterTextSplitter): "
```python
keep_separator: bool | Literal["start", "end"] = True
```
"
CharacterTextSplitter inherits the False default from TextSplitter (discards separators), while RecursiveCharacterTextSplitter overrides with True (retains separators). This is a difference in default values.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 15 [Accuracy]
**Description:** States that chunk_size has matching default values between CharacterTextSplitter and RecursiveCharacterTextSplitter.
**Weight:** Minor
**Numerical Weight:** 1
**Rationale:** Source: "
```python
class TextSplitter(BaseDocumentTransformer, ABC):
    def __init__(
        self,
        chunk_size: int = 4000,  # <-- both inherit this default
        chunk_overlap: int = 200,
        length_function: Callable[[str], int] = len,
        keep_separator: bool | Literal["start", "end"] = False,
        add_start_index: bool = False,
        strip_whitespace: bool = True,
    ) -> None:
```
"
Both CharacterTextSplitter and RecursiveCharacterTextSplitter inherit from TextSplitter without overriding chunk_size, so both use the TextSplitter default value of 4000. This is a matching default value.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 16 [Accuracy]
**Description:** States that chunk_overlap has matching default values between CharacterTextSplitter and RecursiveCharacterTextSplitter.
**Weight:** Minor
**Numerical Weight:** 1
**Rationale:** Source: "
```python
class TextSplitter(BaseDocumentTransformer, ABC):
    def __init__(
        self,
        chunk_size: int = 4000,
        chunk_overlap: int = 200,  # <-- both inherit this default
        length_function: Callable[[str], int] = len,
        keep_separator: bool | Literal["start", "end"] = False,
        add_start_index: bool = False,
        strip_whitespace: bool = True,
    ) -> None:
```
"
Both CharacterTextSplitter and RecursiveCharacterTextSplitter inherit from TextSplitter without overriding chunk_overlap, so both use the TextSplitter default value of 200. This is a matching default value.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 17 [Accuracy]
**Description:** States that strip_whitespace has matching default values between CharacterTextSplitter and RecursiveCharacterTextSplitter.
**Weight:** Minor
**Numerical Weight:** 1
**Rationale:** Source: "
```python
class TextSplitter(BaseDocumentTransformer, ABC):
    def __init__(
        self,
        chunk_size: int = 4000,
        chunk_overlap: int = 200,
        length_function: Callable[[str], int] = len,
        keep_separator: bool | Literal["start", "end"] = False,
        add_start_index: bool = False,
        strip_whitespace: bool = True,  # <-- both inherit this default
    ) -> None:
```
"
Both CharacterTextSplitter and RecursiveCharacterTextSplitter inherit from TextSplitter without overriding strip_whitespace, so both use the TextSplitter default value of True. This is a matching default value.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 18 [Accuracy]
**Description:** States that add_start_index has matching default values between CharacterTextSplitter and RecursiveCharacterTextSplitter.
**Weight:** Minor
**Numerical Weight:** 1
**Rationale:** Source: "
```python
class TextSplitter(BaseDocumentTransformer, ABC):
    def __init__(
        self,
        chunk_size: int = 4000,
        chunk_overlap: int = 200,
        length_function: Callable[[str], int] = len,
        keep_separator: bool | Literal["start", "end"] = False,
        add_start_index: bool = False,  # <-- both inherit this default
        strip_whitespace: bool = True,
    ) -> None:
```
"
Both CharacterTextSplitter and RecursiveCharacterTextSplitter inherit from TextSplitter without overriding add_start_index, so both use the TextSplitter default value of False. This is a matching default value.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 19 [Accuracy]
**Description:** States 1 as the count of parameters with different default values between CharacterTextSplitter and RecursiveCharacterTextSplitter.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** Source 1 (TextSplitter defaults inherited by CharacterTextSplitter): "
```python
def __init__(
    self,
    chunk_size: int = 4000,
    chunk_overlap: int = 200,
    keep_separator: bool | Literal["start", "end"] = False,
    add_start_index: bool = False,
    strip_whitespace: bool = True,
) -> None:
```
"
Source 2 (RecursiveCharacterTextSplitter override): "
```python
def __init__(
    self,
    separators: list[str] | None = None,
    keep_separator: bool | Literal["start", "end"] = True,  # <-- overrides to True
    is_separator_regex: bool = False,
    **kwargs: Any,
) -> None:
```
"
Comparing the five parameters:
- chunk_size: both inherit 4000 (match)
- chunk_overlap: both inherit 200 (match)
- keep_separator: False vs True (different)
- strip_whitespace: both inherit True (match)
- add_start_index: both inherit False (match)

Count of mismatched parameters: 1 (keep_separator only).
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 20 [Accuracy]
**Description:** States 2 as the count of distinct list variables used for chunk accumulation in RecursiveCharacterTextSplitter's _split_text method.
**Weight:** Major
**Numerical Weight:** 4
**Rationale:** Source: "
```python
def _split_text(self, text: str, separators: list[str]) -> list[str]:
    final_chunks = []
    # ... splitting logic ...
    good_splits = []
    for s in splits:
        if self._length_function(s) < self._chunk_size:
            good_splits.append(s)
        else:
            if good_splits:
                merged_text = self._merge_splits(good_splits, separator_)
                final_chunks.extend(merged_text)
                good_splits = []
    # ...
    return final_chunks
```
"
Two distinct list variables accumulate chunks: (1) `good_splits` accumulates segments smaller than chunk_size before merging, and (2) `final_chunks` stores the merged output chunks that will be returned. This two-stage strategy separates validation from assembly.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 21 [Accuracy]
**Description:** States that CharacterTextSplitter achieves O(n) time complexity.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** Source: "
```python
def split_text(self, text: str) -> list[str]:
    splits = _split_text_with_regex(text, sep_pattern, keep_separator=self._keep_separator)
    return self._merge_splits(splits, merge_sep)
```
"
CharacterTextSplitter performs one split operation on the separator (linear scan) and one merge operation (linear iteration over splits). Each character is processed a constant number of times, achieving O(n) time complexity for documents of length n.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 22 [Accuracy]
**Description:** States that RecursiveCharacterTextSplitter achieves O(n) time complexity.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** Source: "
```python
def _split_text(self, text: str, separators: list[str]) -> list[str]:
    final_chunks = []
    separator = separators[-1]
    new_separators = []
    for i, sep in enumerate(separators):  # Bounded: max 4 iterations
        if sep == "":
            separator = sep
            break
        if re.search(sep, text) if self._is_separator_regex else (sep in text):
            separator = sep
            new_separators = separators[i + 1 :]
            break

    splits = text.split(separator) if not self._is_separator_regex else re.split(separator, text)  # O(n) split
    # ... merge logic with bounded recursion ...
    return final_chunks
```
"
RecursiveCharacterTextSplitter iterates through at most 4 separators (bounded depth) with linear scanning at each level. Despite the hierarchical recursion, each character is visited a constant number of times (maximum 4 separator attempts). The bounded recursion depth ensures O(n) time complexity for documents of length n.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 23 [Accuracy]
**Description:** States that MarkdownHeaderTextSplitter achieves O(n) time complexity.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** Source: "
```python
def split_text(self, text: str) -> list[Document]:
    lines = text.split('\n')
    for line in lines:
        # process each line once
        # ... header extraction ...
    return self.aggregate_lines_to_chunks(lines_with_metadata)
```
"
MarkdownHeaderTextSplitter performs one linear scan splitting on newlines, then one linear iteration over lines for header extraction. Each character is processed a constant number of times, achieving O(n) time complexity for documents of length n.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/markdown.py

## CRITERION 24 [Accuracy]
**Description:** States 3 as the count of implementations that achieve O(n) time complexity.
**Weight:** Critical
**Numerical Weight:** 9
**Rationale:** Source 1 (CharacterTextSplitter): "
```python
def split_text(self, text: str) -> list[str]:
    splits = _split_text_with_regex(text, sep_pattern, keep_separator=self._keep_separator)
    return self._merge_splits(splits, merge_sep)
```
"
Source 2 (RecursiveCharacterTextSplitter): "
```python
def _split_text(self, text: str, separators: list[str]) -> list[str]:
    # Bounded depth (max 4 separators), each level scans linearly
    for i, sep in enumerate(separators):  # max 4 iterations
        splits = text.split(sep)  # O(n) at each level
        # ... bounded recursion ...
```
"
Source 3 (MarkdownHeaderTextSplitter): "
```python
def split_text(self, text: str) -> list[Document]:
    lines = text.split('\n')  # O(n) linear split
    for line in lines:  # O(n) linear iteration
        # process each line once
```
"
All three main splitter implementations achieve O(n) time complexity:
- CharacterTextSplitter: O(n) via single linear split + merge
- RecursiveCharacterTextSplitter: O(n) via bounded-depth hierarchical splitting (max 4 levels)
- MarkdownHeaderTextSplitter: O(n) via linear header extraction

Count: 3 implementations maintain linear time bounds, demonstrating architectural commitment to scalable document processing regardless of splitting strategy.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/markdown.py

## CRITERION 25 [Image]
**Description:** Outputs the comparison in a table format.
**Weight:** Major
**Numerical Weight:** 4
**Rationale:** The prompt explicitly requests: "Create a comparison table showing five architectural dimensions". The response must present the comparison as a structured table (markdown, HTML, or other tabular format) rather than as prose paragraphs. This ensures the five dimensions can be compared side-by-side across the three splitters.
**Sources:** Prompt

## CRITERION 26 [Image]
**Description:** Formats the table with 5 columns.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** The prompt specifies five architectural dimensions: "algorithm name, time complexity for documents of length n, context preservation mechanism, base class inherited from, and number of default separators." The table must have exactly 5 columns to represent these dimensions, plus the algorithm name column makes 5 total.
**Sources:** Prompt

## CRITERION 27 [Image]
**Description:** Formats the table with 3 rows (excluding header).
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** The prompt requires comparing "CharacterTextSplitter, RecursiveCharacterTextSplitter, and MarkdownHeaderTextSplitter" - three specific splitters. The table must have exactly 3 data rows (one per splitter), excluding the header row that contains column labels.
**Sources:** Prompt

## CRITERION 28 [Image]
**Description:** Includes "Algorithm" as a column header in the comparison table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt specifies "Label columns as: 'Algorithm', 'Time Complexity', 'Context Preservation', 'Inherits From', 'Separators'." The table must include "Algorithm" as one of the five column headers.
**Sources:** Prompt

## CRITERION 29 [Image]
**Description:** Includes "Time Complexity" as a column header in the comparison table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt specifies "Label columns as: 'Algorithm', 'Time Complexity', 'Context Preservation', 'Inherits From', 'Separators'." The table must include "Time Complexity" as one of the five column headers.
**Sources:** Prompt

## CRITERION 30 [Image]
**Description:** Includes "Context Preservation" as a column header in the comparison table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt specifies "Label columns as: 'Algorithm', 'Time Complexity', 'Context Preservation', 'Inherits From', 'Separators'." The table must include "Context Preservation" as one of the five column headers.
**Sources:** Prompt

## CRITERION 31 [Image]
**Description:** Includes "Inherits From" as a column header in the comparison table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt specifies "Label columns as: 'Algorithm', 'Time Complexity', 'Context Preservation', 'Inherits From', 'Separators'." The table must include "Inherits From" as one of the five column headers.
**Sources:** Prompt

## CRITERION 32 [Image]
**Description:** Includes "Separators" as a column header in the comparison table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt specifies "Label columns as: 'Algorithm', 'Time Complexity', 'Context Preservation', 'Inherits From', 'Separators'." The table must include "Separators" as one of the five column headers.
**Sources:** Prompt

## CRITERION 33 [Image]
**Description:** Includes CharacterTextSplitter as a row in the comparison table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt explicitly requests comparison of "CharacterTextSplitter, RecursiveCharacterTextSplitter, and MarkdownHeaderTextSplitter." The table must include CharacterTextSplitter as one of the three algorithm rows.
**Sources:** Prompt

## CRITERION 34 [Image]
**Description:** Includes RecursiveCharacterTextSplitter as a row in the comparison table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt explicitly requests comparison of "CharacterTextSplitter, RecursiveCharacterTextSplitter, and MarkdownHeaderTextSplitter." The table must include RecursiveCharacterTextSplitter as one of the three algorithm rows.
**Sources:** Prompt

## CRITERION 35 [Image]
**Description:** Includes MarkdownHeaderTextSplitter as a row in the comparison table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt explicitly requests comparison of "CharacterTextSplitter, RecursiveCharacterTextSplitter, and MarkdownHeaderTextSplitter." The table must include MarkdownHeaderTextSplitter as one of the three algorithm rows.
**Sources:** Prompt

## CRITERION 36 [Image]
**Description:** States "O(n)" as CharacterTextSplitter's time complexity value in the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source: "
```python
def split_text(self, text: str) -> list[str]:
    splits = _split_text_with_regex(
        text, sep_pattern, keep_separator=self._keep_separator
    )
    return self._merge_splits(splits, merge_sep)
```
"
CharacterTextSplitter performs one split operation via `_split_text_with_regex` (linear scan through text) and one merge operation via `_merge_splits` (linear iteration over splits). Each character is processed a constant number of times, achieving O(n) time complexity. The table cell for CharacterTextSplitter's Time Complexity column must display "O(n)".
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 37 [Image]
**Description:** States "O(n)" as RecursiveCharacterTextSplitter's time complexity value in the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source: "
```python
def _split_text(self, text: str, separators: list[str]) -> list[str]:
    final_chunks = []
    separator = separators[-1]
    new_separators = []
    for i, s_ in enumerate(separators):  # Bounded: max 4 iterations
        separator_ = s_ if self._is_separator_regex else re.escape(s_)
        if not s_:
            separator = s_
            break
        if re.search(separator_, text):
            separator = s_
            new_separators = separators[i + 1 :]
            break

    separator_ = separator if self._is_separator_regex else re.escape(separator)
    splits = _split_text_with_regex(text, separator_, keep_separator=self._keep_separator)
    # ... merge logic with bounded recursion ...
    return final_chunks
```
"
RecursiveCharacterTextSplitter iterates through at most 4 separators (bounded depth) with linear scanning at each level. Each character is visited a constant number of times (maximum 4 separator attempts), achieving O(n) time complexity. The table cell for RecursiveCharacterTextSplitter's Time Complexity column must display "O(n)".
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 38 [Image]
**Description:** States "O(n)" as MarkdownHeaderTextSplitter's time complexity value in the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source: "
```python
def split_text(self, text: str) -> list[Document]:
    lines = text.split('\n')  # O(n) - single linear split
    for line in lines:  # O(n) - linear iteration
        # process each line once for header extraction
        # ... header matching logic ...
    return self.aggregate_lines_to_chunks(lines_with_metadata)  # O(n) - linear aggregation
```
"
MarkdownHeaderTextSplitter performs one split operation on newlines, then one linear pass to identify headers and extract metadata. Each line is processed once, achieving O(n) time complexity. The table cell for MarkdownHeaderTextSplitter's Time Complexity column must display "O(n)".
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/markdown.py

## CRITERION 39 [Image]
**Description:** States "chunk_overlap (text duplication)" as CharacterTextSplitter's context preservation value in the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source 1 (CharacterTextSplitter inheritance): "
```python
class CharacterTextSplitter(TextSplitter):
    """Splitting text that looks at characters."""
    # Inherits chunk_overlap parameter from TextSplitter
```
"
Source 2 (TextSplitter chunk_overlap): "
```python
class TextSplitter(BaseDocumentTransformer, ABC):
    def __init__(
        self,
        chunk_size: int = 4000,
        chunk_overlap: int = 200,  # <-- text duplication for context preservation
        ...
    ) -> None:
```
"
CharacterTextSplitter inherits the chunk_overlap mechanism from TextSplitter, which duplicates the last chunk_overlap characters of each chunk as the first chunk_overlap characters of the next chunk, preserving context through text duplication. The table cell for CharacterTextSplitter's Context Preservation column must display "chunk_overlap (text duplication)".
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py

## CRITERION 40 [Image]
**Description:** States "chunk_overlap (text duplication)" as RecursiveCharacterTextSplitter's context preservation value in the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source 1 (RecursiveCharacterTextSplitter inheritance): "
```python
class RecursiveCharacterTextSplitter(TextSplitter):
    """Splitting text by recursively looking at characters."""
    # Inherits chunk_overlap parameter from TextSplitter
```
"
Source 2 (TextSplitter chunk_overlap): "
```python
class TextSplitter(BaseDocumentTransformer, ABC):
    def __init__(
        self,
        chunk_size: int = 4000,
        chunk_overlap: int = 200,  # <-- text duplication for context preservation
        ...
    ) -> None:
```
"
RecursiveCharacterTextSplitter inherits the chunk_overlap mechanism from TextSplitter, which duplicates the last chunk_overlap characters of each chunk as the first chunk_overlap characters of the next chunk, preserving context through text duplication. The table cell for RecursiveCharacterTextSplitter's Context Preservation column must display "chunk_overlap (text duplication)".
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py, https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/base.py

## CRITERION 41 [Image]
**Description:** States "Document.metadata (structural injection)" as MarkdownHeaderTextSplitter's context preservation value in the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source: "
```python
def split_text(self, text: str) -> list[Document]:
    lines_with_metadata: list[LineType] = []
    current_metadata: dict[str, str] = {}  # <-- metadata extraction from headers

    # ... header extraction logic ...

    return [
        Document(page_content=chunk['content'],
                 metadata=chunk['metadata'])  # <-- context preserved via metadata injection
        for chunk in aggregated_chunks
    ]
```
"
MarkdownHeaderTextSplitter extracts structural header information and injects it into Document.metadata, preserving hierarchical context through metadata rather than text duplication. This differs from the chunk_overlap approach used by the TextSplitter-based classes. The table cell for MarkdownHeaderTextSplitter's Context Preservation column must display "Document.metadata (structural injection)".
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/markdown.py

## CRITERION 42 [Image]
**Description:** States "TextSplitter" as CharacterTextSplitter's inheritance value in the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source: "
```python
class CharacterTextSplitter(TextSplitter):
    """Splitting text that looks at characters."""
```
"
CharacterTextSplitter directly inherits from TextSplitter. The table must correctly reflect this parent class in the Inherits From column for the CharacterTextSplitter row.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 43 [Image]
**Description:** States "TextSplitter" as RecursiveCharacterTextSplitter's inheritance value in the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source: "
```python
class RecursiveCharacterTextSplitter(TextSplitter):
    """Splitting text by recursively looking at characters.

    Recursively tries to split by different characters to find one
    that works.
    """
```
"
RecursiveCharacterTextSplitter directly inherits from TextSplitter. The table must correctly reflect this parent class in the Inherits From column for the RecursiveCharacterTextSplitter row.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 44 [Image]
**Description:** States "None (standalone)" as MarkdownHeaderTextSplitter's inheritance value in the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source: "
```python
class MarkdownHeaderTextSplitter:
    \"\"\"Splitting markdown files based on specified headers.\"\"\"

    def __init__(
        self,
        headers_to_split_on: list[tuple[str, str]],
        return_each_line: bool = False,
        strip_headers: bool = True,
    ) -> None:
```
"
MarkdownHeaderTextSplitter is a standalone class with no parent class inheritance, unlike CharacterTextSplitter and RecursiveCharacterTextSplitter which inherit from TextSplitter. The table must correctly reflect this absence of inheritance in the Inherits From column for the MarkdownHeaderTextSplitter row, typically shown as "None (standalone)" or similar.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/markdown.py

## CRITERION 45 [Image]
**Description:** States "1" as CharacterTextSplitter's separator count value in the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source: "
```python
def __init__(
    self,
    separator: str = "\n\n",  # <-- single separator parameter (count: 1)
    is_separator_regex: bool = False,
    **kwargs: Any,
) -> None:
```
"
CharacterTextSplitter uses a single separator parameter with default value `"\n\n"`, evaluating only 1 separator. The table cell for CharacterTextSplitter's Separators column must display "1".
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 46 [Image]
**Description:** States "4" as RecursiveCharacterTextSplitter's separator count value in the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source: "
```python
def __init__(
    self,
    separators: list[str] | None = None,
    keep_separator: bool | Literal["start", "end"] = True,
    is_separator_regex: bool = False,
    **kwargs: Any,
) -> None:
    super().__init__(keep_separator=keep_separator, **kwargs)
    self._separators = separators or ["\n\n", "\n", " ", ""]  # <-- 4 elements (count: 4)
    self._is_separator_regex = is_separator_regex
```
"
RecursiveCharacterTextSplitter's default separators list `["\n\n", "\n", " ", ""]` contains exactly 4 elements. The table cell for RecursiveCharacterTextSplitter's Separators column must display "4".
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/character.py

## CRITERION 47 [Image]
**Description:** States "Variable (header-based)" as MarkdownHeaderTextSplitter's separator count value in the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source: "
```python
def __init__(
    self,
    headers_to_split_on: list[tuple[str, str]],
    return_each_line: bool = False,
    strip_headers: bool = True,
):
    self.headers_to_split_on = headers_to_split_on
```
"
MarkdownHeaderTextSplitter accepts a variable list of header patterns to split on via the `headers_to_split_on` parameter. Unlike the fixed separator counts of CharacterTextSplitter (1) and RecursiveCharacterTextSplitter (4), MarkdownHeaderTextSplitter's separator count varies based on the markdown header levels provided. The table must correctly reflect this variability in the Separators column for the MarkdownHeaderTextSplitter row, typically shown as "Variable (header-based)" or similar.
**Sources:** https://github.com/langchain-ai/langchain/blob/72571185a8f51e353a2fe9143855f310c4d31e08/libs/text-splitters/langchain_text_splitters/markdown.py

---

## Summary

**Total Criteria:** 47 (all positive)
**Maximum Score:** 143 points

**Category Breakdown:**
- **Accuracy Criteria (C1-C24):** 24 criteria testing separator analysis, parameter values, inheritance patterns, context preservation, and time complexity
- **Image/Table Criteria (C25-C47):** 23 criteria testing table structure, format, column headers, algorithm rows, and cell values

**Weight Distribution:**
- **Critical (8-10 points):** 2 criteria (C10: architectural obligations sum, C24: time complexity count)
- **Major (4-7 points):** 9 criteria (C3: separator difference, C6: chunk ratio, C7: inheritance count, C13: preservation ratio, C19: parameter mismatch count, C20: list variables, C25-C27: table structure)
- **Minor (1-3 points):** 36 criteria (all others)

**Evaluation Methodology:**
Every criterion requires specific, verifiable answers. All analytical criteria (C1-C24) reference exact code locations with snippets demonstrating the values. Table structure criteria (C25-C35) verify structural requirements specified in the prompt. Table cell value criteria (C36-C47) verify that the correct values from the codebase appear in the corresponding table cells.

**Source Verification:**
All criteria reference the langchain-ai/langchain repository at commit 72571185a8f51e353a2fe9143855f310c4d31e08, or the prompt for table requirements. Code snippets in rationales enable verification without visiting GitHub.
