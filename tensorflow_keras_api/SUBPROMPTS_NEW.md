# Sub-prompts for TensorFlow Keras API Design Analysis

This file contains atomic sub-prompts for each analytical criterion (C1-C19). Table criteria (C20-C44) are evaluated by checking table structure and cell values directly.

---

## Question 1: Constructor Complexity Progression

Sub-prompt #1: How many parameters without default values does Functional's constructor require?
Sub-prompt #1 Answer: 2

Sub-prompt #2: How many parameters without default values does Sequential's constructor require?
Sub-prompt #2 Answer: 0

Sub-prompt #3: What is the ratio of Functional's required parameters to Sequential's required parameters?
Sub-prompt #3 Answer: 2:0 (or infinity, or undefined)

Sub-prompt #4: Which specific parameter does Functional require that Sequential does not have?
Sub-prompt #4 Answer: outputs

---

## Question 2: Serialization Naming Consistency

Sub-prompt #5: How many serialization format pairs follow asymmetric or inconsistent naming patterns?
Sub-prompt #5 Answer: 1

Sub-prompt #6: What is the naming consistency ratio (consistent pairs : total pairs)?
Sub-prompt #6 Answer: 2:3

Sub-prompt #7: Which specific format pair breaks the "model_to_X / model_from_X" naming pattern?
Sub-prompt #7 Answer: config (uses get_config instead of model_to_config)

---

## Question 3: Parameter Default Strategy

Sub-prompt #8: How many Model.compile() parameters have explicit non-None default values?
Sub-prompt #8 Answer: 1 (optimizer='rmsprop')

Sub-prompt #9: How many Model.compile() parameters default to None?
Sub-prompt #9 Answer: 6 (loss, metrics, loss_weights, weighted_metrics, run_eagerly, steps_per_execution)

Sub-prompt #10: What is the ratio of explicit defaults to None defaults in compile()?
Sub-prompt #10 Answer: 1:6

Sub-prompt #11: Which compile() parameter accepts the most diverse type options?
Sub-prompt #11 Answer: optimizer

---

## Question 4: Inheritance Depth Tradeoff

Sub-prompt #12: What is Model's immediate parent class?
Sub-prompt #12 Answer: Layer (or base_layer.Layer)

Sub-prompt #13: How many direct parent classes does Model inherit from?
Sub-prompt #13 Answer: 1

Sub-prompt #14: How many inheritance levels separate Sequential from Python's base object class?
Sub-prompt #14 Answer: 7

Sub-prompt #15: How many inheritance levels separate Functional from Python's base object class?
Sub-prompt #15 Answer: 6

Sub-prompt #16: What is the inheritance depth difference between the simplest and most complex class?
Sub-prompt #16 Answer: 2

---

## Question 5: API Surface Comparison Table

Note: Question 5 requires a table with 5 columns and 3 rows. The table criteria (C17-C44) are evaluated by checking:
- Table structure (presence, column count, row count, headers, ordering)
- Individual cell values (class names, parameter counts, inheritance depths, use cases)

These are verified directly against the expected table structure and not broken into separate sub-prompts, as they represent a single coherent table generation task.

---

## Criteria Mapping Summary

- **C1**: Sub-prompt #1 (Functional required parameters)
- **C2**: Sub-prompt #2 (Sequential required parameters)
- **C3**: Sub-prompt #3 (Parameter ratio)
- **C4**: Sub-prompt #4 (Outputs parameter)
- **C5**: Sub-prompt #5 (Inconsistent pairs count)
- **C6**: Sub-prompt #6 (Consistency ratio)
- **C7**: Sub-prompt #7 (Config pair)
- **C8**: Sub-prompt #8 (Explicit non-None defaults)
- **C9**: Sub-prompt #9 (None defaults)
- **C10**: Sub-prompt #10 (Defaults ratio)
- **C11**: Sub-prompt #11 (Most permissive parameter)
- **C12**: Sub-prompt #12 (Model parent class)
- **C13**: Sub-prompt #13 (Multiple inheritance count)
- **C14**: Sub-prompt #14 (Sequential depth)
- **C15**: Sub-prompt #15 (Functional depth)
- **C16**: Sub-prompt #16 (Depth difference)
- **C17-C44**: Table structure and cell values (evaluated holistically)

Total analytical sub-prompts: 16
Total table criteria: 28
**Total criteria: 44**
