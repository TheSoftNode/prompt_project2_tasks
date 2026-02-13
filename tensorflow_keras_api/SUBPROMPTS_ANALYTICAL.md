# SUBPROMPTS - Analytical Questions (Excluding Table)
## TensorFlow Keras API Design Analysis - Commit 56e5f82

---

**Sub-prompt #1:** What is Functional's required parameter count?
**Sub-prompt #1 Answer:** 2

**Sub-prompt #2:** What is Sequential's required parameter count?
**Sub-prompt #2 Answer:** 0

**Sub-prompt #3:** What is the ratio of Functional's required parameters to Sequential's required parameters?
**Sub-prompt #3 Answer:** 2:0

**Sub-prompt #4:** What parameter does Functional require that Sequential does not?
**Sub-prompt #4 Answer:** outputs

**Sub-prompt #5:** How many serialization format pairs follow inconsistent naming patterns?
**Sub-prompt #5 Answer:** 1

**Sub-prompt #6:** What is the naming consistency ratio (consistent pairs : total pairs)?
**Sub-prompt #6 Answer:** 2:3

**Sub-prompt #7:** Which format pair breaks the naming pattern?
**Sub-prompt #7 Answer:** config

**Sub-prompt #8:** How many compile() parameters have explicit non-None defaults?
**Sub-prompt #8 Answer:** 1

**Sub-prompt #9:** How many compile() parameters default to None?
**Sub-prompt #9 Answer:** 6

**Sub-prompt #10:** What is the ratio of explicit defaults to None defaults?
**Sub-prompt #10 Answer:** 1:6

**Sub-prompt #11:** Which parameter has the most permissive type signature?
**Sub-prompt #11 Answer:** optimizer

**Sub-prompt #12:** What is Model's immediate parent class?
**Sub-prompt #12 Answer:** Layer

**Sub-prompt #13:** How many parent classes does Model inherit from?
**Sub-prompt #13 Answer:** 1

**Sub-prompt #14:** What is Sequential's inheritance depth?
**Sub-prompt #14 Answer:** 7

**Sub-prompt #15:** What is Functional's inheritance depth?
**Sub-prompt #15 Answer:** 6

**Sub-prompt #16:** What is the inheritance depth difference between the simplest and most complex class?
**Sub-prompt #16 Answer:** 2
