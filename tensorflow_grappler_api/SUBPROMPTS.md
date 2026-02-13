# Sub-prompts for TensorFlow Grappler API Design Analysis

This file contains atomic sub-prompts for each analytical criterion (C1-C19). Each sub-prompt corresponds to a specific verifiable answer from the codebase.

---

## Question 1: Wrapper Implementation Strategy

Sub-prompt #1: What is the actual imported module name in the Python Item class?
Sub-prompt #1 Answer: \_pywrap_tf_item

Sub-prompt #2: What is the name of the private instance variable that stores the underlying C++ wrapper object in the Python Item class?
Sub-prompt #2 Answer: \_tf_item

Sub-prompt #3: What is the function name from the imported module that constructs the C++ wrapper object in the Python Item class?
Sub-prompt #3 Answer: TF_NewItem

Sub-prompt #4: What is the property name that provides access to the C++ wrapper object in the Python Item class?
Sub-prompt #4 Answer: tf_item

Sub-prompt #5: How many public methods in the Item class delegate to functions from the imported module?
Sub-prompt #5 Answer: 3

---

## Question 2: Conditional Construction Pattern

Sub-prompt #6: What is the actual imported module name in the Python Cluster class?
Sub-prompt #6 Answer: \_pywrap_tf_cluster

Sub-prompt #7: Which constructor parameter controls the conditional branching in the Cluster class?
Sub-prompt #7 Answer: devices

Sub-prompt #8: What is the first function name used to construct C++ cluster wrapper objects in the Cluster constructor?
Sub-prompt #8 Answer: TF_NewCluster

Sub-prompt #9: What is the second function name used to construct C++ cluster wrapper objects in the Cluster constructor?
Sub-prompt #9 Answer: TF_NewVirtualCluster

---

## Question 3: Method Overloading and Override Strategy

Sub-prompt #10: What is the first unique pure virtual method name in GraphOptimizer?
Sub-prompt #10 Answer: name

Sub-prompt #11: What is the second unique pure virtual method name in GraphOptimizer?
Sub-prompt #11 Answer: UsesFunctionLibrary

Sub-prompt #12: What is the third unique pure virtual method name in GraphOptimizer?
Sub-prompt #12 Answer: Optimize

Sub-prompt #13: How many Optimize method overloads exist in the GraphOptimizer class?
Sub-prompt #13 Answer: 2

Sub-prompt #14: What is the GrapplerItem parameter type for the pure virtual Optimize overload?
Sub-prompt #14 Answer: const GrapplerItem&

Sub-prompt #15: What is the GrapplerItem parameter type for the Optimize overload that provides a default implementation?
Sub-prompt #15 Answer: GrapplerItem&&

---

## Question 4: Conditional Resource Management Pattern

Sub-prompt #16: What is the module-level variable that controls which optimization method is selected in OptimizeGraph?
Sub-prompt #16 Answer: is_oss

Sub-prompt #17: What is the first optimization method name that can be called based on the module-level variable's value?
Sub-prompt #17 Answer: TF_OptimizeGraphSerialized

Sub-prompt #18: What is the second optimization method name that can be called based on the module-level variable's value?
Sub-prompt #18 Answer: TF_OptimizeGraph

Sub-prompt #19: What is the method name called to cleanup the temporary cluster in OptimizeGraph?
Sub-prompt #19 Answer: Shutdown

Sub-prompt #20: What is the control structure block where the cleanup call appears?
Sub-prompt #20 Answer: finally

Sub-prompt #21: What is the name of the module-level threading synchronization primitive used in OptimizeGraph?
Sub-prompt #21 Answer: _OPTIMIZE_GRAPH_CLUSTER_LOCK

---

## Question 5: Python Wrapper Inheritance Pattern

Note: Question 5 requires a table with 3 columns and 3 rows. Table criteria are documented separately in TABLE_CRITERIA.md.

---

## Criteria Mapping Summary

**Analytical Criteria (C1-C19):**

- **C1**: Sub-prompt #1 (Imported module in Item = \_pywrap_tf_item)
- **C2**: Sub-prompt #2 (Private variable in Item = \_tf_item)
- **C3**: Sub-prompt #3 (Constructor function = TF_NewItem)
- **C4**: Sub-prompt #4 (Imported module in Cluster = \_pywrap_tf_cluster)
- **C5**: Sub-prompt #5 (Conditional parameter = devices)
- **C6**: Sub-prompt #6 (First constructor function = TF_NewCluster)
- **C7**: Sub-prompt #7 (Second constructor function = TF_NewVirtualCluster)
- **C8**: Sub-prompt #8 (First pure virtual method = name)
- **C9**: Sub-prompt #9 (Second pure virtual method = UsesFunctionLibrary)
- **C10**: Sub-prompt #10 (Third pure virtual method = Optimize)
- **C11**: Sub-prompt #11 (Optimize overload count = 2)
- **C12**: Sub-prompt #12 (Pure virtual parameter type = const GrapplerItem&)
- **C13**: Sub-prompt #13 (Default impl parameter type = GrapplerItem&&)
- **C14**: Sub-prompt #14 (Control variable = is_oss)
- **C15**: Sub-prompt #15 (First method name = TF_OptimizeGraphSerialized)
- **C16**: Sub-prompt #16 (Second method name = TF_OptimizeGraph)
- **C17**: Sub-prompt #17 (Cleanup method = Shutdown)
- **C18**: Sub-prompt #18 (Control block = finally)
- **C19**: Sub-prompt #19 (Table presence = Yes)

**Table Criteria (C20-C29):**

- **C20**: Table presence
- **C21**: Table has 3 columns
- **C22**: Table has 3 data rows
- **C23**: Row 1 - Component name (includes GrapplerItem/Item)
- **C24**: Row 1 - C++ Base Class
- **C25**: Row 1 - Python Base Class
- **C26**: Row 2 - Component name
- **C27**: Row 2 - C++ Base Class
- **C28**: Row 2 - Python Base Class
- **C29**: Row 3 - Component name
- **C30**: Row 3 - C++ Base Class
- **C31**: Row 3 - Python Base Class

**Total analytical sub-prompts: 21**
- Q1: 5 sub-prompts (C1-C5)
- Q2: 4 sub-prompts (C6-C9)
- Q3: 6 sub-prompts (C10-C15)
- Q4: 6 sub-prompts (C16-C21)
- Q5: Table with 14 criteria documented in TABLE_CRITERIA.md

**Grand Total: 35 criteria** (21 analytical + 14 table)
