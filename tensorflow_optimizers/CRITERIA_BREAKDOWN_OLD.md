# Complete Criteria Breakdown - TensorFlow Keras Optimizer Analysis

## Prompt Coverage Analysis (40 Criteria)

This document maps every requirement in the prompt to its corresponding rubric criteria, showing how each question yields MULTIPLE criteria.

---

## **Question 1: Base Class Architecture**

### Prompt Text:
> "The optimizer_v2 module contains a base class that all optimizer implementations inherit from. **Locate this base class, state its name**, and **identify how many abstract methods** (decorated with `@abc.abstractmethod`) subclasses must implement to satisfy the inheritance contract."

### Actions Required:
1. **LOCATE** the base class (find it in the codebase)
2. **STATE** its name (explicitly name it)
3. **IDENTIFY** the count of abstract methods

### Criteria Extracted:

**C1 (8 points):** Locates and states "OptimizerV2" as the base class name
- ✅ Checks: Did they LOCATE the base class?
- ✅ Checks: Did they STATE the name "OptimizerV2"?
- **Why 1 criterion:** The actions "locate" and "state its name" are so tightly coupled that splitting them would be artificial

**C2 (8 points):** Identifies 1 as the count of abstract methods
- ✅ Checks: Did they IDENTIFY how many abstract methods?
- ✅ Checks: Did they find methods decorated with `@abc.abstractmethod`?
- ✅ Checks: Did they count correctly (1)?

**Total for Q1: 2 criteria, 16 points**

---

## **Question 2: Hyperparameter Complexity and Parameter Naming**

### Prompt Text:
> "Each optimizer defines hyperparameters in its `__init__` method to control optimization behavior. By examining the initialization signatures of Adam, SGD, Adagrad, and RMSprop, **determine which optimizer has the most complex configuration** by counting optimizer-specific parameters (exclude common parameters like `name` and `**kwargs`). Additionally, **identify the specific parameter name** that Adam uses to control its first moment decay rate, noting that this differs from the parameter names used by other optimizers with similar mechanisms."

### Actions Required:
1. **EXAMINE** initialization signatures of all four optimizers
2. **DETERMINE** which has most complex configuration (highest count)
3. **COUNT** optimizer-specific parameters correctly
4. **EXCLUDE** common parameters (name, **kwargs)
5. **IDENTIFY** Adam's specific parameter name for first moment decay

### Criteria Extracted:

**C3 (8 points):** Determines Adam (or RMSprop) as having the most complex configuration
- ✅ Checks: Did they EXAMINE all four optimizers?
- ✅ Checks: Did they COUNT parameters correctly?
- ✅ Checks: Did they EXCLUDE name and **kwargs?
- ✅ Checks: Did they DETERMINE the correct optimizer?
- **Why 1 criterion:** All these checks lead to ONE answer

**C4 (8 points):** Identifies "beta_1" as Adam's first moment decay parameter name
- ✅ Checks: Did they IDENTIFY the specific parameter NAME (not value)?
- ✅ Checks: Is it specifically for first moment decay?
- ✅ Checks: Did they note it differs from other optimizers?

**Total for Q2: 2 criteria, 16 points**

---

## **Question 3: Default Value Analysis and Ratios**

### Prompt Text:
> "Optimizers use default values for their hyperparameters that reflect algorithm-specific tuning strategies. **Identify the default values** for the following: **SGD's acceleration parameter** (express as a decimal), **Adagrad's initial accumulator value** (the parameter preventing division by zero at training start), and **calculate the ratio** between the common default learning rate shared by three optimizers versus the different default used by the fourth optimizer (express as a simplified ratio like X:Y)."

### Actions Required:
1. **IDENTIFY** SGD's acceleration parameter default value
2. **EXPRESS** as decimal
3. **IDENTIFY** Adagrad's initial accumulator value default
4. **UNDERSTAND** its purpose (prevent division by zero)
5. **IDENTIFY** which three optimizers share a common learning rate
6. **IDENTIFY** which one differs
7. **CALCULATE** the ratio
8. **EXPRESS** as simplified ratio (X:Y)

### Criteria Extracted:

**C5 (8 points):** Identifies 0.0 (or 0) as SGD's acceleration parameter default
- ✅ Checks: Did they IDENTIFY SGD's acceleration parameter (momentum)?
- ✅ Checks: Did they get the default value correct (0.0)?
- ✅ Checks: Did they EXPRESS as decimal?

**C6 (8 points):** Identifies 0.1 as Adagrad's initial accumulator value default
- ✅ Checks: Did they IDENTIFY Adagrad's initial accumulator parameter?
- ✅ Checks: Did they understand its purpose (prevent division by zero)?
- ✅ Checks: Did they get the default value correct (0.1)?

**C7 (8 points):** Calculates "1:10" (or "0.001:0.01" or "0.1") as the learning rate ratio
- ✅ Checks: Did they IDENTIFY the common rate (0.001)?
- ✅ Checks: Did they IDENTIFY which three optimizers share it (Adam, Adagrad, RMSprop)?
- ✅ Checks: Did they IDENTIFY the different rate (0.01)?
- ✅ Checks: Did they IDENTIFY which optimizer differs (SGD)?
- ✅ Checks: Did they CALCULATE the ratio correctly?
- ✅ Checks: Did they EXPRESS as simplified ratio (1:10 or equivalent)?

**Total for Q3: 3 criteria, 24 points**

---

## **Question 4: Comparison Table**

This question has TWO distinct parts:
1. **Table Cell Values** (20 criteria)
2. **Table Structure** (13 criteria)

### Part A: Table Cell Values (C8-C27)

Each cell in the table represents a separate criterion because the prompt explicitly defines what each cell should contain.

#### **Requirement:** "Include exactly 4 data rows (one per optimizer) in alphabetical order by optimizer name"

**Alphabetical Ordering Constraint:**
- Adam (1st)
- Adagrad (2nd)
- RMSprop (3rd)
- SGD (4th)

#### **Column 1: "Optimizer"**
- **C8:** States "Adam" in Optimizer column
- **C13:** States "Adagrad" in Optimizer column
- **C18:** States "RMSprop" in Optimizer column
- **C23:** States "SGD" in Optimizer column

#### **Column 2: "Default Learning Rate"**
> "For 'Default Learning Rate', state the numerical default value from each `__init__` method"

- **C9:** States 0.001 as Adam's Default Learning Rate
- **C14:** States 0.001 as Adagrad's Default Learning Rate
- **C19:** States 0.001 as RMSprop's Default Learning Rate
- **C24:** States 0.01 as SGD's Default Learning Rate

#### **Column 3: "Uses Momentum"**
> "For 'Uses Momentum', state 'Yes' only if the optimizer has a momentum parameter with a non-zero default value, otherwise 'No'"

- **C10:** States "No" for Adam's Uses Momentum
  - ✅ Checks: No momentum parameter
- **C15:** States "No" for Adagrad's Uses Momentum
  - ✅ Checks: No momentum parameter
- **C20:** States "No" for RMSprop's Uses Momentum
  - ✅ Checks: Has momentum parameter but default is 0.0
  - ✅ Checks: Applies "non-zero default" rule correctly
- **C25:** States "No" for SGD's Uses Momentum
  - ✅ Checks: Has momentum parameter but default is 0.0
  - ✅ Checks: Applies "non-zero default" rule correctly

#### **Column 4: "Adaptive Learning Rate"**
> "For 'Adaptive Learning Rate', state 'Yes' if the optimizer adapts learning rates per parameter (like Adam, Adagrad, RMSprop do), otherwise 'No' for fixed global rates"

- **C11:** States "Yes" for Adam's Adaptive Learning Rate
  - ✅ Checks: Per-parameter adaptation
- **C16:** States "Yes" for Adagrad's Adaptive Learning Rate
  - ✅ Checks: Per-parameter adaptation
- **C21:** States "Yes" for RMSprop's Adaptive Learning Rate
  - ✅ Checks: Per-parameter adaptation
- **C26:** States "No" for SGD's Adaptive Learning Rate
  - ✅ Checks: Fixed global rate (not per-parameter)

#### **Column 5: "Hyperparameter Count"**
> "For 'Hyperparameter Count', count only optimizer-specific parameters in `__init__`, excluding `name` and `**kwargs`"

- **C12:** States 4 as Adam's Hyperparameter Count
  - ✅ Checks: Correct count (learning_rate, beta_1, beta_2, epsilon, amsgrad)
  - ✅ Checks: Excludes name and **kwargs
- **C17:** States 3 as Adagrad's Hyperparameter Count
  - ✅ Checks: Correct count (learning_rate, initial_accumulator_value, epsilon)
- **C22:** States 4 as RMSprop's Hyperparameter Count
  - ✅ Checks: Correct count (learning_rate, rho, momentum, epsilon, centered)
- **C27:** States 2 as SGD's Hyperparameter Count
  - ✅ Checks: Correct count (learning_rate, momentum, nesterov)

**Subtotal for Cell Values: 20 criteria (C8-C27), 80 points**

---

### Part B: Table Structure (C28-C40)

#### **Requirement 1: Table Inclusion**
> "Create a comparison table of the four analyzed optimizers"

**C28 (2 points):** Includes a comparison table in the response
- ✅ Checks: Table exists
- ✅ Checks: Presents optimizer comparison

#### **Requirement 2: Column Count**
> "The table must include exactly 5 columns"

**C29 (5 points):** Formats the table with exactly 5 columns
- ✅ Checks: Exactly 5 columns (not 4, not 6)

#### **Requirement 3: Row Count**
> "Include exactly 4 data rows (one per optimizer)"

**C30 (5 points):** Formats the table with exactly 4 data rows (excluding header)
- ✅ Checks: Exactly 4 data rows
- ✅ Checks: Excludes header from count
- ✅ Checks: One row per optimizer

#### **Requirement 4: Column Headers in Exact Order**
> "with these headers in this exact order: 'Optimizer', 'Default Learning Rate', 'Uses Momentum', 'Adaptive Learning Rate', 'Hyperparameter Count'"

**C31 (2 points):** Includes "Optimizer" as the first column header
- ✅ Checks: "Optimizer" header exists
- ✅ Checks: In first position

**C32 (2 points):** Includes "Default Learning Rate" as the second column header
- ✅ Checks: "Default Learning Rate" header exists
- ✅ Checks: In second position

**C33 (2 points):** Includes "Uses Momentum" as the third column header
- ✅ Checks: "Uses Momentum" header exists
- ✅ Checks: In third position

**C34 (2 points):** Includes "Adaptive Learning Rate" as the fourth column header
- ✅ Checks: "Adaptive Learning Rate" header exists
- ✅ Checks: In fourth position

**C35 (2 points):** Includes "Hyperparameter Count" as the fifth column header
- ✅ Checks: "Hyperparameter Count" header exists
- ✅ Checks: In fifth position

#### **Requirement 5: Alphabetical Ordering**
> "in alphabetical order by optimizer name"

**C36 (2 points):** Displays optimizers in alphabetical order
- ✅ Checks: Adam first
- ✅ Checks: Adagrad second
- ✅ Checks: RMSprop third
- ✅ Checks: SGD fourth

#### **Requirement 6: Table Introduction**
> "Before presenting the table, provide a brief introduction that states the number of columns, the number of rows, lists the column names, and describes how the rows are organized."

**C37 (3 points):** Provides a brief introduction before the table
- ✅ Checks: Introduction exists
- ✅ Checks: Before the table (not after)
- ✅ Checks: Describes table structure

**C38 (2 points):** States the number of columns in the introduction
- ✅ Checks: States "5 columns" (or equivalent)
- ✅ Checks: In the introduction

**C39 (2 points):** States the number of rows in the introduction
- ✅ Checks: States "4 rows" or "4 optimizers" (or equivalent)
- ✅ Checks: In the introduction

**C40 (2 points):** Lists the column names in the introduction
- ✅ Checks: Lists all 5 column names
- ✅ Checks: In the introduction

**Subtotal for Table Structure: 13 criteria (C28-C40), 28 points**

---

## **FINAL BREAKDOWN SUMMARY**

| Question | Description | Criteria Count | Points | Criteria Numbers |
|:---------|:-----------|:---------------|:-------|:-----------------|
| **Q1** | Base Class Architecture | 2 | 16 | C1-C2 |
| **Q2** | Hyperparameter Complexity & Naming | 2 | 16 | C3-C4 |
| **Q3** | Default Values & Ratios | 3 | 24 | C5-C7 |
| **Q4a** | Table Cell Values | 20 | 80 | C8-C27 |
| **Q4b** | Table Structure | 13 | 28 | C28-C40 |
| **TOTAL** | **All Requirements** | **40** | **136** | C1-C40 |

---

## **Why Multiple Criteria Per Question?**

### **Question 1 Example:**
The prompt says: "Locate this base class, state its name, and identify how many abstract methods..."

This is asking for TWO distinct things:
1. **NAME of the base class** → C1
2. **COUNT of abstract methods** → C2

Even though "locate" and "state its name" are mentioned, they're so tightly coupled that splitting them into separate criteria would be artificial. The key distinction is NAME vs COUNT.

### **Question 2 Example:**
The prompt says: "determine which optimizer has the most complex configuration... Additionally, identify the specific parameter name that Adam uses..."

Two distinct asks:
1. **Which optimizer has highest count** → C3
2. **What is Adam's parameter NAME** → C4

### **Question 3 Example:**
The prompt says: "Identify the default values for the following: SGD's acceleration parameter... Adagrad's initial accumulator value... and calculate the ratio..."

Three distinct values requested:
1. **SGD's acceleration default** → C5
2. **Adagrad's accumulator default** → C6
3. **Learning rate ratio** → C7

### **Question 4 Example:**
The table question is special because:
- **20 cells** = **20 cell value criteria** (C8-C27)
- **Structure requirements** = **13 structural criteria** (C28-C40)

Each cell is a separate criterion because the prompt explicitly defines what each cell should contain.

---

## **100% Coverage Verification**

✅ **Every prompt instruction has corresponding criteria**
✅ **"Locate" AND "state" → Covered in C1**
✅ **"Identify count" → C2**
✅ **"Determine" highest → C3**
✅ **"Identify" parameter name → C4**
✅ **"Identify" three default values → C5, C6, C7**
✅ **All 20 table cells → C8-C27**
✅ **All table structural requirements → C28-C40**
✅ **Exact column order → C31-C35**
✅ **Alphabetical row order → C36**
✅ **Table introduction with 3 requirements → C37-C40**

**No prompt requirement is uncovered. Every instruction yields at least one criterion.**
