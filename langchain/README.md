# LangChain Text Chunking Algorithm Analysis - Project 2 Task

## Task Overview

**Subdomain:** Algorithmic Analysis
**Routing:** Scratch (3+ sources from LangChain repository)
**Target Models:** Deep Research models (Gemini 3.0 Pro, Gemini DR, ChatGPT DR)
**Expected Difficulty:** 20-80% failure rate

## Task Description

This task requires analyzing and comparing text chunking algorithms used in LangChain's document processing system for large language model applications. The analysis focuses on algorithmic approaches for splitting long documents into semantically meaningful segments suitable for embedding and retrieval.

## Task Components

### 1. **PROMPT.md**
Main research prompt requesting comparison of text chunking strategies across multiple dimensions:
- Algorithm type and strategy
- Time complexity analysis
- Context preservation methods
- Optimal document types
- Separator handling approaches

### 2. **SUBPROMPTS.md**
15 verification questions with 1-5 word answers extracted from source code:
- Default parameters (chunk_size, chunk_overlap, separators)
- Implementation details (data structures, functions, modules)
- Complexity analysis (time, space)
- Validation constraints

### 3. **GOLDEN_RESPONSE.md**
Scientific report (500+ words) analyzing text chunking algorithms:
- Introduction to the problem space
- CharacterTextSplitter analysis
- RecursiveCharacterTextSplitter analysis
- Markdown-aware splitting
- Comparative analysis with table
- References

### 4. **COMPARISON_TABLE.md**
Visual comparison table showing:
- 3 algorithms (rows)
- 5 dimensions (columns)
- Clear formatting for image generation

### 5. **RUBRICS.md**
40 evaluation criteria with three tags:
- **Accuracy [C1-C15]:** Sub-prompt verification (15 criteria)
- **Quality [C16-C30]:** Analytical depth and correctness (15 criteria)
- **Image [C31-C40]:** Table completeness and clarity (10 criteria)

### 6. **CITATIONS.md**
Source documentation:
- base.py (Essential)
- character.py (Essential)
- markdown.py (Optional)

### 7. **SCAFFOLD.md**
Summary of expected answers and table structure

## Sources

All sources are from the LangChain text-splitters library:

1. **base.py** - TextSplitter abstract base class with default parameters and core algorithm
2. **character.py** - CharacterTextSplitter and RecursiveCharacterTextSplitter implementations
3. **markdown.py** - MarkdownHeaderTextSplitter structure-aware implementation

## Key Requirements Met

✅ **Image requirement:** Comparison table with 5 columns and 3 rows
✅ **Golden response:** 500+ words with scientific formatting
✅ **Sub-prompts:** 15 single-sentence questions with 1-5 word answers
✅ **Sources:** 3 high-quality sources (LangChain implementation files)
✅ **Routing:** Scratch (3+ sources from one repo)
✅ **Rubrics:** 40 criteria with Accuracy/Quality/Image tags
✅ **Slightly underspecified:** Prompt allows research flexibility in analysis approach

## Image Generation

Convert COMPARISON_TABLE.md to image format:
- Use spreadsheet software (Excel, Google Sheets)
- Use table-to-image tools
- Use markdown renderers with screenshot
- Upload to Google Drive and add link to GOLDEN_RESPONSE.md

## Validation

Verify all sub-prompt answers against source code:
```bash
grep -n "chunk_size: int = 4000" langchain/libs/text-splitters/langchain_text_splitters/base.py
grep -n "separator: str" langchain/libs/text-splitters/langchain_text_splitters/character.py
grep -n "_separators" langchain/libs/text-splitters/langchain_text_splitters/character.py
```

## Usage Notes

This task tests Deep Research models' ability to:
- Analyze algorithmic complexity
- Compare implementation strategies
- Extract specific technical details from source code
- Synthesize comparative analysis with visual representation
- Maintain scientific writing standards

Expected performance: 20-80% failure rate due to requirement for both deep technical analysis and precise fact extraction from source code.
