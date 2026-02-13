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
**Description:** States 1 as the count of abstract methods in OptimizerV2.
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
**Description:** States 5 as Adam's optimizer-specific parameter count.
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
**Description:** States 3 as SGD's optimizer-specific parameter count.
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
**Description:** States 3 as Adagrad's optimizer-specific parameter count.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** Source 1 (TensorFlow implementation): "
```python
  def __init__(self,
               learning_rate=0.001,
               initial_accumulator_value=0.1,
               epsilon=1e-7,
               name='Adagrad',
               **kwargs):
```
"
Source 2 (Adagrad paper): "We describe and analyze an algorithm for adaptively modifying the proximal function, which significantly simplifies setting a learning rate and results in regret guarantees that are provably as good as the best proximal function that can be chosen in hindsight."

Adagrad's `__init__` method defines 3 optimizer-specific parameters (excluding `name` and `**kwargs`): learning_rate, initial_accumulator_value, and epsilon. These parameters control the Adagrad algorithm's adaptive learning rate mechanism as described in Duchi et al. (2011), including the base learning rate, the starting value for gradient accumulators (preventing division by zero), and numerical stability epsilon.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adagrad.py, https://jmlr.org/papers/v12/duchi11a.html

## CRITERION 6 [Accuracy]
**Description:** States 5 as RMSprop's optimizer-specific parameter count.
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
**Description:** Identifies Adam or RMSprop as having the highest parameter count.
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
**Rationale:** Source 1 (TensorFlow implementation): "
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
Source 2 (Adam paper): "We introduce Adam, an algorithm for first-order gradient-based optimization of stochastic objective functions, based on adaptive estimates of lower-order moments."

Adam's `__init__` method includes `beta_1=0.9` as the parameter controlling the exponential decay rate for the first moment estimates (the moving average of gradients). The parameter naming convention (beta_1, beta_2) comes directly from the original Adam paper by Kingma and Ba (2014), which describes the algorithm as using "adaptive estimates of lower-order moments" where beta_1 controls the first moment estimate. This differs from RMSprop's `rho` parameter despite both controlling moving averages.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adam.py, https://arxiv.org/abs/1412.6980

## CRITERION 9 [Accuracy]
**Description:** States 0.0 as SGD's momentum parameter default value.
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
**Description:** States 0.1 as Adagrad's initial_accumulator_value default.
**Weight:** Major
**Numerical Weight:** 8
**Rationale:** Source 1 (TensorFlow implementation): "
```python
  def __init__(self,
               learning_rate=0.001,
               initial_accumulator_value=0.1,
               epsilon=1e-7,
               name='Adagrad',
               **kwargs):
```
"
Source 2 (Adagrad paper): "The algorithm maintains a per-coordinate learning rate that incorporates knowledge of the geometry of the data observed in earlier iterations. We show that the algorithm has a number of useful properties."

Adagrad's `__init__` shows `initial_accumulator_value=0.1` as the default. This parameter sets the starting value for the per-parameter gradient accumulators, preventing division by zero during the first optimization steps. The positive initialization (0.1) ensures numerical stability at the start of training when accumulated squared gradients would otherwise be zero, as described in the original Duchi et al. (2011) paper on adaptive subgradient methods.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adagrad.py, https://jmlr.org/papers/v12/duchi11a.html

## CRITERION 11 [Accuracy]
**Description:** States 1:10 (or 0.001:0.01 or 0.1) as the learning rate ratio.
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
**Description:** States "Adam" in the Optimizer column (first row).
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** The table must display optimizers in alphabetical order. "Adam" is alphabetically first among (Adam, Adagrad, RMSprop, SGD), so it should appear in the first data row's Optimizer column.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adam.py

## CRITERION 13 [Accuracy]
**Description:** States 0.001 as Adam's default learning rate.
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
**Description:** States "No" for Adam's Uses Momentum value.
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
**Description:** States "Yes" for Adam's Adaptive Learning Rate value.
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Source (TensorFlow implementation): "
```python
class Adam(optimizer_v2.OptimizerV2):
  r"""Optimizer that implements the Adam algorithm.
```
"
Adam implements per-parameter adaptive learning rates by maintaining first and second moment estimates (moving averages of gradients and squared gradients) for each parameter. The TensorFlow Keras Optimizer documentation confirms Adam inherits from the base Optimizer class and implements adaptive moment estimation. The prompt states: "state 'Yes' if the optimizer adapts learning rates per parameter (like Adam, Adagrad, RMSprop do)". Adam is explicitly listed as an adaptive optimizer.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adam.py, https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer, https://arxiv.org/abs/1412.6980

## CRITERION 16 [Accuracy]
**Description:** States 5 as Adam's Hyperparameter Count value.
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** From Criterion 3, Adam has 5 optimizer-specific parameters: learning_rate, beta_1, beta_2, epsilon, amsgrad (excluding `name` and `**kwargs` as instructed).
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adam.py

## CRITERION 17 [Accuracy]
**Description:** States "Adagrad" in the Optimizer column (second row).
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Alphabetical order places Adagrad second (Adam, Adagrad, RMSprop, SGD).
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adagrad.py

## CRITERION 18 [Accuracy]
**Description:** States 0.001 as Adagrad's default learning rate.
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
**Description:** States "No" for Adagrad's Uses Momentum value.
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
**Description:** States "Yes" for Adagrad's Adaptive Learning Rate value.
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Source (TensorFlow implementation): "
```python
class Adagrad(optimizer_v2.OptimizerV2):
  r"""Optimizer that implements the Adagrad algorithm.
```
"
Adagrad implements per-parameter adaptive learning rates by accumulating squared gradients for each parameter individually. The TensorFlow Keras Optimizer base class documentation shows that optimizers can override the update_step method to implement adaptive behavior. The prompt explicitly lists Adagrad as an adaptive optimizer: "like Adam, Adagrad, RMSprop do".
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adagrad.py, https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer

## CRITERION 21 [Accuracy]
**Description:** States 3 as Adagrad's Hyperparameter Count value.
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** From Criterion 5, Adagrad has 3 optimizer-specific parameters: learning_rate, initial_accumulator_value, epsilon.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adagrad.py

## CRITERION 22 [Accuracy]
**Description:** States "RMSprop" in the Optimizer column (third row).
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Alphabetical order places RMSprop third (Adam, Adagrad, RMSprop, SGD).
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/rmsprop.py

## CRITERION 23 [Accuracy]
**Description:** States 0.001 as RMSprop's default learning rate.
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
**Description:** States "No" for RMSprop's Uses Momentum value.
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
**Description:** States "Yes" for RMSprop's Adaptive Learning Rate value.
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Source (TensorFlow implementation): "
```python
class RMSprop(optimizer_v2.OptimizerV2):
  r"""Optimizer that implements the RMSprop algorithm.
```
"
RMSprop implements per-parameter adaptive learning rates by maintaining a moving average of squared gradients for each parameter. The TensorFlow Keras Optimizer base class provides the framework for implementing adaptive update steps. The prompt explicitly lists RMSprop as an adaptive optimizer: "like Adam, Adagrad, RMSprop do".
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/rmsprop.py, https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer

## CRITERION 26 [Accuracy]
**Description:** States 5 as RMSprop's Hyperparameter Count value.
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** From Criterion 6, RMSprop has 5 optimizer-specific parameters: learning_rate, rho, momentum, epsilon, centered.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/rmsprop.py

## CRITERION 27 [Accuracy]
**Description:** States "SGD" in the Optimizer column (fourth row).
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Alphabetical order places SGD fourth and last (Adam, Adagrad, RMSprop, SGD).
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/gradient_descent.py

## CRITERION 28 [Accuracy]
**Description:** States 0.01 as SGD's default learning rate.
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
**Description:** States "No" for SGD's Uses Momentum value.
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
**Description:** States "No" for SGD's Adaptive Learning Rate value.
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** Source (TensorFlow implementation): "
```python
class SGD(optimizer_v2.OptimizerV2):
  r"""Gradient descent (with momentum) optimizer.
```
"
SGD uses a single global learning rate applied uniformly to all parameters. Unlike Adam, Adagrad, and RMSprop, SGD does not maintain parameter-specific statistics or adapt learning rates per parameter. The TensorFlow implementation shows it as "Gradient descent (with momentum) optimizer" - a standard gradient descent method without adaptive learning rates. The prompt specifies: "otherwise 'No' for fixed global rates". SGD uses a fixed global rate.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/gradient_descent.py, https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer

## CRITERION 31 [Accuracy]
**Description:** States 3 as SGD's Hyperparameter Count value.
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** From Criterion 4, SGD has 3 optimizer-specific parameters: learning_rate, momentum, nesterov.
**Sources:** https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/gradient_descent.py

## CRITERION 32 [Table Structure]
**Description:** Includes a comparison table in the response.
**Weight:** Critical
**Numerical Weight:** 4
**Rationale:** The prompt explicitly requires: "Create a comparison table analyzing the architectural and behavioral characteristics of all four optimizers." The response must include a table in markdown format to satisfy this requirement. Without a table, the response fails to complete the assigned task.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 33 [Table Structure]
**Description:** States that the table has exactly 5 columns.
**Weight:** Major
**Numerical Weight:** 2
**Rationale:** The prompt specifies: "The table must include exactly 5 columns with these headers in this exact order: 'Optimizer', 'Default Learning Rate', 'Uses Momentum', 'Adaptive Learning Rate', 'Hyperparameter Count'". The table must have precisely 5 columns, no more and no less.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 34 [Table Structure]
**Description:** States that the table has exactly 4 data rows.
**Weight:** Major
**Numerical Weight:** 2
**Rationale:** The prompt specifies: "Include exactly 4 data rows (one per optimizer)". Since there are 4 optimizers being analyzed (Adam, SGD, Adagrad, RMSprop), the table must have exactly 4 data rows plus the header row.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 35 [Table Structure]
**Description:** States that table rows are in alphabetical order.
**Weight:** Major
**Numerical Weight:** 4
**Rationale:** The prompt requires: "in alphabetical order by optimizer name". The correct alphabetical order is: Adam, Adagrad, RMSprop, SGD. The table rows must appear in this exact sequence.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 36 [Table Structure]
**Description:** States that column headers match exactly in the correct order.
**Weight:** Major
**Numerical Weight:** 2
**Rationale:** The prompt specifies headers "in this exact order": (1) "Optimizer", (2) "Default Learning Rate", (3) "Uses Momentum", (4) "Adaptive Learning Rate", (5) "Hyperparameter Count". The headers must match these names exactly (case-insensitive) and appear in this precise sequence from left to right.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 37 [Table Structure]
**Description:** Includes a brief introduction before the table.
**Weight:** Major
**Numerical Weight:** 4
**Rationale:** The prompt requires: "Before presenting the table, provide a brief introduction that states the number of columns, the number of rows, lists the column names, and describes how the rows are organized." An introduction paragraph must appear immediately before the table.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 38 [Table Structure]
**Description:** States the number of columns (5) in the table introduction.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The introduction must explicitly state: "5 columns" or equivalent phrasing like "consists of 5 columns" or "includes 5 columns". This is one of the four required elements listed in the prompt.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 39 [Table Structure]
**Description:** States the number of rows (4) in the table introduction.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The introduction must explicitly state: "4 rows" or equivalent phrasing like "consists of 4 rows" or "includes 4 data rows". This is one of the four required elements listed in the prompt.
**Sources:** N/A (structural requirement from prompt)

## CRITERION 40 [Table Structure]
**Description:** States column names and describes alphabetical organization in the introduction.
**Weight:** Minor
**Numerical Weight:** 4
**Rationale:** The introduction must: (1) list the column names (all 5: Optimizer, Default Learning Rate, Uses Momentum, Adaptive Learning Rate, Hyperparameter Count), and (2) describe how rows are organized (alphabetically by optimizer name). These are the remaining two required elements from the prompt's four-part introduction requirement.
**Sources:** N/A (structural requirement from prompt)
