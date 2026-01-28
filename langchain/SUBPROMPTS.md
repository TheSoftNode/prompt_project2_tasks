# SUB-PROMPTS

## Question-Answer Pairs

**Sub-prompt #1:** What is the default chunk size in TextSplitter?
**Sub-prompt #1 Answer:** 4000

**Sub-prompt #2:** What is the default chunk overlap in TextSplitter?
**Sub-prompt #2 Answer:** 200

**Sub-prompt #3:** What is the default separator for CharacterTextSplitter?
**Sub-prompt #3 Answer:** \\n\\n

**Sub-prompt #4:** What are the default separators in RecursiveCharacterTextSplitter?
**Sub-prompt #4 Answer:** \\n\\n, \\n, space, empty

**Sub-prompt #5:** What is the time complexity for splitting a document of length n?
**Sub-prompt #5 Answer:** O(n)

**Sub-prompt #6:** What is the space complexity for storing splits of document length n?
**Sub-prompt #6 Answer:** O(n)

**Sub-prompt #7:** What is the default keep_separator value for RecursiveCharacterTextSplitter?
**Sub-prompt #7 Answer:** True

**Sub-prompt #8:** What variable name stores accumulated splits smaller than chunk_size?
**Sub-prompt #8 Answer:** good_splits

**Sub-prompt #9:** What abstract method must all text splitters implement?
**Sub-prompt #9 Answer:** split_text

**Sub-prompt #10:** What happens when chunk_overlap exceeds chunk_size?
**Sub-prompt #10 Answer:** ValueError raised

**Sub-prompt #11:** How does MarkdownHeaderTextSplitter maintain context across chunks?
**Sub-prompt #11 Answer:** Hierarchical header information

**Sub-prompt #12:** What context preservation method does CharacterTextSplitter use?
**Sub-prompt #12 Answer:** Fixed overlap

**Sub-prompt #13:** What context preservation method does RecursiveCharacterTextSplitter use?
**Sub-prompt #13 Answer:** Overlap plus hierarchical boundaries

**Sub-prompt #14:** What separator handling approach does CharacterTextSplitter use?
**Sub-prompt #14 Answer:** Single separator

**Sub-prompt #15:** What separator handling approach does RecursiveCharacterTextSplitter use?
**Sub-prompt #15 Answer:** Hierarchical fallback
