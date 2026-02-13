# Question Breakdown: Verification Criteria

This document breaks down each question into atomic sub-questions/criteria that can be independently verified. Each criterion should have a short answer (≤5 words).

---

## Question 1: Cognitive Dimension Violation Cost Analysis (15 criteria)

### Sentence 1: Determining Violations and Coefficient (2 criteria)

**C1:** How many dimensions does factory violate?
- Expected answer: 5

**C2:** What is factory per-dimension coefficient?
- Expected answer: 0.42

### Sentence 2: Factory Time Penalty Extraction (3 criteria)

**C3:** What is Ellis's SSLSocket factory median time in seconds?
- Expected answer: 965

**C4:** What is Ellis's SSLSocket constructor median time in seconds?
- Expected answer: 461

**C5:** What is the factory time penalty ratio?
- Expected answer: 2.09

### Sentence 3: Helper Class Speedup Analysis (8 criteria)

**C6:** What is the first task name?
- Expected answer: Email

**C7:** What is the second task name?
- Expected answer: Web

**C8:** What is the third task name?
- Expected answer: Thingies

**C9:** What is Email task speedup?
- Expected answer: 11.2

**C10:** What is Web task speedup?
- Expected answer: 7.6

**C11:** What is Thingies task speedup?
- Expected answer: 2.4

**C12:** What is the average speedup?
- Expected answer: 7.07

**C13:** What is helper per-dimension coefficient?
- Expected answer: 2.36

### Sentence 4: Coefficient Comparison (2 criteria)

**C14:** What is the coefficient ratio?
- Expected answer: 5.6

**C15:** Which pattern has greater cognitive cost per dimension?
- Expected answer: Helper class

---

## Question 2: Experience-Adjusted Pattern Complexity Score (11 criteria)

### Piccioni Percentage Improvement (1 criterion)

**C1:** What is the percentage improvement?
- Expected answer: 45%

### Stylos & Myers Task Speedups (5 criteria)

**C2:** What is Email task speedup?
- Expected answer: 11.2

**C3:** What is Web task speedup?
- Expected answer: 7.6

**C4:** What is Thingies task speedup?
- Expected answer: 2.4

**C5:** What is the sum of speedups?
- Expected answer: 21.2

**C6:** What is the average speedup ratio?
- Expected answer: 7.07

### Experience Adjustment (2 criteria)

**C7:** What is the complement of 45%?
- Expected answer: 0.55

**C8:** What is the Experience-Adjusted Method Placement Penalty?
- Expected answer: 3.89

### Comparison to Factory (3 criteria)

**C9:** What is Ellis factory penalty ratio?
- Expected answer: 2.09

**C10:** Which API design approach has greater cognitive cost?
- Expected answer: Helper class

**C11:** What is the ratio between them?
- Expected answer: 1.86

---

## Question 3: Cross-Study API Pattern Comparison (14 criteria)

### Table Format Verification (4 criteria)

**C1:** Does table have exact title specified?
- Expected answer: Yes

**C2:** How many data rows (excluding header)?
- Expected answer: 4

**C3:** How many columns?
- Expected answer: 5

**C4:** Are column headers exactly as specified?
- Expected answer: Yes

### Row 1: Factory Pattern (Ellis Data) - 4 criteria

**C5:** What is time penalty value?
- Expected answer: 2.09× or 2.1×

**C6:** What is failure rate value?
- Expected answer: 41.7%

**C7:** How many cognitive violations?
- Expected answer: 5

**C8:** What is primary issue?
- Expected answer: Discovery or Penetrability

### Row 2: Constructor Parameters (Stylos 2007) - 3 criteria

**C9:** What percentage avoided required constructors?
- Expected answer: 100%

**C10:** How many cognitive violations?
- Expected answer: 2 or 3

**C11:** What is primary issue?
- Expected answer: Premature Commitment

### Row 3: Helper Class Methods (Stylos & Myers 2008) - 3 criteria

**C12:** What is time penalty value?
- Expected answer: 11.2× or 7.07×

**C13:** How many cognitive violations?
- Expected answer: 3

**C14:** What is primary issue?
- Expected answer: Work-Step Unit or Penetrability

**FINAL VERIFICATION:** Total criteria count
- Expected: 40 criteria (13 + 13 + 14)

---

## Summary Statistics

- **Question 1:** 13 criteria (5 Ellis + 3 Clarke + 2 Factory calc + 3 Helper)
- **Question 2:** 13 criteria (2 Piccioni + 6 Stylos & Myers + 2 Adjustment + 3 Comparison)
- **Question 3:** 14 criteria (4 Format + 4 Row1 + 3 Row2 + 3 Row3)
- **Total:** 40 verification criteria

All criteria have answers ≤5 words as required.
