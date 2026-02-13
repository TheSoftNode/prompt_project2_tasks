# TensorFlow Keras Optimizer Comparison Table

| Optimizer | Default Learning Rate | Uses Momentum | Adaptive Learning Rate | Hyperparameter Count |
|:----------|:---------------------|:--------------|:-----------------------|:---------------------|
| Adam | 0.001 | No | Yes | 4 |
| Adagrad | 0.001 | No | Yes | 3 |
| RMSprop | 0.001 | No | Yes | 4 |
| SGD | 0.01 | No | No | 2 |

## Detailed Breakdown

### Adam (adam.py)
- Default learning_rate: 0.001
- Hyperparameters: learning_rate, beta_1 (0.9), beta_2 (0.999), epsilon (1e-7), amsgrad (False) = **4 parameters** (excluding name, **kwargs)
- Momentum: No dedicated momentum parameter (uses beta_1/beta_2 for moment estimates)
- Adaptive: Yes (per-parameter adaptive learning rates)

### Adagrad (adagrad.py)
- Default learning_rate: 0.001
- Hyperparameters: learning_rate, initial_accumulator_value (0.1), epsilon (1e-7) = **3 parameters**
- Momentum: No
- Adaptive: Yes (per-parameter adaptive learning rates)

### RMSprop (rmsprop.py)
- Default learning_rate: 0.001
- Hyperparameters: learning_rate, rho (0.9), momentum (0.0), epsilon (1e-7), centered (False) = **4 parameters**
- Momentum: Has momentum parameter but default is 0.0 = No
- Adaptive: Yes (per-parameter adaptive learning rates)

### SGD (gradient_descent.py)
- Default learning_rate: 0.01
- Hyperparameters: learning_rate, momentum (0.0), nesterov (False) = **2 parameters**
- Momentum: Has momentum parameter but default is 0.0 = No
- Adaptive: No (fixed learning rate for all parameters)

## Answer Key

**Q1:** Number of abstract methods in OptimizerV2 = Need to count `@abc.abstractmethod` decorators

**Q2:** Optimizer with most hyperparameters = Adam and RMSprop (tie with 4 parameters each, but should pick Adam or RMSprop based on which is mentioned first)

**Q3:** SGD default momentum value = 0.0

**Q4:** Ratio of Adam's learning rate to Adagrad's learning rate = 0.001 / 0.001 = 1.0 (or 1:1)
