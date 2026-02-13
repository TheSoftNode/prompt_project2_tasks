# Sub-prompts for REST API Extensibility Analysis

This file contains atomic sub-prompts for each analytical criterion. Each sub-prompt corresponds to a specific verifiable answer from the papers.

---

## Question 1: SDN REST API Empirical Evaluation (C1-C10)

**Sub-prompt #1:** How many distinct REST endpoints were implemented in the evaluated SDN controller?
**Sub-prompt #1 Answer:** 28 endpoints

**Sub-prompt #2:** What is the exact average response time (in milliseconds) for GET requests under 1000 concurrent connections?
**Sub-prompt #2 Answer:** 47 ms

**Sub-prompt #3:** What is the exact average response time (in milliseconds) for POST requests under 1000 concurrent connections?
**Sub-prompt #3 Answer:** 89 ms

**Sub-prompt #4:** What specific versioning strategy was employed in the SDN REST API?
**Sub-prompt #4 Answer:** URI path versioning (e.g., /api/v1/, /api/v2/)

**Sub-prompt #5:** What is the backward compatibility retention period?
**Sub-prompt #5 Answer:** 18 months (or 3 major versions)

**Sub-prompt #6:** What is the first most frequently invoked endpoint?
**Sub-prompt #6 Answer:** /flows (flow table queries)

**Sub-prompt #7:** What is the request frequency percentage for the first endpoint?
**Sub-prompt #7 Answer:** 42%

**Sub-prompt #8:** What is the second most frequently invoked endpoint?
**Sub-prompt #8 Answer:** /topology (network topology requests)

**Sub-prompt #9:** What is the request frequency percentage for the second endpoint?
**Sub-prompt #9 Answer:** 28%

**Sub-prompt #10:** What is the third most frequently invoked endpoint?
**Sub-prompt #10 Answer:** /stats (statistics queries)

---

## Question 2: Design Decision Mapping & Analysis (C11-C22)

**Sub-prompt #11:** What is the complete design decision path for SDN REST APIs?
**Sub-prompt #11 Answer:** D1→Stateless, D2→Resource-oriented, D3→Uniform interface, D4→Self-descriptive messages, D5→HATEOAS partial, D6→JSON representation

**Sub-prompt #12:** What is the first contradiction regarding error handling between the two papers?
**Sub-prompt #12 Answer:** REST extensibility paper recommends verbose error responses with stack traces for debugging; SDN patterns paper recommends minimal error information to prevent security information leakage

**Sub-prompt #13:** What is the second contradiction regarding error handling?
**Sub-prompt #13 Answer:** REST extensibility paper advocates for custom error codes (e.g., 4XX custom); SDN patterns paper mandates strict adherence to standard HTTP status codes only

**Sub-prompt #14:** What is the Backward Compatibility Percentage for Plugins?
**Sub-prompt #14 Answer:** 85%

**Sub-prompt #15:** What is the Adoption Effort Score for Plugins?
**Sub-prompt #15 Answer:** 7 (complex integration)

**Sub-prompt #16:** What is the calculated Extensibility Index for Plugins?
**Sub-prompt #16 Answer:** (85 × 100) ÷ 7 = 1214.3 (rounded to 1214)

**Sub-prompt #17:** What is the Extensibility Index for Middleware?
**Sub-prompt #17 Answer:** (92 × 100) ÷ 3 = 3066.7 (rounded to 3067)

**Sub-prompt #18:** What is the Extensibility Index for Webhooks?
**Sub-prompt #18 Answer:** (78 × 100) ÷ 4 = 1950

**Sub-prompt #19:** What is the Extensibility Index for Versioning?
**Sub-prompt #19 Answer:** (95 × 100) ÷ 2 = 4750

**Sub-prompt #20:** What HTTP status code is recommended for rate limiting?
**Sub-prompt #20 Answer:** 429 Too Many Requests

**Sub-prompt #21:** What HTTP status code is recommended for authentication failure?
**Sub-prompt #21 Answer:** 401 Unauthorized

**Sub-prompt #22:** What HTTP status code is recommended for authorization failure (authenticated but forbidden)?
**Sub-prompt #22 Answer:** 403 Forbidden

---

## Question 3: Grouped Bar Chart (C23-C42)

Note: Chart criteria with 20 specific evaluation points are documented in CHART_CRITERIA.md.

---

## Criteria Mapping Summary

**Analytical Criteria (C1-C22):**

- **C1**: Sub-prompt #1 (Endpoints = 28)
- **C2**: Sub-prompt #2 (GET response time = 47 ms)
- **C3**: Sub-prompt #3 (POST response time = 89 ms)
- **C4**: Sub-prompt #4 (Versioning = URI path)
- **C5**: Sub-prompt #5 (Retention = 18 months)
- **C6**: Sub-prompt #6 (Endpoint 1 = /flows)
- **C7**: Sub-prompt #7 (Frequency 1 = 42%)
- **C8**: Sub-prompt #8 (Endpoint 2 = /topology)
- **C9**: Sub-prompt #9 (Frequency 2 = 28%)
- **C10**: Sub-prompt #10 (Endpoint 3 = /stats)
- **C11**: Sub-prompt #11 (Design decision path)
- **C12**: Sub-prompt #12 (Contradiction 1 = error verbosity)
- **C13**: Sub-prompt #13 (Contradiction 2 = custom vs standard codes)
- **C14**: Sub-prompt #14 (Plugins backward compat = 85%)
- **C15**: Sub-prompt #15 (Plugins adoption = 7)
- **C16**: Sub-prompt #16 (Plugins index = 1214)
- **C17**: Sub-prompt #17 (Middleware index = 3067)
- **C18**: Sub-prompt #18 (Webhooks index = 1950)
- **C19**: Sub-prompt #19 (Versioning index = 4750)
- **C20**: Sub-prompt #20 (Rate limit code = 429)
- **C21**: Sub-prompt #21 (Auth failure code = 401)
- **C22**: Sub-prompt #22 (Authorization failure code = 403)

**Chart Criteria (C23-C42):**

- **C23-C42**: Documented in CHART_CRITERIA.md (20 criteria for the grouped bar chart)

**Total analytical sub-prompts: 22**

- Q1: 10 sub-prompts (C1-C10)
- Q2: 12 sub-prompts (C11-C22)
- Q3: Chart with 20 criteria documented in CHART_CRITERIA.md

**Grand Total: 42 criteria** (22 analytical + 20 chart)
