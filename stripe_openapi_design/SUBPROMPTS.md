# Sub-prompts for Stripe OpenAPI Specification Design Analysis

This file contains atomic sub-prompts for each analytical criterion (C1-C29). Table criteria (C30-C46) are evaluated by checking table structure, headers, and all cell values.

---

## Question 1: Expandable Field Distribution Analysis

Sub-prompt #1: How many schemas have 20 or more expandable fields?
Sub-prompt #1 Answer: 14

Sub-prompt #2: What is the schema name with the maximum expandable field count?
Sub-prompt #2 Answer: tax_product_registrations_resource_country_options

Sub-prompt #3: What is the exact expandable field count for the schema with maximum expandable fields?
Sub-prompt #3 Answer: 100

Sub-prompt #4: What percentage of schemas where ALL properties are expandable relative to schemas with at least one expandable field (rounded to 1 decimal place)?
Sub-prompt #4 Answer: 17.7%

---

## Question 2: Parameter Serialization Complexity

Sub-prompt #5: How many total query parameters exist across all operations?
Sub-prompt #5 Answer: 967

Sub-prompt #6: How many parameters use the deepObject serialization style?
Sub-prompt #6 Answer: 358

Sub-prompt #7: What percentage of query parameters use deepObject style (rounded to 1 decimal place)?
Sub-prompt #7 Answer: 37.0%

Sub-prompt #8: Which operation (HTTP method + path) has the maximum parameter count?
Sub-prompt #8 Answer: GET /v1/credit_notes/preview/lines

Sub-prompt #9: What is the exact parameter count for the operation with maximum parameters?
Sub-prompt #9 Answer: 17

Sub-prompt #10: Of all deepObject parameters, how many are specifically named "expand"?
Sub-prompt #10 Answer: 263

Sub-prompt #11: What is the ratio of operations with BOTH query parameters AND request body to total POST operations?
Sub-prompt #11 Answer: 263:310

---

## Question 3: Nullability Constraint Patterns

Sub-prompt #12: How many schemas have at least one nullable property?
Sub-prompt #12 Answer: 697

Sub-prompt #13: What is the schema name with the maximum nullable property count?
Sub-prompt #13 Answer: invoice

Sub-prompt #14: What is the exact nullable property count for the schema with maximum nullable properties?
Sub-prompt #14 Answer: 46

Sub-prompt #15: How many schemas have BOTH required fields AND nullable fields simultaneously?
Sub-prompt #15 Answer: 315

Sub-prompt #16: What percentage of schemas with nullable properties but NO required fields relative to total schemas with properties (rounded to 1 decimal place)?
Sub-prompt #16 Answer: 27.8%

Sub-prompt #17: How many nullable properties does the invoice schema have?
Sub-prompt #17 Answer: 46

Sub-prompt #18: How many required properties does the invoice schema have?
Sub-prompt #18 Answer: 29

Sub-prompt #19: How many nullable properties does the checkout.session schema have?
Sub-prompt #19 Answer: 45

Sub-prompt #20: How many required properties does the checkout.session schema have?
Sub-prompt #20 Answer: 12

---

## Question 4: Polymorphic Type Asymmetry

Sub-prompt #21: How many schemas use anyOf at least once?
Sub-prompt #21 Answer: 303

Sub-prompt #22: What is the schema name containing the property with the maximum anyOf option count?
Sub-prompt #22 Answer: balance_transaction

Sub-prompt #23: What is the property name with the maximum anyOf option count?
Sub-prompt #23 Answer: source

Sub-prompt #24: What is the exact anyOf option count for the property with maximum anyOf options?
Sub-prompt #24 Answer: 17

Sub-prompt #25: How many operations have anyOf in their request body schema?
Sub-prompt #25 Answer: 134

Sub-prompt #26: How many operations have anyOf in their response schema?
Sub-prompt #26 Answer: 15

Sub-prompt #27: What is the ratio of operations with anyOf in request to operations with anyOf in response?
Sub-prompt #27 Answer: 134:15

---

## Question 5: Resource Complexity Comparison Table

Note: Question 5 requires a table with 3 columns and 3 rows. The table criteria (C30-C46) are evaluated by checking:
- Table structure (presence, column count, row count, description, ordering)
- All column headers (3 headers)
- All cell values (3 rows × 3 columns = 9 cells)

These are verified directly against the expected table structure and not broken into separate sub-prompts, as they represent a single coherent table generation task.

---

## Criteria Mapping Summary

**Analytical Criteria (C1-C29):**
- **C1**: Sub-prompt #1 (Schemas with 20+ expandable = 14)
- **C2**: Sub-prompt #2 (Max expandable schema name)
- **C3**: Sub-prompt #3 (Max expandable count = 100)
- **C4**: Sub-prompt #4 (100% expandable percentage = 17.7%)
- **C5**: Sub-prompt #5 (Total query parameters = 967)
- **C6**: Sub-prompt #6 (DeepObject parameters = 358)
- **C7**: Sub-prompt #7 (DeepObject percentage = 37.0%)
- **C8**: Sub-prompt #8 (Max parameter operation)
- **C9**: Sub-prompt #9 (Max parameter count = 17)
- **C10**: Sub-prompt #10 (Expand deepObject count = 263)
- **C11**: Sub-prompt #11 (Dual-input ratio = 263:310)
- **C12**: Sub-prompt #12 (Schemas with nullable = 697)
- **C13**: Sub-prompt #13 (Max nullable schema name)
- **C14**: Sub-prompt #14 (Max nullable count = 46)
- **C15**: Sub-prompt #15 (Both nullable+required = 315)
- **C16**: Sub-prompt #16 (Nullable-no-required % = 27.8%)
- **C17**: Sub-prompt #17 (Invoice nullable = 46)
- **C18**: Sub-prompt #18 (Invoice required = 29)
- **C19**: Sub-prompt #19 (Checkout.session nullable = 45)
- **C20**: Sub-prompt #20 (Checkout.session required = 12)
- **C21**: Sub-prompt #21 (Schemas with anyOf = 303)
- **C22**: Sub-prompt #22 (Max anyOf schema name)
- **C23**: Sub-prompt #23 (Max anyOf property name)
- **C24**: Sub-prompt #24 (Max anyOf count = 17)
- **C25**: Sub-prompt #25 (AnyOf in request = 134)
- **C26**: Sub-prompt #26 (AnyOf in response = 15)
- **C27**: Sub-prompt #27 (AnyOf ratio = 134:15)
- **C28**: Explains expandable field tradeoff
- **C29**: Explains dual-input OR nullable+required OR polymorphic asymmetry tradeoffs

**Table Criteria (C30-C46):**
- **C30**: Table presence
- **C31**: Table has 3 columns
- **C32**: Table has 3 data rows
- **C33**: Describes table structure before presenting
- **C34**: Rows ordered highest to lowest by expandable count
- **C35**: "Resource ID" column header
- **C36**: "Expandable Fields" column header
- **C37**: "Expandability Ratio" column header
- **C38**: Row 1 - Resource ID = payment_method
- **C39**: Row 1 - Expandable Fields = 56
- **C40**: Row 1 - Expandability Ratio = 87.5%
- **C41**: Row 2 - Resource ID = payment_method_configuration
- **C42**: Row 2 - Expandable Fields = 54
- **C43**: Row 2 - Expandability Ratio = 87.1%
- **C44**: Row 3 - Resource ID = checkout.session
- **C45**: Row 3 - Expandable Fields = 34
- **C46**: Row 3 - Expandability Ratio = 51.5%

Total analytical sub-prompts: 27 factual + 2 explanation = 29
Total table criteria: 5 structure + 3 headers + 9 cells = 17
**Total criteria: 46**
