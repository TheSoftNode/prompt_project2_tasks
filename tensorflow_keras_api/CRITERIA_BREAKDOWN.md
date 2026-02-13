# Criteria Breakdown - TensorFlow Keras Model API Analysis

This document maps each prompt question to its evaluation criteria, showing how multiple criteria are extracted from each question.

---

## **Question 1: Parameter Binding Strategy Divergence**

**Prompt text:**
> "Compare the constructor signatures across Model, Sequential, and Functional classes. Calculate the total count of unique parameter names across all three constructors, determine how many parameters are shared across all three classes, and express this as a ratio. Identify which specific parameter appears in one class but is absent from another despite both classes serving model construction purposes."

**Number of criteria extracted: 4**

**Breakdown:**
1. **"Calculate the total count of unique parameter names"** → **C1** (5 points)
   - Verifies total unique parameter count across all 3 constructors

2. **"determine how many parameters are shared across all three classes"** → **C2** (5 points)
   - Verifies count of parameters present in ALL 3 classes

3. **"express this as a ratio"** → **C3** (8 points)
   - Verifies the shared:total ratio calculation

4. **"Identify which specific parameter appears in one class but is absent from another"** → **C4** (8 points)
   - Verifies identification of parameter in Functional but not Sequential (e.g., "outputs")

**Why 4 criteria?**
The question asks for: (1) total count, (2) shared count, (3) ratio calculation, (4) specific parameter identification. Each distinct ask = separate criterion.

**Total for Question 1: 4 criteria, 26 points**

---

## **Question 2: Serialization Function Naming Asymmetry**

**Prompt text:**
> "Examine the model serialization API function pairs. Determine how many pairs follow asymmetric naming patterns between their save and load functions. Calculate the ratio of asymmetric pairs to total format pairs. For each pair, compute the character length difference between function names, and identify which pair exhibits the maximum difference."

**Number of criteria extracted: 7**

**Breakdown:**
1. **"Determine how many pairs follow asymmetric naming patterns"** → **C5** (5 points)
   - Verifies count of asymmetric pairs (e.g., 1 pair: get_config vs model_from_config)

2. **"Calculate the ratio of asymmetric pairs to total format pairs"** → **C6** (8 points)
   - Verifies ratio calculation (e.g., 1:3)

3. **"compute the character length difference" (JSON pair)** → **C7** (3 points)
   - Verifies: |len("model_to_json") - len("model_from_json")| = 0

4. **"compute the character length difference" (YAML pair)** → **C8** (3 points)
   - Verifies: |len("model_to_yaml") - len("model_from_yaml")| = 0

5. **"compute the character length difference" (config pair)** → **C9** (3 points)
   - Verifies: |len("get_config") - len("model_from_config")| = 7

6. **"identify which pair exhibits the maximum difference"** → **C10** (8 points)
   - Verifies: config pair (get_config/model_from_config)

7. **"state the difference value"** → **C11** (5 points)
   - Verifies: 7

**Why 7 criteria?**
The question asks for: (1) count, (2) ratio, (3-5) three length differences, (6) which pair has max, (7) the max value itself.

**Total for Question 2: 7 criteria, 35 points**

---

## **Question 3: Compile Method Parameter Optionality**

**Prompt text:**
> "Review the Model.compile() method signature. Count parameters with explicit non-None defaults versus those defaulting to None. Calculate the ratio between these two categories. Identify which parameter accepts the most diverse type options."

**Number of criteria extracted: 4**

**Breakdown:**
1. **"Count parameters with explicit non-None defaults"** → **C12** (5 points)
   - Verifies count (e.g., 2: run_eagerly=False, steps_per_execution=None might have other defaults)

2. **"Count parameters defaulting to None"** → **C13** (5 points)
   - Verifies count (e.g., 5: optimizer, loss, metrics, loss_weights, weighted_metrics)

3. **"Calculate the ratio between these two categories"** → **C14** (8 points)
   - Verifies ratio calculation (e.g., 2:5)

4. **"Identify which parameter accepts the most diverse type options"** → **C15** (8 points)
   - Verifies parameter name (e.g., "optimizer" accepts: str, Optimizer instance, dict)

**Why 4 criteria?**
The question asks for: (1) explicit defaults count, (2) None defaults count, (3) ratio, (4) most diverse parameter.

**Total for Question 3: 4 criteria, 26 points**

---

## **Question 4: Method Override Density**

**Prompt text:**
> "Compare method override patterns between Sequential and Functional classes relative to their parent. Count overridden methods for each class, determine which has more overrides, and identify a specific method that both classes override despite it being concrete in the parent."

**Number of criteria extracted: 4**

**Breakdown:**
1. **"Count overridden methods for...Sequential"** → **C16** (5 points)
   - Verifies count of methods Sequential overrides from Model

2. **"Count overridden methods for...Functional"** → **C17** (5 points)
   - Verifies count of methods Functional overrides from Model

3. **"determine which has more overrides"** → **C18** (8 points)
   - Verifies which class (Sequential or Functional) has higher count

4. **"identify a specific method that both classes override despite it being concrete"** → **C19** (8 points)
   - Verifies method name (e.g., "__init__" or "call" or "build")

**Why 4 criteria?**
The question asks for: (1) Sequential count, (2) Functional count, (3) comparison winner, (4) specific shared override.

**Total for Question 4: 4 criteria, 26 points**

---

## **Question 5: API Surface Complexity Table**

**Prompt text:**
> "Create a comparison table with 5 columns documenting constructor parameters, abstract methods, overridden methods, and multi-input support across the three classes. Order rows alphabetically and provide an introduction describing the table structure."

**Number of criteria extracted: 25**

**Breakdown:**

### **Analytical Criteria - Cell Values (15 criteria, 105 points)**

**Row 1 (Functional):**
- C20: Class Name = "Functional" (7 points)
- C21: Required Parameter Count = 2 (inputs, outputs) (7 points)
- C22: Defined Abstract Methods = 0 (7 points)
- C23: Overridden Methods = [count from C17] (7 points)
- C24: Multi-Input Support = "Yes" (7 points)

**Row 2 (Model):**
- C25: Class Name = "Model" (7 points)
- C26: Required Parameter Count = 0 or 2 (flexible signature) (7 points)
- C27: Defined Abstract Methods = [count] (7 points)
- C28: Overridden Methods = 0 (base class) (7 points)
- C29: Multi-Input Support = "Yes" (7 points)

**Row 3 (Sequential):**
- C30: Class Name = "Sequential" (7 points)
- C31: Required Parameter Count = 0 (layers has default) (7 points)
- C32: Defined Abstract Methods = 0 (7 points)
- C33: Overridden Methods = [count from C16] (7 points)
- C34: Multi-Input Support = "No" (7 points)

### **Table Structure Criteria (10 criteria, 30 points)**

- C35: Table is provided (4 points)
- C36: Table has exactly 5 columns (3 points)
- C37: Table has exactly 3 data rows (3 points)
- C38: Column 1 = "Class Name" (2 points)
- C39: Column 2 = "Required Parameter Count" (2 points)
- C40: Column 3 = "Defined Abstract Methods" (2 points)
- C41: Column 4 = "Overridden Methods" (2 points)
- C42: Column 5 = "Multi-Input Support" (2 points)
- C43: Rows in alphabetical order (Functional, Model, Sequential) (4 points)
- C44: Introduction describes structure (3 points)

**Why 25 criteria?**
The table requires: 3 rows × 5 columns = 15 cell values, plus 10 structure/format criteria.

**Total for Question 5: 25 criteria, 135 points**

---

## **Summary**

**Total criteria across all questions: 44 criteria, 248 points**

- **Question 1:** 4 criteria (total params, shared params, ratio, specific param)
- **Question 2:** 7 criteria (asymmetric count, ratio, 3 length diffs, max pair, max value)
- **Question 3:** 4 criteria (explicit count, None count, ratio, most diverse param)
- **Question 4:** 4 criteria (Sequential overrides, Functional overrides, comparison, shared override)
- **Question 5:** 25 criteria (15 cell values + 10 table structure)

---

## **Key Principles Applied**

1. **Each calculation = separate criterion**
   - "Calculate total" vs "calculate shared" vs "calculate ratio" = 3 criteria

2. **Each count/identification = separate criterion**
   - Don't bundle multiple counts into one criterion

3. **Ratios are high-value criteria**
   - Ratio calculations weighted 8 points (require synthesis)

4. **Table cells verified individually**
   - Each of 15 cells = separate criterion for precise grading

5. **Complex questions yield more criteria**
   - Question 2 has 7 criteria due to multiple calculations
