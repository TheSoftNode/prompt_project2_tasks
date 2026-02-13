# RUBRICS_ADVANCED - TensorFlow Keras Optimizer Analysis - 40 Criteria

## Overview
- **Total Criteria**: 40 (all positive)
- **Domain**: Code Repository Documentation - Optimizer Implementation Analysis  
- **Repository**: tensorflow/tensorflow (keras optimizer_v2 module)
- **Commit**: 56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449
- **Task Type**: Research & Analysis (Scratch Routing)

---

## CRITERION 1 [Accuracy]
**Description:** States "OptimizerV2" as the base class name.
**Weight:** Major
**Numerical Weight:** 8
**Rationale:** Source: "
```python
class OptimizerV2(trackable.Trackable):
  """Base class for Keras optimizers.

  You should not use this class directly, but instead instantiate one of its
  subclasses such as `tf.keras.optimizers.SGD`, `tf.keras.optimizers.Adam`, etc.
```
"
The optimizer_v2 module contains `OptimizerV2` as the base class that all optimizer implementations inherit from. This class is defined in optimizer_v2.py and provides core optimization functionality including variable tracking, gradient application, and configuration management. All four analyzed optimizers (Adam, SGD, Adagrad, RMSprop) inherit directly from this base class.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/optimizer_v2.py

## CRITERION 2 [Accuracy]
**Description:** Identifies 1 as the count of abstract methods in OptimizerV2.
**Weight:** Major
**Numerical Weight:** 8
**Rationale:** Source: "
```python
  @abc.abstractmethod
  def get_config(self):
    """Returns the config of the optimizer.

    An optimizer config is a Python dictionary (serializable)
    containing the configuration of an optimizer.
```
"
The OptimizerV2 base class defines exactly 1 abstract method decorated with `@abc.abstractmethod`: the `get_config` method. This is the only method that subclasses MUST implement to satisfy the inheritance contract. This method enables optimizer serialization by returning a Python dictionary containing the optimizer's configuration, allowing optimizers to be saved and restored.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/optimizer_v2.py

## CRITERION 3 [Accuracy]
**Description:** Counts Adam's optimizer-specific parameters correctly (5 parameters).
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source: "
```python
  def __init__(self,
               learning_rate=0.001,
               beta_1=0.9,
               beta_2=0.999,
               epsilon=1e-7,
               amsgrad=False,
               name='Adam',
               **kwargs):
```
"
Adam's `__init__` method defines 5 optimizer-specific parameters (excluding `name` and `**kwargs` as instructed): learning_rate, beta_1, beta_2, epsilon, and amsgrad. These parameters control the Adam optimization algorithm's behavior including learning rate, first moment decay, second moment decay, numerical stability epsilon, and whether to use the AMSGrad variant.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adam.py

## CRITERION 4 [Accuracy]
**Description:** Counts SGD's optimizer-specific parameters correctly (3 parameters).
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source: "
```python
  def __init__(self,
               learning_rate=0.01,
               momentum=0.0,
               nesterov=False,
               name="SGD",
               **kwargs):
```
"
SGD's `__init__` method defines 3 optimizer-specific parameters (excluding `name` and `**kwargs`): learning_rate, momentum, and nesterov. These parameters control the stochastic gradient descent algorithm including the step size, velocity accumulation factor, and whether to use Nesterov momentum.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/gradient_descent.py

## CRITERION 5 [Accuracy]
**Description:** Counts Adagrad's optimizer-specific parameters correctly (3 parameters).
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source: "
```python
  def __init__(self,
               learning_rate=0.001,
               initial_accumulator_value=0.1,
               epsilon=1e-7,
               name='Adagrad',
               **kwargs):
```
"
Adagrad's `__init__` method defines 3 optimizer-specific parameters (excluding `name` and `**kwargs`): learning_rate, initial_accumulator_value, and epsilon. These parameters control the Adagrad algorithm's adaptive learning rate mechanism, including the base learning rate, the starting value for gradient accumulators (preventing division by zero), and numerical stability epsilon.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adagrad.py

## CRITERION 6 [Accuracy]
**Description:** Counts RMSprop's optimizer-specific parameters correctly (5 parameters).
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source: "
```python
  def __init__(self,
               learning_rate=0.001,
               rho=0.9,
               momentum=0.0,
               epsilon=1e-7,
               centered=False,
               name="RMSprop",
               **kwargs):
```
"
RMSprop's `__init__` method defines 5 optimizer-specific parameters (excluding `name` and `**kwargs`): learning_rate, rho, momentum, epsilon, and centered. These parameters control the RMSprop algorithm including base learning rate, the decay rate for the moving average of squared gradients, optional momentum, numerical stability epsilon, and whether to use centered RMSprop variant.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/rmsprop.py

## CRITERION 7 [Accuracy]
**Description:** Determines Adam or RMSprop has the highest parameter count.
**Weight:** Major
**Numerical Weight:** 8
**Rationale:** Based on the parameter counts from Criteria 3-6:
- Adam: 5 parameters (learning_rate, beta_1, beta_2, epsilon, amsgrad)
- SGD: 3 parameters (learning_rate, momentum, nesterov)
- Adagrad: 3 parameters (learning_rate, initial_accumulator_value, epsilon)
- RMSprop: 5 parameters (learning_rate, rho, momentum, epsilon, centered)

Both Adam and RMSprop tie with 5 optimizer-specific parameters each, making them the most complex configurations. Either answer ("Adam" or "RMSprop") is correct.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adam.py, https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/rmsprop.py

## CRITERION 8 [Accuracy]
**Description:** Identifies "beta_1" as Adam's first moment decay parameter name.
**Weight:** Major  
**Numerical Weight:** 8
**Rationale:** Source: "
```python
  def __init__(self,
               learning_rate=0.001,
               beta_1=0.9,
               beta_2=0.999,
               epsilon=1e-7,
               amsgrad=False,
               name='Adam',
               **kwargs):
```
"
Adam's `__init__` method includes `beta_1=0.9` as the parameter controlling the exponential decay rate for the first moment estimates (the moving average of gradients). This parameter name is specific to Adam and differs from RMSprop's `rho` parameter despite both controlling moving averages. The name `beta_1` comes from the original Adam paper by Kingma and Ba (2014).
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adam.py, https://arxiv.org/abs/1412.6980

## CRITERION 9 [Accuracy]
**Description:** Identifies 0.0 as SGD's acceleration parameter (momentum) default value.
**Weight:** Major
**Numerical Weight:** 8
**Rationale:** Source: "
```python
  def __init__(self,
               learning_rate=0.01,
               momentum=0.0,
               nesterov=False,
               name="SGD",
               **kwargs):
```
"
SGD's `__init__` signature shows `momentum=0.0` as the default value for its acceleration parameter. With this default of 0.0, SGD performs vanilla gradient descent without any velocity accumulation. Only when momentum is set to a value greater than 0 does SGD incorporate velocity-based acceleration.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/gradient_descent.py

## CRITERION 10 [Accuracy]
**Description:** Identifies 0.1 as Adagrad's initial_accumulator_value default.
**Weight:** Major
**Numerical Weight:** 8
**Rationale:** Source: "
```python
  def __init__(self,
               learning_rate=0.001,
               initial_accumulator_value=0.1,
               epsilon=1e-7,
               name='Adagrad',
               **kwargs):
```
"
Adagrad's `__init__` shows `initial_accumulator_value=0.1` as the default. This parameter sets the starting value for the per-parameter gradient accumulators, preventing division by zero during the first optimization steps. The positive initialization (0.1) ensures numerical stability at the start of training when accumulated squared gradients would otherwise be zero.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adagrad.py

## CRITERION 11 [Accuracy]
**Description:** Calculates 1:10 (or 0.001:0.01 or 0.1) as the learning rate ratio.
**Weight:** Major
**Numerical Weight:** 8
**Rationale:** Sources show:
- Adam: `learning_rate=0.001`
- Adagrad: `learning_rate=0.001`
- RMSprop: `learning_rate=0.001`  
- SGD: `learning_rate=0.01`

Three optimizers (Adam, Adagrad, RMSprop) share a common default of 0.001, while SGD uses a different default of 0.01. The ratio is: 0.001 / 0.01 = 1/10 = 1:10. This can also be expressed as 0.001:0.01 or as the decimal 0.1.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adam.py, https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adagrad.py, https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/rmsprop.py, https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/gradient_descent.py

## CRITERION 12 [Accuracy]
**Description:** Adam row - Optimizer column contains "Adam".
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** The table must display optimizers in alphabetical order. "Adam" is alphabetically first among (Adam, Adagrad, RMSprop, SGD), so it should appear in the first data row's Optimizer column.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adam.py

## CRITERION 13 [Accuracy]
**Description:** Adam row - Default Learning Rate column contains 0.001.
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Source: "
```python
  def __init__(self,
               learning_rate=0.001,
```
"
Adam's `__init__` method shows `learning_rate=0.001` as the default value.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adam.py

## CRITERION 14 [Accuracy]
**Description:** Adam row - Uses Momentum column contains "No".
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Source: "
```python
  def __init__(self,
               learning_rate=0.001,
               beta_1=0.9,
               beta_2=0.999,
               epsilon=1e-7,
               amsgrad=False,
               name='Adam',
               **kwargs):
```
"
Adam does not have a `momentum` parameter in its `__init__` signature. The prompt specifies: "state 'Yes' only if the optimizer has a momentum parameter with a non-zero default value, otherwise 'No'". Since Adam lacks a momentum parameter entirely, the answer is "No".
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adam.py

## CRITERION 15 [Accuracy]
**Description:** Adam row - Adaptive Learning Rate column contains "Yes".
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Adam implements per-parameter adaptive learning rates by maintaining first and second moment estimates (moving averages of gradients and squared gradients) for each parameter. The prompt states: "state 'Yes' if the optimizer adapts learning rates per parameter (like Adam, Adagrad, RMSprop do)". Adam is explicitly listed as an adaptive optimizer.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adam.py, https://www.tensorflow.org/api_docs/python/tf/keras/optimizers, https://arxiv.org/abs/1412.6980

## CRITERION 16 [Accuracy]
**Description:** Adam row - Hyperparameter Count column contains 5.
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** From Criterion 3, Adam has 5 optimizer-specific parameters: learning_rate, beta_1, beta_2, epsilon, amsgrad (excluding `name` and `**kwargs` as instructed).
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adam.py

## CRITERION 17 [Accuracy]
**Description:** Adagrad row - Optimizer column contains "Adagrad".
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Alphabetical order places Adagrad second (Adam, Adagrad, RMSprop, SGD).
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adagrad.py

## CRITERION 18 [Accuracy]
**Description:** Adagrad row - Default Learning Rate column contains 0.001.
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Source: "
```python
  def __init__(self,
               learning_rate=0.001,
```
"
Adagrad's `__init__` method shows `learning_rate=0.001` as the default value.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adagrad.py

## CRITERION 19 [Accuracy]
**Description:** Adagrad row - Uses Momentum column contains "No".
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Source: "
```python
  def __init__(self,
               learning_rate=0.001,
               initial_accumulator_value=0.1,
               epsilon=1e-7,
               name='Adagrad',
               **kwargs):
```
"
Adagrad does not have a `momentum` parameter in its `__init__` signature, so the answer is "No".
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adagrad.py

## CRITERION 20 [Accuracy]
**Description:** Adagrad row - Adaptive Learning Rate column contains "Yes".
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Adagrad implements per-parameter adaptive learning rates by accumulating squared gradients for each parameter individually. The prompt explicitly lists Adagrad as an adaptive optimizer: "like Adam, Adagrad, RMSprop do".
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adagrad.py, https://www.tensorflow.org/api_docs/python/tf/keras/optimizers

## CRITERION 21 [Accuracy]
**Description:** Adagrad row - Hyperparameter Count column contains 3.
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** From Criterion 5, Adagrad has 3 optimizer-specific parameters: learning_rate, initial_accumulator_value, epsilon.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adagrad.py

## CRITERION 22 [Accuracy]
**Description:** RMSprop row - Optimizer column contains "RMSprop".
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Alphabetical order places RMSprop third (Adam, Adagrad, RMSprop, SGD).
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/rmsprop.py

## CRITERION 23 [Accuracy]
**Description:** RMSprop row - Default Learning Rate column contains 0.001.
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Source: "
```python
  def __init__(self,
               learning_rate=0.001,
```
"
RMSprop's `__init__` method shows `learning_rate=0.001` as the default value.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/rmsprop.py

## CRITERION 24 [Accuracy]
**Description:** RMSprop row - Uses Momentum column contains "No".
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Source: "
```python
  def __init__(self,
               learning_rate=0.001,
               rho=0.9,
               momentum=0.0,
```
"
While RMSprop HAS a `momentum` parameter, its default value is `momentum=0.0`. The prompt requires: "state 'Yes' only if the optimizer has a momentum parameter with a non-zero default value". Since the default is 0.0, the answer is "No".
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/rmsprop.py

## CRITERION 25 [Accuracy]
**Description:** RMSprop row - Adaptive Learning Rate column contains "Yes".
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** RMSprop implements per-parameter adaptive learning rates by maintaining a moving average of squared gradients for each parameter. The prompt explicitly lists RMSprop as an adaptive optimizer: "like Adam, Adagrad, RMSprop do".
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/rmsprop.py, https://www.tensorflow.org/api_docs/python/tf/keras/optimizers

## CRITERION 26 [Accuracy]
**Description:** RMSprop row - Hyperparameter Count column contains 5.
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** From Criterion 6, RMSprop has 5 optimizer-specific parameters: learning_rate, rho, momentum, epsilon, centered.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/rmsprop.py

## CRITERION 27 [Accuracy]
**Description:** SGD row - Optimizer column contains "SGD".
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Alphabetical order places SGD fourth and last (Adam, Adagrad, RMSprop, SGD).
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/gradient_descent.py

## CRITERION 28 [Accuracy]
**Description:** SGD row - Default Learning Rate column contains 0.01.
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Source: "
```python
  def __init__(self,
               learning_rate=0.01,
```
"
SGD's `__init__` method shows `learning_rate=0.01` as the default value (10x higher than the other three optimizers).
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/gradient_descent.py

## CRITERION 29 [Accuracy]
**Description:** SGD row - Uses Momentum column contains "No".
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Source: "
```python
  def __init__(self,
               learning_rate=0.01,
               momentum=0.0,
```
"
While SGD HAS a `momentum` parameter, its default value is `momentum=0.0`. Since the prompt requires a non-zero default for "Yes", the answer is "No".
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/gradient_descent.py

## CRITERION 30 [Accuracy]
**Description:** SGD row - Adaptive Learning Rate column contains "No".
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** SGD uses a single global learning rate applied uniformly to all parameters. It does not maintain parameter-specific statistics or adapt learning rates per parameter. The prompt specifies: "otherwise 'No' for fixed global rates". SGD uses a fixed global rate.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/gradient_descent.py, https://www.tensorflow.org/api_docs/python/tf/keras/optimizers

## CRITERION 31 [Accuracy]
**Description:** SGD row - Hyperparameter Count column contains 3.
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** From Criterion 4, SGD has 3 optimizer-specific parameters: learning_rate, momentum, nesterov.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/gradient_descent.py

## CRITERION 32 [Table Structure]
**Description:** Response includes a comparison table.
**Weight:** Critical
**Numerical Weight:** 4
**Rationale:** The prompt explicitly requires: "Create a comparison table analyzing the architectural and behavioral characteristics of all four optimizers." The response must include a table in markdown format to satisfy this requirement. Without a table, the response fails to complete the assigned task.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 33 [Table Structure]
**Description:** Table has exactly 5 columns.
**Weight:** Major
**Numerical Weight:** 2
**Rationale:** The prompt specifies: "The table must include exactly 5 columns with these headers in this exact order: 'Optimizer', 'Default Learning Rate', 'Uses Momentum', 'Adaptive Learning Rate', 'Hyperparameter Count'". The table must have precisely 5 columns, no more and no less.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 34 [Table Structure]
**Description:** Table has exactly 4 data rows (excluding header).
**Weight:** Major
**Numerical Weight:** 2
**Rationale:** The prompt specifies: "Include exactly 4 data rows (one per optimizer)". Since there are 4 optimizers being analyzed (Adam, SGD, Adagrad, RMSprop), the table must have exactly 4 data rows plus the header row.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 35 [Table Structure]
**Description:** Table displays optimizers in alphabetical order.
**Weight:** Major
**Numerical Weight:** 4
**Rationale:** The prompt requires: "in alphabetical order by optimizer name". The correct alphabetical order is: Adam, Adagrad, RMSprop, SGD. The table rows must appear in this exact sequence.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 36 [Table Structure]
**Description:** Column headers match exactly and appear in the correct order.
**Weight:** Major
**Numerical Weight:** 2
**Rationale:** The prompt specifies headers "in this exact order": (1) "Optimizer", (2) "Default Learning Rate", (3) "Uses Momentum", (4) "Adaptive Learning Rate", (5) "Hyperparameter Count". The headers must match these names exactly (case-insensitive) and appear in this precise sequence from left to right.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 37 [Table Structure]
**Description:** Response provides a brief introduction before the table.
**Weight:** Major
**Numerical Weight:** 4
**Rationale:** The prompt requires: "Before presenting the table, provide a brief introduction that states the number of columns, the number of rows, lists the column names, and describes how the rows are organized." An introduction paragraph must appear immediately before the table.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 38 [Table Structure]
**Description:** Table introduction states the number of columns.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The introduction must explicitly state: "5 columns" or equivalent phrasing like "consists of 5 columns" or "includes 5 columns". This is one of the four required elements listed in the prompt.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 39 [Table Structure]
**Description:** Table introduction states the number of rows.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The introduction must explicitly state: "4 rows" or equivalent phrasing like "consists of 4 rows" or "includes 4 data rows". This is one of the four required elements listed in the prompt.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 40 [Table Structure]
**Description:** Table introduction lists column names and describes alphabetical organization.
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** The introduction must: (1) list the column names (all 5: Optimizer, Default Learning Rate, Uses Momentum, Adaptive Learning Rate, Hyperparameter Count), and (2) describe how rows are organized (alphabetically by optimizer name). These are the remaining two required elements from the prompt's four-part introduction requirement.
**Sources:** N/A (structural requirement from prompt)
