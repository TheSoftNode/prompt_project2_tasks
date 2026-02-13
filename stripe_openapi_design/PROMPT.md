# Stripe OpenAPI Specification Design Analysis

**Subdomain:** API Design

**Routing:** Scratch

---

## Main Prompt

Consider the stripe/openapi repository on GitHub, specifically the OpenAPI v3 specification in the `/latest/` directory, as of February 3, 2026. Stripe's API specification demonstrates sophisticated design patterns through vendor extensions, parameter serialization strategies, and field expandability mechanisms. API designers face inherent tradeoffs between resource expansion capabilities (reducing roundtrips vs response bloat), nullability constraints (flexibility vs contract clarity), polymorphic type handling (request simplicity vs response type safety), and parameter serialization complexity (nested object support vs URL encoding limitations).

Review the Stripe OpenAPI specification to quantify API design decisions and their implications. Provide the following:

**Question 1: Expandable Field Distribution Analysis**
Stripe uses the vendor extension `x-expandableFields` to mark fields that can be expanded via the `expand` query parameter, allowing clients to control response granularity. Count how many schemas have 20 or more expandable fields. Identify the schema with the maximum expandable field count and state the exact count. Calculate the percentage of schemas where ALL properties are expandable (expandable fields count equals total properties count) relative to schemas with at least one expandable field. Explain what API design tradeoff this "100% expandable" pattern represents (response customization flexibility vs implementation complexity).

**Question 2: Parameter Serialization Complexity**
OpenAPI supports different parameter serialization styles. Count the total query parameters across all operations. Count parameters using the `deepObject` style and calculate the percentage relative to total query parameters. Identify the operation (HTTP method + path) with the maximum parameter count and state the exact count. Of all parameters using `deepObject` style, count how many are specifically named `expand`. Calculate the ratio of operations accepting BOTH query parameters AND request body to total POST operations, and explain what API design tradeoff this dual-input pattern represents (input source multiplicity vs interface simplicity).

**Question 3: Nullability Constraint Patterns**
API schemas must specify which fields are required, optional, or nullable. Count schemas with at least one nullable property. Identify the schema with the maximum nullable property count and state the exact count. Count schemas having BOTH required fields AND nullable fields simultaneously. Calculate the percentage of schemas with nullable properties but NO required fields relative to total schemas containing properties. For the `invoice` and `checkout.session` schemas specifically, state their nullable property counts and required property counts, then explain what API design philosophy the coexistence of nullable and required fields represents (defensive programming vs strict contracts).

**Question 4: Polymorphic Type Asymmetry**
Stripe uses `anyOf` for polymorphic types that can accept or return multiple types. Count schemas using `anyOf` at least once. Identify the property with the maximum `anyOf` option count, stating the schema name, property name, and exact option count. Count operations with `anyOf` in their request body schema versus response schema. Calculate the request-to-response ratio and explain what API design constraint causes this asymmetry (client input validation flexibility vs server output type guarantees).

**Question 5: Resource Complexity Comparison Table**
Create a resource complexity comparison table with exactly 3 columns: "Resource ID", "Expandable Fields", "Expandability Ratio". Include exactly 3 data rows containing the 3 resources (by `x-resourceId`) with the highest expandable field counts, ordered from highest to lowest by expandable field count. For "Expandable Fields", count fields listed in `x-expandableFields` for the primary schema with that `x-resourceId`. For "Expandability Ratio", calculate (Expandable Fields / Total Properties) as a percentage with 1 decimal place. Before the table, describe its structure (column count, row count, column names, ordering criterion).

## Citations

[1] stripe/openapi. "Stripe OpenAPI Specification - Latest GA Release." _latest/openapi.spec3.yaml_, commit 38f2785cfd2cc036c10e68d4c25e7be3a26ca927. GitHub. https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

[2] stripe/openapi. "Stripe OpenAPI Specification - Latest GA Release (JSON)." _latest/openapi.spec3.json_, commit 38f2785cfd2cc036c10e68d4c25e7be3a26ca927. GitHub. https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.json

[3] stripe/openapi. "OpenAPI Repository README." _README.md_, commit 38f2785cfd2cc036c10e68d4c25e7be3a26ca927. GitHub. https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/README.md
