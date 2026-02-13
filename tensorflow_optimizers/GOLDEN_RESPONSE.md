# TensorFlow Keras Optimizer Analysis

Analysis of the TensorFlow Keras optimizer implementations in the tensorflow/tensorflow repository as of February 1, 2026.

## Count-based Findings

**Abstract method contract**

The optimizer_v2 module contains OptimizerV2 as the base class for all optimizer implementations. [1] This class defines 1 abstract method that subclasses must implement: `get_config`. [1] This method returns the configuration dictionary of the optimizer, enabling serialization and deserialization of optimizer instances. [1]

Abstract methods count = 1. [1]

**Inheritance architecture**

All four analyzed optimizers (Adam, SGD, Adagrad, RMSprop) inherit directly from the same base class. [1] By examining the class definitions, Adam inherits from OptimizerV2, SGD inherits from OptimizerV2, Adagrad inherits from OptimizerV2, and RMSprop inherits from OptimizerV2. [1]

Base class name = OptimizerV2. [1]

**Hyperparameter complexity**

Adam's `__init__` method accepts 5 optimizer-specific hyperparameters: `learning_rate` (default 0.001), `beta_1` (default 0.9), `beta_2` (default 0.999), `epsilon` (default 1e-7), and `amsgrad` (default False). [2] SGD accepts 3 parameters: `learning_rate` (default 0.01), `momentum` (default 0.0), and `nesterov` (default False). [3] Adagrad accepts 3 parameters: `learning_rate` (default 0.001), `initial_accumulator_value` (default 0.1), and `epsilon` (default 1e-7). [4] RMSprop accepts 5 parameters: `learning_rate` (default 0.001), `rho` (default 0.9), `momentum` (default 0.0), `epsilon` (default 1e-7), and `centered` (default False). [5]

Highest hyperparameter count = Adam or RMSprop with 5 parameters each (excluding name and \*\*kwargs). [2][5]

**Moment estimation parameters**

Adam implements adaptive moment estimation using two exponential moving average parameters. [2][7] The first moment estimate uses `beta_1` (default 0.9) to control the exponential decay rate for the gradient moving average. [2][7] The second moment estimate uses `beta_2` (default 0.999) for the squared gradient moving average. [2][7] RMSprop uses different parameter names: `rho` for the gradient square moving average and optionally `momentum` for velocity. [5]

Adam's first moment decay parameter name = beta_1. [2][7]

**Acceleration mechanism defaults**

SGD's `__init__` signature specifies `momentum=0.0` as the default value for its acceleration parameter. [3] When momentum is 0, the update rule simplifies to vanilla gradient descent: `w = w - learning_rate * g`. [3] When momentum exceeds 0, velocity accumulation accelerates convergence: `velocity = momentum * velocity - learning_rate * g` followed by `w = w + velocity`. [3]

SGD momentum default value = 0.0. [3]

**Adagrad initialization strategy**

Adagrad initializes per-parameter accumulators to avoid division by zero at the start of training. [4][8] The `initial_accumulator_value` parameter (default 0.1) sets the starting value for these accumulators. [4] This positive initialization ensures numerical stability during the first optimization steps, as described in the original adaptive subgradient methods paper. [4][8]

Adagrad initial_accumulator_value default = 0.1. [4][8]

**Learning rate configurations**

Adam, Adagrad, and RMSprop all specify `learning_rate=0.001` as their default value. [2][4][5] SGD specifies `learning_rate=0.01`, which is 10 times larger. [3]

Ratio of common rate (0.001) to different rate (0.01) = 0.001:0.01 = 1:10. [2][3][4][5]

**Adaptive versus non-adaptive distribution**

Adam, Adagrad, and RMSprop implement per-parameter adaptive learning rates by maintaining parameter-specific statistics (moment estimates, accumulated gradients, or gradient squares). [2][4][5][6][7][8] Adagrad's adaptive approach, introduced in Duchi et al. (2011), accumulates squared gradients to scale learning rates inversely with gradient magnitudes. [4][8] SGD uses a single global learning rate applied uniformly across all parameters. [3][6]

Adaptive to non-adaptive ratio = 3:1. [2][3][4][5][6][7][8]

**Comparative architecture table**

The table below includes the determined characteristics for each optimizer. It consists of 5 columns and 4 rows. The columns are named: Optimizer, Default Learning Rate, Uses Momentum, Adaptive Learning Rate, and Hyperparameter Count. Optimizers are displayed in rows in alphabetical order: Adam, Adagrad, RMSprop, and SGD. [1][2]

| Optimizer | Default Learning Rate | Uses Momentum | Adaptive Learning Rate | Hyperparameter Count |
| :-------- | :-------------------- | :------------ | :--------------------- | :------------------- |
| Adam      | 0.001                 | No            | Yes                    | 5                    |
| Adagrad   | 0.001                 | No            | Yes                    | 3                    |
| RMSprop   | 0.001                 | No            | Yes                    | 5                    |
| SGD       | 0.01                  | No            | No                     | 3                    |

## Conclusion

The TensorFlow Keras optimizer_v2 module demonstrates a consistent architectural pattern where all optimizers inherit from OptimizerV2 and implement a single abstract method (get_config) for configuration management. Adam exhibits the highest hyperparameter complexity with 4 tunable parameters, reflecting its sophisticated adaptive moment estimation approach using beta_1 for first moment decay. Three of the four analyzed optimizers (Adam, Adagrad, RMSprop) share an identical default learning rate of 0.001, while SGD uses 0.01, creating a 1:10 ratio. SGD's momentum parameter defaults to 0.0, indicating vanilla gradient descent unless explicitly configured otherwise. Adagrad's initial_accumulator_value of 0.1 ensures numerical stability during early training iterations. The 3:1 ratio of adaptive to non-adaptive optimizers underscores TensorFlow's emphasis on algorithms that automatically adjust learning rates based on parameter-specific gradient statistics.

## References

[1] tensorflow/tensorflow. "OptimizerV2 Base Class." _tensorflow/python/keras/optimizer_v2/optimizer_v2.py_, commit 56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449. GitHub. https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/optimizer_v2.py

[2] tensorflow/tensorflow. "Adam Optimizer." _tensorflow/python/keras/optimizer_v2/adam.py_, commit 56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449. GitHub. https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adam.py

[3] tensorflow/tensorflow. "SGD Optimizer." _tensorflow/python/keras/optimizer_v2/gradient_descent.py_, commit 56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449. GitHub. https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/gradient_descent.py

[4] tensorflow/tensorflow. "Adagrad Optimizer." _tensorflow/python/keras/optimizer_v2/adagrad.py_, commit 56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449. GitHub. https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/adagrad.py

[5] tensorflow/tensorflow. "RMSprop Optimizer." _tensorflow/python/keras/optimizer_v2/rmsprop.py_, commit 56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449. GitHub. https://github.com/tensorflow/tensorflow/blob/56e5f82166a6cf6b4b7bc1202affe0bd8b0c8449/tensorflow/python/keras/optimizer_v2/rmsprop.py

[6] TensorFlow. "Keras Optimizers API Documentation." https://www.tensorflow.org/api_docs/python/tf/keras/optimizers

[7] Kingma, Diederik P., and Jimmy Ba. "Adam: A Method for Stochastic Optimization." arXiv preprint arXiv:1412.6980 (2014). https://arxiv.org/abs/1412.6980
