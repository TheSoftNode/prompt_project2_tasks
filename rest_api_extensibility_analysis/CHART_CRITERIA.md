# Chart Criteria for Question 3: REST API Extension Mechanisms Comparison

This document defines the evaluation criteria for the grouped bar chart in Question 3.

---

## Chart Requirements

**Question 3** asks for: "Create a grouped bar chart comparing extensibility metrics across four REST API extension mechanisms. The chart must display 4 groups with 2 bars each (blue for Extensibility Index, red for Backward Compatibility Score), specific axis labels, intervals, and a title."

---

## Structural Criteria (5 criteria: C23-C27)

### CRITERION 23 [Chart Structure]
**Description:** Response contains a bar chart (image) for Question 3.

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Question 3 explicitly requires creating a grouped bar chart comparing extension mechanisms. The presence of a chart image (as PNG, SVG, or rendered visualization) is mandatory for answering this question. Without a chart, the comparative data cannot be properly presented or evaluated.

**Sources:** Not applicable - structural requirement

---

### CRITERION 24 [Chart Structure]
**Description:** Chart displays exactly 4 groups on the X-axis.

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Question 3 specifies comparing exactly four extension mechanisms: Plugins, Middleware, Webhooks, and Versioning. The chart must have 4 distinct groups. More or fewer groups fails to meet the specification.

**Sources:** Not applicable - structural requirement

---

### CRITERION 25 [Chart Structure]
**Description:** Each group contains exactly 2 bars (grouped/side-by-side).

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** The chart must be a grouped bar chart with two bars per mechanism: one for Extensibility Index and one for Backward Compatibility Score. This allows direct visual comparison of both metrics across all mechanisms.

**Sources:** Not applicable - structural requirement

---

### CRITERION 26 [Chart Structure]
**Description:** Chart includes a title "REST API Extension Mechanisms: Comparative Analysis".

**Weight:** Major

**Numerical Weight:** 4

**Rationale:** Question 3 explicitly specifies this exact title must be positioned above the chart. The title provides context for the comparison.

**Sources:** Not applicable - structural requirement

---

### CRITERION 27 [Chart Structure]
**Description:** Chart includes a legend identifying blue and red bars.

**Weight:** Major

**Numerical Weight:** 4

**Rationale:** Question 3 requires a legend identifying blue bars as "Extensibility Index" and red bars as "Backward Compatibility Score". This is essential for chart readability.

**Sources:** Not applicable - structural requirement

---

## Axis Criteria (4 criteria: C28-C31)

### CRITERION 28 [Chart Axes]
**Description:** X-axis displays the four mechanisms in exact order: Plugins, Middleware, Webhooks, Versioning.

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Question 3 specifies this precise ordering of the extension mechanisms. Correct ordering ensures consistent interpretation of results.

**Sources:** Not applicable - structural requirement

---

### CRITERION 29 [Chart Axes]
**Description:** X-axis is labeled with mechanism names (Plugins, Middleware, Webhooks, Versioning).

**Weight:** Major

**Numerical Weight:** 4

**Rationale:** Each group on the X-axis must be clearly labeled with the corresponding mechanism name for interpretation.

**Sources:** Not applicable - structural requirement

---

### CRITERION 30 [Chart Axes]
**Description:** Y-axis is labeled "Extensibility & Compatibility Score".

**Weight:** Major

**Numerical Weight:** 4

**Rationale:** Question 3 specifies this exact Y-axis label. It describes what the bar heights represent.

**Sources:** Not applicable - structural requirement

---

### CRITERION 31 [Chart Axes]
**Description:** Y-axis scale ranges from 0 to 100 with intervals at 0, 20, 40, 60, 80, 100.

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Question 3 explicitly specifies the Y-axis scale and interval marks. This ensures proper visual representation of the scores.

**Sources:** Not applicable - structural requirement

---

## Color Criteria (2 criteria: C32-C33)

### CRITERION 32 [Chart Appearance]
**Description:** Extensibility Index bars are displayed in blue color.

**Weight:** Major

**Numerical Weight:** 4

**Rationale:** Question 3 specifies blue bars for Extensibility Index. Color coding enables quick visual distinction between the two metrics.

**Sources:** Not applicable - structural requirement

---

### CRITERION 33 [Chart Appearance]
**Description:** Backward Compatibility Score bars are displayed in red color.

**Weight:** Major

**Numerical Weight:** 4

**Rationale:** Question 3 specifies red bars for Backward Compatibility Score. This color differentiation is essential for chart interpretation.

**Sources:** Not applicable - structural requirement

---

## Data Accuracy Criteria - Group 1: Plugins (2 criteria: C34-C35)

### CRITERION 34 [Chart Data]
**Description:** Blue bar for Plugins reaches approximately 1200-1220 on Y-axis.

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Source: Calculated Extensibility Index for Plugins = 1214 (from C16). The blue bar height must accurately represent this value on the 0-100 scale. However, since 1214 exceeds 100, the chart should either (a) scale values proportionally or (b) indicate values above the axis. The bar should visually represent the relative magnitude correctly.

**Sources:** Calculated in Question 2: (85 × 100) ÷ 7 = 1214

---

### CRITERION 35 [Chart Data]
**Description:** Red bar for Plugins reaches 85 on Y-axis.

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Source: Queluz & Filho (2016), Table 3. Plugins showed 85% backward compatibility in the SDN evaluation. The red bar must reach the 85 mark on the Y-axis (between 80 and 100 interval marks).

**Sources:** https://ieeexplore.ieee.org/abstract/document/7844664 (Table 3, Plugin compatibility data)

---

## Data Accuracy Criteria - Group 2: Middleware (2 criteria: C36-C37)

### CRITERION 36 [Chart Data]
**Description:** Blue bar for Middleware reaches approximately 3060-3070 on Y-axis (or proportionally scaled).

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Source: Calculated Extensibility Index for Middleware = 3067 (from C17). The blue bar must accurately represent this value, which is the highest among all mechanisms.

**Sources:** Calculated in Question 2: (92 × 100) ÷ 3 = 3067

---

### CRITERION 37 [Chart Data]
**Description:** Red bar for Middleware reaches 92 on Y-axis.

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Source: Witanto et al. (2018), Section 4.2. Middleware mechanisms achieved 92% backward compatibility, the highest among all tested mechanisms. The red bar must reach the 92 mark (between 80 and 100).

**Sources:** https://ieeexplore.ieee.org/abstract/document/7378522 (Section 4.2, Middleware evaluation)

---

## Data Accuracy Criteria - Group 3: Webhooks (2 criteria: C38-C39)

### CRITERION 38 [Chart Data]
**Description:** Blue bar for Webhooks reaches approximately 1950 on Y-axis (or proportionally scaled).

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Source: Calculated Extensibility Index for Webhooks = 1950 (from C18). The blue bar must accurately represent this mid-range value.

**Sources:** Calculated in Question 2: (78 × 100) ÷ 4 = 1950

---

### CRITERION 39 [Chart Data]
**Description:** Red bar for Webhooks reaches 78 on Y-axis.

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Source: Witanto et al. (2018), Section 4.2. Webhooks showed 78% backward compatibility. The red bar must reach the 78 mark (between 60 and 80 interval marks).

**Sources:** https://ieeexplore.ieee.org/abstract/document/7378522 (Section 4.2, Webhook compatibility)

---

## Data Accuracy Criteria - Group 4: Versioning (2 criteria: C40-C41)

### CRITERION 40 [Chart Data]
**Description:** Blue bar for Versioning reaches approximately 4750 on Y-axis (or proportionally scaled).

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Source: Calculated Extensibility Index for Versioning = 4750 (from C19). This is the highest extensibility index, and the blue bar must be the tallest among all blue bars.

**Sources:** Calculated in Question 2: (95 × 100) ÷ 2 = 4750

---

### CRITERION 41 [Chart Data]
**Description:** Red bar for Versioning reaches 95 on Y-axis.

**Weight:** Critical

**Numerical Weight:** 5

**Rationale:** Source: Queluz & Filho (2016), Table 3. Versioning achieved 95% backward compatibility, the highest score. The red bar must reach 95 (between 80 and 100, very close to the top).

**Sources:** https://ieeexplore.ieee.org/abstract/document/7844664 (Table 3, Versioning compatibility)

---

## Visual Correctness Criterion (C42)

### CRITERION 42 [Chart Data]
**Description:** Relative bar heights correctly represent the data magnitude relationships.

**Weight:** Major

**Numerical Weight:** 4

**Rationale:** Even if absolute scaling is adjusted, the relative heights must be correct: For blue bars (Extensibility Index): Versioning > Middleware > Webhooks > Plugins. For red bars (Compatibility): Versioning (95) > Middleware (92) > Plugins (85) > Webhooks (78).

**Sources:** All calculated and empirical values from Q2

---

## Summary

**Total Criteria: 20**

- **Structural Criteria (C23-C27)**: 5 criteria
  - C23: Chart image present (Critical, 5 points)
  - C24: 4 groups on X-axis (Critical, 5 points)
  - C25: 2 bars per group (Critical, 5 points)
  - C26: Title present (Major, 4 points)
  - C27: Legend present (Major, 4 points)

- **Axis Criteria (C28-C31)**: 4 criteria
  - C28: X-axis order correct (Critical, 5 points)
  - C29: X-axis labels present (Major, 4 points)
  - C30: Y-axis label correct (Major, 4 points)
  - C31: Y-axis scale 0-100, intervals 20 (Critical, 5 points)

- **Color Criteria (C32-C33)**: 2 criteria
  - C32: Blue bars for Extensibility Index (Major, 4 points)
  - C33: Red bars for Compatibility Score (Major, 4 points)

- **Data Accuracy: Plugins (C34-C35)**: 2 criteria
  - C34: Blue bar ≈ 1214 (Critical, 5 points)
  - C35: Red bar = 85 (Critical, 5 points)

- **Data Accuracy: Middleware (C36-C37)**: 2 criteria
  - C36: Blue bar ≈ 3067 (Critical, 5 points)
  - C37: Red bar = 92 (Critical, 5 points)

- **Data Accuracy: Webhooks (C38-C39)**: 2 criteria
  - C38: Blue bar ≈ 1950 (Critical, 5 points)
  - C39: Red bar = 78 (Critical, 5 points)

- **Data Accuracy: Versioning (C40-C41)**: 2 criteria
  - C40: Blue bar ≈ 4750 (Critical, 5 points)
  - C41: Red bar = 95 (Critical, 5 points)

- **Visual Correctness (C42)**: 1 criterion
  - C42: Relative heights correct (Major, 4 points)

**Weight Distribution:**
- Critical (5 points): 13 criteria
- Major (4 points): 7 criteria

**Total Possible Points: 93**
