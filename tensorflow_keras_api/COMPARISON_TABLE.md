# API Surface Comparison Table Reference

This table shows the correct values for all 15 cells (3 rows × 5 columns) for Question 5.

| Class Name | Required Parameters | Optional Parameters | Inheritance Depth | Primary Use Case |
|:-----------|:-------------------|:-------------------|:-----------------|:-----------------|
| Functional | 2 | 2 | 6 | Graph Models |
| Model | 0 | Variable | 5 | Base Abstraction |
| Sequential | 0 | 2 | 7 | Linear Models |

## Cell-by-Cell Breakdown

**Row 1 (Functional):**
- C17: Class Name = "Functional"
- C18: Required Parameters = 2 (inputs, outputs)
- C19: Optional Parameters = 2 (name=None, trainable=True)
- C20: Inheritance Depth = 6 (Functional → Model → Layer → Module → AutoTrackable → Trackable → object)
- C21: Primary Use Case = "Graph Models" (or "Complex Architectures", "DAG Models")

**Row 2 (Model):**
- C22: Class Name = "Model"
- C23: Required Parameters = 0 (*args/**kwargs - flexible, context-dependent)
- C24: Optional Parameters = Variable (depends on usage context)
- C25: Inheritance Depth = 5 (Model → Layer → Module → AutoTrackable → Trackable → object)
- C26: Primary Use Case = "Base Abstraction" (or "Foundation Class")

**Row 3 (Sequential):**
- C27: Class Name = "Sequential"
- C28: Required Parameters = 0 (layers=None, name=None)
- C29: Optional Parameters = 2 (layers, name)
- C30: Inheritance Depth = 7 (Sequential → Functional → Model → Layer → Module → AutoTrackable → Trackable → object)
- C31: Primary Use Case = "Linear Models" (or "Simple Stacks", "Sequential Architectures")

## Table Structure Requirements

- **Total columns**: 5 (Class Name, Required Parameters, Optional Parameters, Inheritance Depth, Primary Use Case)
- **Total data rows**: 3 (Functional, Model, Sequential)
- **Row ordering**: Alphabetical by Class Name
- **Introduction**: Must describe structure (column count, row count, column names, alphabetical ordering)
