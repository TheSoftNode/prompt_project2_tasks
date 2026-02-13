# Table Criteria for Question 3: Cross-Study Pattern Comparison

This document defines the evaluation criteria for the table in Question 3.

---

## Table Requirements

**Question 3** asks for: "Create an image of a table comparing API design patterns across the empirical studies with exactly 3 data rows (excluding header) and exactly 3 columns. The table must have the exact title: 'API Design Pattern Usability: Empirical Evidence Synthesis'. Column headers must be: 'Pattern', 'Time Penalty (vs. Baseline)', 'Cognitive Violations'. Row 1 must be labeled 'Factory Pattern' and contain Ellis's SSLSocket data (time penalty as ratio, number of Clarke dimensions violated). Row 2 must be labeled 'Required Constructor Parameters' and contain Stylos & Clarke's data (comparing to create-set-call baseline, number of violated dimensions). Row 3 must be labeled 'Helper Class Methods' and contain Stylos & Myers's Email task data (time penalty ratio, number of violated dimensions)."

---

## Structural Criteria (4 criteria: C29-C32)

### CRITERION 29 [Table Structure]
**Sub-prompt #29:** Does table have markdown format?
**Answer:** Yes

**Rationale:** Question 3 explicitly requires creating a table comparing API design patterns. The table must use markdown syntax with pipe delimiters and header separators to be considered valid for image generation.

**Sources:** Not applicable - structural requirement

---

### CRITERION 30 [Table Structure]
**Sub-prompt #30:** How many columns total?
**Answer:** 3

**Rationale:** Question 3 specifies the table must have exactly 3 columns: "Pattern", "Time Penalty (vs. Baseline)", "Cognitive Violations". A table with fewer or more columns fails to meet the specification.

**Sources:** Not applicable - structural requirement

---

### CRITERION 31 [Table Structure]
**Sub-prompt #31:** How many data rows (excluding header)?
**Answer:** 3

**Rationale:** Question 3 specifies exactly 3 data rows: one for Factory Pattern, one for Required Constructor Parameters, and one for Helper Class Methods. More or fewer rows indicates incorrect content.

**Sources:** Not applicable - structural requirement

---

### CRITERION 32 [Table Structure]
**Sub-prompt #32:** Does table have exact title?
**Answer:** Yes

**Rationale:** Question 3 explicitly specifies the table "must have the exact title: 'API Design Pattern Usability: Empirical Evidence Synthesis'". The title provides context for the cross-study comparison.

**Sources:** Not applicable - structural requirement

---

## Column Header Criteria (2 criteria: C33-C34)

### CRITERION 33 [Table Content]
**Sub-prompt #33:** What is column 2 header?
**Answer:** Time Penalty (vs. Baseline)

**Rationale:** Question 3 specifies column headers must include "Time Penalty (vs. Baseline)" as the second column to show the empirical performance cost of each pattern compared to baseline approaches.

**Sources:** Not applicable - structural requirement

---

### CRITERION 34 [Table Content]
**Sub-prompt #34:** What is column 3 header?
**Answer:** Cognitive Violations

**Rationale:** Question 3 specifies column headers must include "Cognitive Violations" as the third column to show how many dimensions from Clarke & Becker's framework each pattern violates.

**Sources:** Not applicable - structural requirement

---

## Row 1: Factory Pattern (3 criteria: C35-C37)

### CRITERION 35 [Table Content]
**Sub-prompt #35:** What is row 1 pattern name?
**Answer:** Factory Pattern

**Rationale:** Question 3 specifies Row 1 "must be labeled 'Factory Pattern'" to identify this design pattern in the comparison.

**Sources:** Not applicable - structural requirement

---

### CRITERION 36 [Table Content]
**Sub-prompt #36:** What is time penalty value?
**Answer:** 2.09

**Rationale:** From Ellis et al., the factory pattern shows a median completion time of 16:05 (965 seconds) compared to constructor approach at 7:42 (461 seconds) for the SSLSocket task. The time penalty ratio is 965 ÷ 461 = 2.09.

**Sources:** Ellis, B., Stylos, J., & Myers, B. (2007). The factory pattern in API design: A usability evaluation. Figure 3 (median times)

---

### CRITERION 37 [Table Content]
**Sub-prompt #37:** How many cognitive violations?
**Answer:** 5

**Rationale:** From Question 1 analysis, the factory pattern violates 5 dimensions from Clarke & Becker's framework: Work-Step Unit, Penetrability, Premature Commitment, Abstraction Gradient, and Hidden Dependencies.

**Sources:** Ellis (2007) usability problems mapped to Clarke & Becker (2003) cognitive dimensions framework

---

## Row 2: Required Constructor Parameters (3 criteria: C38-C40)

### CRITERION 38 [Table Content]
**Sub-prompt #38:** What is row 2 pattern name?
**Answer:** Required Constructor Parameters

**Rationale:** Question 3 specifies Row 2 "must be labeled 'Required Constructor Parameters'" to identify this API design pattern.

**Sources:** Not applicable - structural requirement

---

### CRITERION 39 [Table Content]
**Sub-prompt #39:** What is time penalty value?
**Answer:** N/A

**Rationale:** Stylos & Clarke (2007) study focuses on avoidance behavior rather than time penalties. Their data shows 100% of participants avoided required constructor parameters in favor of create-set-call pattern, but they do not report completion time comparisons.

**Sources:** Stylos, J., & Clarke, S. (2007). Usability implications of requiring parameters in objects' constructors. (No time penalty data available)

---

### CRITERION 40 [Table Content]
**Sub-prompt #40:** How many cognitive violations?
**Answer:** 3

**Rationale:** Required constructor parameters violate 3 cognitive dimensions: Premature Commitment (must know values upfront), Viscosity (hard to change once set), and Visibility (parameters not easily discoverable).

**Sources:** Stylos & Clarke (2007) mapped to Clarke & Becker (2003) framework

---

## Row 3: Helper Class Methods (3 criteria: C41-C43)

### CRITERION 41 [Table Content]
**Sub-prompt #41:** What is row 3 pattern name?
**Answer:** Helper Class Methods

**Rationale:** Question 3 specifies Row 3 "must be labeled 'Helper Class Methods'" to identify this API design pattern.

**Sources:** Not applicable - structural requirement

---

### CRITERION 42 [Table Content]
**Sub-prompt #42:** What is time penalty value?
**Answer:** 11.2

**Rationale:** From Stylos & Myers (2008), the Email task shows helper class methods took median 11.2 minutes versus starting class methods at 1.0 minute, giving a time penalty ratio of 11.2 ÷ 1.0 = 11.2.

**Sources:** Stylos, J., & Myers, B. A. (2008). The implications of method placement on API learnability. Table 1 (Email task median times)

---

### CRITERION 43 [Table Content]
**Sub-prompt #43:** How many cognitive violations?
**Answer:** 3

**Rationale:** Helper class methods violate 3 cognitive dimensions: Penetrability (hard to discover helper classes), Work-Step Unit (requires finding multiple classes), and Working Framework (adds architectural complexity).

**Sources:** Stylos & Myers (2008) mapped to Clarke & Becker (2003) framework

---

## Summary

**Total Criteria: 13**

- **Structural Criteria (C29-C32)**: 4 criteria
  - C29: Markdown table format
  - C30: 3 columns
  - C31: 3 data rows
  - C32: Exact title

- **Column Header Criteria (C33-C34)**: 2 criteria
  - C33: "Time Penalty (vs. Baseline)" header
  - C34: "Cognitive Violations" header

- **Row 1: Factory Pattern (C35-C37)**: 3 criteria
  - C35: Row label "Factory Pattern"
  - C36: Time penalty = 2.09
  - C37: Violations = 5

- **Row 2: Constructor Parameters (C38-C40)**: 3 criteria
  - C38: Row label "Required Constructor Parameters"
  - C39: Time penalty = N/A
  - C40: Violations = 3

- **Row 3: Helper Class Methods (C41-C43)**: 3 criteria
  - C41: Row label "Helper Class Methods"
  - C42: Time penalty = 11.2
  - C43: Violations = 3
