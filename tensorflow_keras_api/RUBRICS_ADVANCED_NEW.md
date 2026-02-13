# RUBRICS_ADVANCED - TensorFlow Keras Model API Design Analysis - 44 Criteria

## Overview
- **Total Criteria**: 44 (all positive)
- **Domain**: API Design - Keras Model Construction Interface Analysis
- **Repository**: tensorflow/tensorflow (keras models module)
- **Commit**: 56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449
- **Task Type**: Research & Analysis (Scratch Routing)

---

## CRITERION 1 [Accuracy]
**Description:** States 2 as Functional's required parameter count.
**Weight:** Minor
**Numerical Weight:** 5
**Rationale:** Source: "
```python
class Functional(training.Model):
  def __init__(self, inputs, outputs, name=None, trainable=True):
```
"
Functional's constructor has 2 required parameters without default values: inputs and outputs. The name and trainable parameters have default values (name=None, trainable=True), making them optional. This represents an API design tradeoff where developers must explicitly specify both input and output tensors, trading convenience for architectural clarity in graph construction.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/functional.py

## CRITERION 2 [Accuracy]
**Description:** States 0 as Sequential's required parameter count.
**Weight:** Minor
**Numerical Weight:** 5
**Rationale:** Source: "
```python
class Sequential(training.Model):
  def __init__(self, layers=None, name=None):
```
"
Sequential's constructor has 0 required parameters without default values. Both layers and name have default values (layers=None, name=None), making them optional. Developers can instantiate Sequential() with no arguments and add layers afterward using the add() method. This represents maximum convenience at the cost of requiring additional method calls.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/sequential.py

## CRITERION 3 [Accuracy]
**Description:** States 2:0 or infinity as the ratio of Functional's to Sequential's required parameters.
**Weight:** Major
**Numerical Weight:** 8
**Rationale:** Functional has 2 required parameters (inputs, outputs) while Sequential has 0 required parameters (layers=None, name=None). The ratio is 2:0. Since division by zero is undefined, this can also be expressed as "infinity" or "undefined" or "2:0" as the ratio representation. This reveals the API design tradeoff between explicit graph specification (Functional) and implicit construction (Sequential).
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/functional.py, https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/sequential.py

## CRITERION 4 [Accuracy]
**Description:** Identifies "outputs" as the parameter Functional requires that Sequential does not.
**Weight:** Major
**Numerical Weight:** 8
**Rationale:** Source (Functional): "
```python
def __init__(self, inputs, outputs, name=None, trainable=True):
```
"
Source (Sequential): "
```python
def __init__(self, layers=None, name=None):
```
"
Functional's constructor requires an outputs parameter that defines the output tensor(s) of the computational graph. Sequential completely lacks this parameter because it infers outputs implicitly from the last layer in the stack. This represents the API design tradeoff: Functional gains flexibility to define complex multi-output architectures at the cost of requiring explicit output specification, while Sequential prioritizes simplicity by implicitly determining outputs from layer ordering.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/functional.py, https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/sequential.py

## CRITERION 5 [Accuracy]
**Description:** States 1 as the count of serialization pairs following inconsistent naming patterns.
**Weight:** Minor
**Numerical Weight:** 5
**Rationale:** Sources: "
```python
def model_to_json(model, **kwargs):
def model_from_json(json_string, custom_objects=None):

def model_to_yaml(model, **kwargs):
def model_from_yaml(yaml_string, custom_objects=None):

def get_config(self):  # Model method
def model_from_config(config, custom_objects=None):
```
"
The JSON pair (model_to_json/model_from_json) follows the "model_to_X/model_from_X" pattern consistently. The YAML pair (model_to_yaml/model_from_yaml) follows the pattern consistently. However, the config pair breaks the pattern: the save function is get_config (not model_to_config), while the load function is model_from_config. Only 1 pair follows an inconsistent naming pattern.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/models.py, https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/training.py

## CRITERION 6 [Accuracy]
**Description:** States 2:3 as the naming consistency ratio (consistent pairs : total pairs).
**Weight:** Major
**Numerical Weight:** 8
**Rationale:** From Criterion 5, 2 pairs follow consistent naming (JSON, YAML) and 1 pair follows inconsistent naming (config). Total pairs = 3. The ratio of consistent pairs to total pairs is 2:3. This reveals the API design tradeoff between consistency (using uniform naming patterns) and legacy compatibility (preserving existing get_config method names).
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/models.py, https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/training.py

## CRITERION 7 [Accuracy]
**Description:** Identifies the "config" format pair as breaking the naming pattern.
**Weight:** Major
**Numerical Weight:** 8
**Rationale:** Source: "
```python
def get_config(self):  # Not model_to_config
def model_from_config(config, custom_objects=None):  # Follows pattern
```
"
The config serialization pair uses get_config for saving (not model_to_config) while using model_from_config for loading. This asymmetry breaks the "model_to_X/model_from_X" pattern that JSON and YAML follow. This violates the API design principle of consistency, likely due to legacy compatibility concerns where get_config was an established Model method before the serialization API was standardized.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/models.py, https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/training.py

## CRITERION 8 [Accuracy]
**Description:** States 1 as the count of compile() parameters with explicit non-None defaults.
**Weight:** Minor
**Numerical Weight:** 5
**Rationale:** Source: "
```python
def compile(self,
            optimizer='rmsprop',
            loss=None,
            metrics=None,
            loss_weights=None,
            weighted_metrics=None,
            run_eagerly=None,
            steps_per_execution=None,
            **kwargs):
```
"
Model.compile() has 1 parameter with explicit non-None default: optimizer='rmsprop'. All other parameters (loss, metrics, loss_weights, weighted_metrics, run_eagerly, steps_per_execution) default to None.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/training.py

## CRITERION 9 [Accuracy]
**Description:** States 6 as the count of compile() parameters defaulting to None.
**Weight:** Minor
**Numerical Weight:** 5
**Rationale:** From the signature in Criterion 8, the parameters defaulting to None are: loss=None, metrics=None, loss_weights=None, weighted_metrics=None, run_eagerly=None, steps_per_execution=None. That's 6 parameters with None defaults.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/training.py

## CRITERION 10 [Accuracy]
**Description:** States 1:6 as the ratio of explicit defaults to None defaults.
**Weight:** Major
**Numerical Weight:** 8
**Rationale:** Based on Criteria 8 and 9, there is 1 explicit non-None default (optimizer='rmsprop') and 6 None defaults (loss, metrics, loss_weights, weighted_metrics, run_eagerly, steps_per_execution). The ratio is 1:6. This reveals the API design philosophy of flexibility over type safety: most parameters default to None, allowing compile() to be called with minimal configuration while accepting diverse configuration strategies through None checks.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/training.py

## CRITERION 11 [Accuracy]
**Description:** Identifies "optimizer" as the parameter with the most permissive type signature.
**Weight:** Major
**Numerical Weight:** 8
**Rationale:** Source: "
```python
def compile(self,
            optimizer='rmsprop',
            ...):
  '''Arguments:
    optimizer: String (name of optimizer) or optimizer instance.
  '''
```
"
The optimizer parameter accepts the most distinct types: (1) string identifiers ('adam', 'sgd', 'rmsprop'), (2) Optimizer class instances, and (3) configuration dictionaries. This makes it the most permissive parameter in the signature. This represents the API design philosophy of flexibility vs type safety: accepting multiple input types increases convenience at the cost of runtime type checking complexity.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/training.py

## CRITERION 12 [Accuracy]
**Description:** States "Layer" or "base_layer.Layer" as Model's immediate parent class.
**Weight:** Minor
**Numerical Weight:** 5
**Rationale:** Source: "
```python
class Model(base_layer.Layer):
```
"
Model's immediate parent class is base_layer.Layer (or simply "Layer" in Keras). Model inherits from Layer to gain composability and configuration management. This design decision allows models to be used as layers within other models, enabling modular architecture composition.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/training.py

## CRITERION 13 [Accuracy]
**Description:** States 1 as Model's multiple inheritance count (number of direct parent classes).
**Weight:** Minor
**Numerical Weight:** 5
**Rationale:** Source: "
```python
class Model(base_layer.Layer):
```
"
Model inherits from 1 parent class: base_layer.Layer. This is single inheritance, not multiple inheritance. The multiple inheritance count is 1 (one parent). The API design uses single inheritance to maintain a clear hierarchy and avoid diamond inheritance complexity.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/training.py

## CRITERION 14 [Accuracy]
**Description:** States 7 as the inheritance depth for Sequential.
**Weight:** Minor
**Numerical Weight:** 5
**Rationale:** Source: "
```python
class Sequential(functional.Functional):
```
"
Sequential's full inheritance chain: Sequential → Functional → Model → Layer → Module → AutoTrackable → Trackable → object. Counting from object to Sequential, the inheritance depth is 7 levels.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/sequential.py

## CRITERION 15 [Accuracy]
**Description:** States 6 as the inheritance depth for Functional.
**Weight:** Minor
**Numerical Weight:** 5
**Rationale:** Source: "
```python
class Functional(training.Model):
```
"
Functional's full inheritance chain: Functional → Model → Layer → Module → AutoTrackable → Trackable → object. Counting from object to Functional, the inheritance depth is 6 levels.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/functional.py

## CRITERION 16 [Accuracy]
**Description:** States 2 as the inheritance depth difference between simplest and most complex class.
**Weight:** Major
**Numerical Weight:** 8
**Rationale:** Based on Criteria 14 and 15: Sequential has depth 7, Functional has depth 6, Model has depth 5 (Model → Layer → Module → AutoTrackable → Trackable → object). The difference between the deepest (Sequential at 7) and shallowest (Model at 5) is 2 levels. This reveals the API design tradeoff: code reuse through inheritance (Sequential/Functional reuse Model's functionality) vs complexity (deeper hierarchies are harder to understand).
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/training.py, https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/sequential.py, https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/functional.py

## CRITERION 17 [Accuracy]
**Description:** States "Functional" in the Class Name column (first row).
**Weight:** Minor
**Numerical Weight:** 7
**Rationale:** The table must display classes in alphabetical order. "Functional" is alphabetically first among (Functional, Model, Sequential), so it should appear in the first data row's Class Name column.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/functional.py

## CRITERION 18 [Accuracy]
**Description:** States 2 as Functional's Required Parameters count.
**Weight:** Minor
**Numerical Weight:** 7
**Rationale:** From Criterion 1, Functional has 2 required parameters: inputs and outputs.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/functional.py

## CRITERION 19 [Accuracy]
**Description:** States 2 as Functional's Optional Parameters count.
**Weight:** Minor
**Numerical Weight:** 7
**Rationale:** Source: "
```python
def __init__(self, inputs, outputs, name=None, trainable=True):
```
"
Functional has 2 optional parameters with default values: name=None and trainable=True.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/functional.py

## CRITERION 20 [Accuracy]
**Description:** States 6 as Functional's Inheritance Depth.
**Weight:** Minor
**Numerical Weight:** 7
**Rationale:** From Criterion 15, Functional's inheritance depth from object is 6 levels: Functional → Model → Layer → Module → AutoTrackable → Trackable → object.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/functional.py

## CRITERION 21 [Accuracy]
**Description:** States "Graph Models" as Functional's Primary Use Case.
**Weight:** Minor
**Numerical Weight:** 7
**Rationale:** Source: "
```python
class Functional(training.Model):
  '''A `Functional` model is a `Model` defined as a directed graph of layers.
```
"
Functional is designed for building directed acyclic graphs of layers, supporting complex architectures with multiple inputs/outputs and non-linear connections. The primary use case is "Graph Models" or "Complex Architectures" or "DAG Models".
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/functional.py

## CRITERION 22 [Accuracy]
**Description:** States "Model" in the Class Name column (second row).
**Weight:** Minor
**Numerical Weight:** 7
**Rationale:** Alphabetical order places Model second (Functional, Model, Sequential).
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/training.py

## CRITERION 23 [Accuracy]
**Description:** States 0 or 2 as Model's Required Parameters count.
**Weight:** Minor
**Numerical Weight:** 7
**Rationale:** Source: "
```python
class Model(base_layer.Layer):
  def __init__(self, *args, **kwargs):
```
"
Model's constructor uses flexible *args/**kwargs signature. When used functionally with inputs/outputs, it effectively requires 2 parameters. When subclassed, it requires 0 parameters. The answer depends on usage context, but typically 0 or 2.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/training.py

## CRITERION 24 [Accuracy]
**Description:** States the count of Model's Optional Parameters (variable based on *args/**kwargs).
**Weight:** Minor
**Numerical Weight:** 7
**Rationale:** Model's *args/**kwargs signature makes optional parameter counting context-dependent. When using functional API pattern, optional parameters might include name, trainable, etc. The count is variable/flexible.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/training.py

## CRITERION 25 [Accuracy]
**Description:** States 5 as Model's Inheritance Depth.
**Weight:** Minor
**Numerical Weight:** 7
**Rationale:** From Criterion 12, Model inherits from Layer. The chain is: Model → Layer → Module → AutoTrackable → Trackable → object. The depth is 5 levels.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/training.py

## CRITERION 26 [Accuracy]
**Description:** States "Base Abstraction" as Model's Primary Use Case.
**Weight:** Minor
**Numerical Weight:** 7
**Rationale:** Source: "
```python
class Model(base_layer.Layer):
  '''Model groups layers into an object with training and inference features.
```
"
Model serves as the base abstraction providing core training/inference functionality. It's the parent class for Sequential and Functional, defining the common interface. The primary use case is "Base Abstraction" or "Foundation Class".
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/training.py

## CRITERION 27 [Accuracy]
**Description:** States "Sequential" in the Class Name column (third row).
**Weight:** Minor
**Numerical Weight:** 7
**Rationale:** Alphabetical order places Sequential third and last (Functional, Model, Sequential).
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/sequential.py

## CRITERION 28 [Accuracy]
**Description:** States 0 as Sequential's Required Parameters count.
**Weight:** Minor
**Numerical Weight:** 7
**Rationale:** From Criterion 2, Sequential has 0 required parameters (layers=None, name=None).
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/sequential.py

## CRITERION 29 [Accuracy]
**Description:** States 2 as Sequential's Optional Parameters count.
**Weight:** Minor
**Numerical Weight:** 7
**Rationale:** Source: "
```python
def __init__(self, layers=None, name=None):
```
"
Sequential has 2 optional parameters with default values: layers=None and name=None.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/sequential.py

## CRITERION 30 [Accuracy]
**Description:** States 7 as Sequential's Inheritance Depth.
**Weight:** Minor
**Numerical Weight:** 7
**Rationale:** From Criterion 14, Sequential's inheritance depth from object is 7 levels: Sequential → Functional → Model → Layer → Module → AutoTrackable → Trackable → object.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/sequential.py

## CRITERION 31 [Accuracy]
**Description:** States "Linear Models" as Sequential's Primary Use Case.
**Weight:** Minor
**Numerical Weight:** 7
**Rationale:** Source: "
```python
class Sequential(training.Model):
  '''Sequential groups a linear stack of layers into a `tf.keras.Model`.
```
"
Sequential is designed for linear layer stacking where data flows sequentially through layers without branching. The primary use case is "Linear Models" or "Simple Stacks" or "Sequential Architectures".
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/engine/sequential.py

## CRITERION 32 [Table Structure]
**Description:** Includes a comparison table in the response.
**Weight:** Critical
**Numerical Weight:** 4
**Rationale:** The prompt explicitly requires: "Create a comparison table with exactly 5 columns..." The response must include a table in markdown format to satisfy this requirement.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 33 [Table Structure]
**Description:** States that the table has exactly 5 columns.
**Weight:** Major
**Numerical Weight:** 3
**Rationale:** The prompt specifies: "Create a comparison table with exactly 5 columns: 'Class Name', 'Required Parameters', 'Optional Parameters', 'Inheritance Depth', 'Primary Use Case'." The table must have precisely 5 columns.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 34 [Table Structure]
**Description:** States that the table has exactly 3 data rows.
**Weight:** Major
**Numerical Weight:** 3
**Rationale:** The prompt specifies: "Include exactly 3 data rows (Functional, Model, Sequential)". The table must have exactly 3 data rows plus the header row.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 35 [Table Structure]
**Description:** States "Class Name" as the first column header.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt requires: "Class Name" as the first of 5 columns in the specified order.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 36 [Table Structure]
**Description:** States "Required Parameters" as the second column header.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt requires: "Required Parameters" as the second column header.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 37 [Table Structure]
**Description:** States "Optional Parameters" as the third column header.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt requires: "Optional Parameters" as the third column header.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 38 [Table Structure]
**Description:** States "Inheritance Depth" as the fourth column header.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt requires: "Inheritance Depth" as the fourth column header.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 39 [Table Structure]
**Description:** States "Primary Use Case" as the fifth column header.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt requires: "Primary Use Case" as the fifth column header.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 40 [Table Structure]
**Description:** Includes rows in alphabetical order (Functional, Model, Sequential).
**Weight:** Major
**Numerical Weight:** 4
**Rationale:** The prompt explicitly requires: "in alphabetical order". The table rows must appear in the sequence: Functional, Model, Sequential.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 41 [Table Structure]
**Description:** Includes an introduction before the table describing its structure.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** The prompt requires: "Before the table, describe its structure (column count, row count, column names, and ordering)." An introduction paragraph must appear immediately before the table.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 42 [Table Structure]
**Description:** States the number of columns (5) in the table introduction.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The introduction must explicitly state: "5 columns" or equivalent phrasing. This is one of the required elements from the prompt.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 43 [Table Structure]
**Description:** States the number of rows (3) in the table introduction.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The introduction must explicitly state: "3 rows" or "3 data rows" or equivalent phrasing.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 44 [Table Structure]
**Description:** Lists column names and describes alphabetical ordering in the introduction.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The introduction must: (1) list the 5 column names, and (2) describe alphabetical organization. These are required elements from the prompt.
**Sources:** N/A (structural requirement from prompt)
