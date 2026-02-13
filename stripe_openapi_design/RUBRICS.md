# RUBRICS - Stripe OpenAPI Specification Design Analysis - 46 Criteria

## Overview
- **Total Criteria**: 46 (all positive)
- **Domain**: API Design - OpenAPI Specification Analysis
- **Repository**: stripe/openapi
- **Commit**: 38f2785cfd2cc036c10e68d4c25e7be3a26ca927
- **Task Type**: Research & Analysis (Scratch Routing)

---

## CRITERION 1 [Accuracy]
**Description:** States 14 as the count of schemas with 20 or more expandable fields.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** Counting schemas in the OpenAPI specification where the `x-expandableFields` array has length ≥ 20 yields exactly 14 schemas. These represent resources with extensive relationship networks requiring selective expansion capabilities, such as `payment_method` (56 expandable fields), `payment_method_configuration` (54 fields), and tax registration schemas. The 20-field threshold identifies resources where expansion control becomes critical for API performance optimization, as loading all related entities without selective expansion would result in excessive data transfer and query overhead.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 2 [Accuracy]
**Description:** Identifies "tax_product_registrations_resource_country_options" as the schema with maximum expandable fields.
**Weight:** Major
**Numerical Weight:** 4
**Rationale:** Among all 1,468 schemas in the specification, the schema named `tax_product_registrations_resource_country_options` has the highest count in its `x-expandableFields` array. This schema represents tax registration configuration options across 100+ countries, where each country-specific property (`ad` for Andorra, `ae` for UAE, `ar` for Argentina, etc.) can reference detailed regulatory requirement objects. This extensive expandability reflects Stripe's global tax compliance requirements where registration rules vary significantly by jurisdiction, requiring selective loading to avoid overwhelming API responses with unnecessary country configurations.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 3 [Accuracy]
**Description:** States 100 as the exact expandable field count for the schema with maximum expandable fields.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** The `tax_product_registrations_resource_country_options` schema's `x-expandableFields` array contains exactly 100 entries. Each entry represents a country code property (ISO 3166-1 alpha-2) that can be expanded to retrieve full tax registration configuration objects for that jurisdiction. The 100-field count represents comprehensive global coverage and demonstrates the extreme case of Stripe's expandability pattern where every single property is individually controllable through the `expand` parameter.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 4 [Accuracy]
**Description:** States 17.7% as the percentage of schemas where ALL properties are expandable.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** Of 553 schemas containing at least one expandable field, exactly 98 schemas exhibit the "100% expandable" pattern where `length(x-expandableFields) == length(properties)`. The percentage calculation: 98/553 = 17.72%, rounded to 17.7%. This pattern occurs when schemas serve primarily as relationship aggregators rather than data containers, with every property referencing another resource rather than containing inline scalar values. Examples include association tables, configuration containers, and navigation objects that exist solely to organize relationships between core entities.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 5 [Accuracy]
**Description:** States 967 as the total query parameter count across all operations.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** Summing all parameters where `in: "query"` across all 588 operations in 436 paths yields 967 total query parameters. This comprehensive count includes pagination parameters (limit, starting_after, ending_before), filtering parameters for list operations, expansion parameters for selective field loading, created/date range filters, metadata search parameters, and status filters. The high count reflects Stripe's extensive API surface with granular control over resource listing, filtering, and retrieval operations.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 6 [Accuracy]
**Description:** States 358 as the count of parameters using deepObject serialization style.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** Counting parameters with `style: deepObject` yields 358 parameters. The deepObject serialization style enables complex nested object structures in URL query strings through bracket notation (e.g., `created[gte]=1609459200&created[lt]=1640995200` for date ranges, `metadata[order_id]=ord_123&metadata[user_type]=premium` for metadata filtering). This style is essential for Stripe's filtering patterns where structured criteria must be passed via GET requests without requiring request bodies for read operations.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 7 [Accuracy]
**Description:** States 37.0% as the percentage of query parameters using deepObject style.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** The ratio 358/967 = 37.01%, rounded to 37.0%. This substantial percentage demonstrates that over one-third of all query parameters require nested object representation through deepObject serialization. The high percentage reflects Stripe's design philosophy of providing rich filtering capabilities on GET endpoints, where simple key-value parameters prove insufficient for expressing complex filter criteria like date ranges, metadata queries, numerical comparisons, and multi-field filtering conditions.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 8 [Accuracy]
**Description:** Identifies "GET /v1/credit_notes/preview/lines" as the operation with maximum parameter count.
**Weight:** Major
**Numerical Weight:** 4
**Rationale:** Among all 588 operations across all paths, `GET /v1/credit_notes/preview/lines` has the highest query parameter count. This operation generates previews of credit note line items before actual creation, simulating the crediting calculation without persisting data. The operation requires extensive parameters to specify: which invoice to credit (invoice), which specific lines to credit (lines array with item/type/amount), credit note parameters (credit_amount, reason, memo), shipping cost adjustments (shipping_cost), pagination (limit, starting_after, ending_before), and field expansion (expand array). This complexity reflects the preview operation's need to simulate complete credit note creation logic.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 9 [Accuracy]
**Description:** States 17 as the exact parameter count for the operation with maximum parameters.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** The `GET /v1/credit_notes/preview/lines` operation's parameter list contains exactly 17 query parameters. This represents the upper bound of parameter complexity in Stripe's API design, balancing comprehensive control over preview calculations with API usability. Beyond 17 parameters, Stripe's design philosophy suggests that operations should be decomposed into smaller operations or accept structured request bodies rather than continuing to add query parameters.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 10 [Accuracy]
**Description:** States 263 as the count of deepObject parameters specifically named "expand".
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** Of the 358 deepObject parameters, exactly 263 have `name: "expand"`. This represents 73.5% (263/358) of deepObject parameters dedicated exclusively to resource expansion control. The expand parameter appears in nearly every GET operation and many POST operations, using deepObject style with `explode: true` to accept array values like `expand[]=customer&expand[]=subscription&expand[]=charges.data.balance_transaction`, enabling clients to selectively load related resources through nested dot notation for deep expansion of relationship chains.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 11 [Accuracy]
**Description:** States 263:310 as the ratio of operations with both query parameters and request body to total POST operations.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** Of 310 total POST operations, 263 accept both query parameters (typically expand, limit, and filtering parameters) and request body (resource creation/mutation data). The ratio 263:310 represents 84.8% of POST operations supporting dual-input sources. This pattern enables operations like `POST /v1/customers?expand[]=subscriptions&expand[]=sources` where the request body creates/updates the customer resource while query parameters control the response shape, pagination of nested lists, and selective loading of relationships. This dual-input pattern maximizes developer convenience by avoiding the need for subsequent GET requests to retrieve expanded data after mutations.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 12 [Accuracy]
**Description:** States 697 as the count of schemas with at least one nullable property.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** Counting schemas where at least one property has `nullable: true` yields 697 schemas out of 1,468 total schemas (47.5%). This extensive nullability reflects Stripe's design philosophy of explicitly modeling semantic absence through null values rather than field omission. Nullable fields enable API consumers to distinguish between "field not applicable in this context" (null value present) versus "field not yet loaded/expanded" (field absent from response), providing clearer semantics than omission-based optionality.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 13 [Accuracy]
**Description:** Identifies "invoice" as the schema with maximum nullable property count.
**Weight:** Major
**Numerical Weight:** 4
**Rationale:** Among all schemas with nullable properties, the `invoice` schema has the highest count of properties marked `nullable: true`. The invoice schema serves as a central aggregation point for numerous optional business relationships that may or may not exist depending on the invoice's creation context, payment lifecycle stage, and business model. Nullable relationships include: customer (may be deleted), subscription (one-time invoices have no subscription), payment_intent (not yet created for draft invoices), charge (unpaid invoices have no charge), discount (may be removed), default_payment_method (customer may have none), and many others representing contextual associations with valid null semantics.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 14 [Accuracy]
**Description:** States 46 as the exact nullable property count for the schema with maximum nullable properties.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** The `invoice` schema has exactly 46 properties with `nullable: true`. These represent optional relationships spanning customer management (customer, account_name, customer_email, customer_phone), subscription lifecycle (subscription, subscription_details), payment processing (payment_intent, charge, default_payment_method, default_source), discounts (discount, discounts), tax (tax, default_tax_rates, customer_tax_ids), application fees (application, application_fee_amount), and financial associations (on_behalf_of, transfer_data), all of which may validly be null in different invoice contexts.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 15 [Accuracy]
**Description:** States 315 as the count of schemas with BOTH required fields AND nullable fields.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** Counting schemas that have both a non-empty `required` array AND at least one nullable property yields 315 schemas. This pattern is semantically valid and intentional in OpenAPI design: required fields must be present in responses but may have null values (explicitly unset or inapplicable states), while optional fields may be absent entirely. For example, `invoice.customer` is required (field must exist in all invoice responses) and nullable (value may be null if the customer was deleted), enabling clients to distinguish "no customer" (null) from "customer relationship not loaded" (field absent when not expanded).
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 16 [Accuracy]
**Description:** States 27.8% as the percentage of schemas with nullable properties but NO required fields.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** Of 1,374 schemas containing at least one property, 382 have nullable properties but empty `required` arrays. The ratio 382/1,374 = 27.80%. This indicates over one-quarter of schemas adopt fully optional structures where all fields may be absent or null. These typically represent auxiliary data structures like metadata container objects, configuration option bundles, supplementary information schemas providing contextual data, nested parameter objects for mutations, and response modifier schemas that lack mandatory fields.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 17 [Accuracy]
**Description:** States 46 as the invoice schema's nullable property count.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** Counting properties in the `invoice` schema where `nullable: true` yields exactly 46 properties. This matches the maximum nullable count identified in Criterion 13, confirming invoice has the most extensive nullable property set in Stripe's OpenAPI specification. The 46 nullable properties span all major functional domains: customer relationships, subscription associations, payment processing entities, tax calculations, discount applications, and financial reporting linkages.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 18 [Accuracy]
**Description:** States 29 as the invoice schema's required property count.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** The `invoice` schema's `required` array contains exactly 29 property names. These represent core invoice fields that must always be present in responses regardless of context: identity fields (id, object, livemode), financial amounts (amount_due, amount_paid, amount_remaining, subtotal, total), currency, status, timestamps (created, due_date, period_start, period_end), boolean flags (attempted, paid, auto_advance), and fundamental invoice attributes that define the invoice's state independent of its relationships.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 19 [Accuracy]
**Description:** States 45 as the checkout.session schema's nullable property count.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** Counting properties in the `checkout.session` schema where `nullable: true` yields exactly 45 properties. Checkout sessions have nearly as many nullable properties as invoices (45 vs 46), reflecting the session's flexible, ephemeral nature. Nullable properties vary based on payment mode (payment/setup/subscription), UI customization choices (custom_text, shipping_address_collection), post-payment automation (after_expiration, consent_collection), subscription settings (subscription_data), and shipping requirements (shipping_cost, shipping_details), all contextually null based on session configuration.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 20 [Accuracy]
**Description:** States 12 as the checkout.session schema's required property count.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** The `checkout.session` schema's `required` array contains exactly 12 property names. This is significantly fewer than invoice's 29 required fields, reflecting checkout session's more flexible contract designed for diverse e-commerce scenarios. Required fields include: id, object, created, livemode (identity/metadata), mode (payment/setup/subscription), status (open/complete/expired), url (redirect target), and expiration timestamps (expires_at) - the minimal set needed to identify and interact with a session regardless of configuration.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 21 [Accuracy]
**Description:** States 303 as the count of schemas using anyOf at least once.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** Counting schemas that contain `anyOf` anywhere in their definition (including nested properties, array items, and transitively referenced schemas) yields 303 schemas. The anyOf construct enables polymorphic type definitions where a property can accept or return multiple alternative types, supporting Stripe's pattern of accepting flexible input formats (string IDs or full object representations) while documenting precise output type possibilities for proper client code generation and type safety.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 22 [Accuracy]
**Description:** Identifies "balance_transaction" as the schema containing the property with maximum anyOf option count.
**Weight:** Major
**Numerical Weight:** 4
**Rationale:** After recursively searching all properties across all 1,468 schemas for anyOf usage and counting options, the property with the most anyOf alternatives is located in the `balance_transaction` schema. Balance transactions serve as Stripe's universal ledger entries, recording all balance-affecting events across the entire platform. This requires polymorphic typing to reference any of numerous possible source types: charges, refunds, payouts, application fees, transfers, disputes, adjustments, and many other financial event types that modify account balances.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 23 [Accuracy]
**Description:** Identifies "source" as the property name with maximum anyOf option count.
**Weight:** Major
**Numerical Weight:** 4
**Rationale:** Within the `balance_transaction` schema, the property named `source` has the maximum anyOf count across the entire specification. The source property identifies which specific financial event created this ledger entry, requiring comprehensive polymorphic typing to reference: charge objects (card/bank payments), refund objects (payment returns), payout objects (bank transfers out), application_fee objects (platform fees), transfer objects (connected account transfers), dispute objects (chargeback events), reserve_transaction objects (held funds), issuing_authorization/issuing_transaction objects (card activity), and other balance-affecting resource types, plus a string type for ID-only references.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 24 [Accuracy]
**Description:** States 17 as the exact anyOf option count for the property with maximum anyOf options.
**Weight:** Minor
**Numerical Weight:** 3
**Rationale:** The `balance_transaction.source` property's anyOf array contains exactly 17 options. These represent references to 16 different resource type schemas (charge, refund, payout, application_fee, transfer, topup, reversal, dispute, reserve_transaction, connect_collection_transfer, issuing_authorization, issuing_transaction, issuing_dispute, adjustment, platform_earning, platform_tax), plus one string type for ID-only references. The 17-option count represents Stripe's complete taxonomy of balance-affecting events that can appear in ledgers.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 25 [Accuracy]
**Description:** States 134 as the count of operations with anyOf in request body schema.
**Weight:** Major
**Numerical Weight:** 4
**Rationale:** Counting operations where `anyOf` appears anywhere in the request body schema (including nested references and array items) yields 134 operations. Request-side polymorphism enables flexible client input where multiple alternative structures are acceptable. Examples include accepting either "pm_card_123" string or {type: "card", card: {number: "4242...", exp_month: 12, exp_year: 2025}} object for payment methods, accepting either "price_abc" or inline {unit_amount: 1000, currency: "usd"} for prices, maximizing developer convenience by avoiding client-side type discrimination requirements before API calls.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 26 [Accuracy]
**Description:** States 15 as the count of operations with anyOf in response schema.
**Weight:** Major
**Numerical Weight:** 4
**Rationale:** Counting operations where `anyOf` appears anywhere in response schemas (including nested object properties and list items) yields only 15 operations. Response-side polymorphism is intentionally minimized because servers should provide predictable, strongly-typed output structures that clients can safely parse without extensive runtime type discrimination. The 15 operations with response anyOf represent special cases: list endpoints returning heterogeneous item types (e.g., /v1/events with different event type data structures), union type responses with clear discriminator fields (object: "charge" vs object: "payment_intent"), or webhook payloads containing diverse data objects.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 27 [Accuracy]
**Description:** States 134:15 as the ratio of operations with anyOf in request to operations with anyOf in response.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** The ratio 134:15 (approximately 9:1) demonstrates significant polymorphic type asymmetry strongly favoring request-side flexibility over response-side polymorphism. This asymmetry ratio embodies Postel's Law applied to API design: "be liberal in what you accept, conservative in what you send." Stripe accepts diverse input formats (9× more polymorphic operations) to maximize developer convenience, reduce client-side validation complexity, and support multiple integration patterns, while providing predictable output structures to minimize client-side parsing complexity, reduce deserialization errors, and enable reliable code generation.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 28 [Analysis]
**Description:** Explains the API design tradeoff that the "100% expandable" pattern represents.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** The response must explain that when all properties in a schema are expandable (17.7% of expandable schemas), this represents the tradeoff between response customization flexibility (benefit) and implementation complexity (cost). Clients gain complete control over response granularity, enabling minimal data transfer for list operations while supporting comprehensive expansion for detail views. However, the API backend must implement lazy loading or deferred resolution for every single property, increasing implementation complexity through conditional data fetching logic, cache management for partial objects, performance overhead from numerous potential database joins, and testing complexity to verify all expansion combinations work correctly.
**Sources:** N/A (Design analysis requirement)

## CRITERION 29 [Analysis]
**Description:** Explains API design tradeoffs for at least one additional pattern: dual-input, nullable+required coexistence, or polymorphic asymmetry.
**Weight:** Major
**Numerical Weight:** 5
**Rationale:** The response must explain design tradeoffs using specific API design principles from the prompt. For dual-input pattern (263:310 POST operations): input source multiplicity vs interface simplicity - accepting both query parameters and request body maximizes convenience but violates single responsibility and complicates request validation. For nullable+required coexistence (315 schemas): defensive programming vs strict contracts - guaranteed field presence prevents null reference errors while allowing semantic absence. For polymorphic asymmetry (134:15 ratio): client input validation flexibility vs server output type guarantees - liberal input acceptance enables diverse integration patterns while conservative output ensures client parsing safety.
**Sources:** N/A (Design analysis requirement)

## CRITERION 30 [Table Structure]
**Description:** Includes a comparison table in the response.
**Weight:** Critical
**Numerical Weight:** 4
**Rationale:** The prompt explicitly requires "Create a resource complexity comparison table with exactly 3 columns..." The response must include a table structure (markdown, HTML, or other tabular format) presenting the resource comparison data. Table absence fails this structural requirement completely.
**Sources:** N/A (Structural requirement from prompt)

## CRITERION 31 [Table Structure]
**Description:** States that the table has exactly 3 columns.
**Weight:** Major
**Numerical Weight:** 3
**Rationale:** The prompt specifies "Create a resource complexity comparison table with exactly 3 columns: 'Resource ID', 'Expandable Fields', 'Expandability Ratio'." The table must have precisely 3 columns as specified, not 2 (missing a column), not 4+ (extra columns), but exactly 3 to match the specification.
**Sources:** N/A (Structural requirement from prompt)

## CRITERION 32 [Table Structure]
**Description:** States that the table has exactly 3 data rows.
**Weight:** Major
**Numerical Weight:** 3
**Rationale:** The prompt specifies "Include exactly 3 data rows containing the 3 resources (by x-resourceId) with the highest expandable field counts." The table must have exactly 3 data rows (excluding the header row), representing the top 3 resources by expandable field count: payment_method (56), payment_method_configuration (54), and checkout.session (34).
**Sources:** N/A (Structural requirement from prompt)

## CRITERION 33 [Table Structure]
**Description:** Includes a description of the table structure before presenting the table.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt requires "Before the table, describe its structure (column count, row count, column names, ordering criterion)." The response must provide this meta-description before displaying the actual table, stating "The comparison table has 3 columns and 3 data rows. The columns are: Resource ID, Expandable Fields, and Expandability Ratio. The rows contain the 3 resources with the highest expandable field counts, ordered from highest to lowest by expandable field count." or equivalent description.
**Sources:** N/A (Structural requirement from prompt)

## CRITERION 34 [Table Structure]
**Description:** States that rows are ordered from highest to lowest by expandable field count.
**Weight:** Major
**Numerical Weight:** 3
**Rationale:** The prompt specifies "ordered from highest to lowest by expandable field count." The three resources must appear with descending expandable counts: payment_method (56 first), payment_method_configuration (54 second), checkout.session (34 third). Reverse ordering, alphabetical ordering, or random ordering fails this requirement.
**Sources:** N/A (Structural requirement from prompt)

## CRITERION 35 [Table Structure]
**Description:** States "Resource ID" (or equivalent) as the first column header.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt requires "Resource ID" as the first of 3 columns. The table header must use this exact term or close variant ("Resource", "Resource Name", "Resource Identifier") to identify the x-resourceId column containing schema resource identifiers.
**Sources:** N/A (Structural requirement from prompt)

## CRITERION 36 [Table Structure]
**Description:** States "Expandable Fields" (or equivalent) as the second column header.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt requires "Expandable Fields" as the second column header, representing the count of fields in the x-expandableFields array. Acceptable variants include "Expandable Field Count", "Expandable", or "# Expandable Fields".
**Sources:** N/A (Structural requirement from prompt)

## CRITERION 37 [Table Structure]
**Description:** States "Expandability Ratio" (or equivalent) as the third column header.
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The prompt requires "Expandability Ratio" as the third column header, representing the percentage of expandable fields relative to total properties. Acceptable variants include "Expandability %", "Expansion Ratio", or "% Expandable".
**Sources:** N/A (Structural requirement from prompt)

## CRITERION 38 [Accuracy - Row 1]
**Description:** States "payment_method" in the Resource ID column (first row).
**Weight:** Major
**Numerical Weight:** 3
**Rationale:** The resource with the highest expandable field count is `payment_method` with 56 expandable fields according to the x-expandableFields array in its schema definition. This must appear as the first row's Resource ID to satisfy the descending ordering requirement specified in the prompt.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 39 [Accuracy - Row 1]
**Description:** States 56 in the Expandable Fields column (first row).
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The `payment_method` schema's `x-expandableFields` array contains exactly 56 entries. These represent expandable relationships to: customer object, billing_details subcomponents, payment method type-specific objects (card, bank_account, wallet details like acss_debit, affirm, afterpay_clearpay, alipay, etc.), and various configuration objects. The 56 count reflects payment_method's role as a comprehensive payment instrument aggregator requiring selective loading.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 40 [Accuracy - Row 1]
**Description:** States 87.5% in the Expandability Ratio column (first row).
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The payment_method schema has 56 expandable fields out of 64 total properties. Calculation: 56/64 = 0.875 = 87.5%. This high ratio indicates payment_method serves primarily as a relationship aggregator rather than data container, with 87.5% of properties referencing other resources requiring selective expansion rather than containing inline scalar values.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 41 [Accuracy - Row 2]
**Description:** States "payment_method_configuration" in the Resource ID column (second row).
**Weight:** Major
**Numerical Weight:** 3
**Rationale:** The resource with the second-highest expandable field count is `payment_method_configuration` with 54 expandable fields. This correctly appears after payment_method (56) in descending order, satisfying the prompt's ordering requirement.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 42 [Accuracy - Row 2]
**Description:** States 54 in the Expandable Fields column (second row).
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The `payment_method_configuration` schema's `x-expandableFields` array contains exactly 54 entries. These represent configuration options for various payment method types (card, bank transfers, wallets, buy-now-pay-later) across different geographic markets, currencies, and payment flows, reflecting Stripe's global payment method configuration complexity.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 43 [Accuracy - Row 2]
**Description:** States 87.1% in the Expandability Ratio column (second row).
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The payment_method_configuration schema has 54 expandable fields out of 62 total properties. Calculation: 54/62 = 0.8709 = 87.1% (rounded to 1 decimal place as required by prompt). The ratio is nearly identical to payment_method (87.5%), indicating both schemas follow similar design patterns as relationship aggregators.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 44 [Accuracy - Row 3]
**Description:** States "checkout.session" in the Resource ID column (third row).
**Weight:** Major
**Numerical Weight:** 3
**Rationale:** The resource with the third-highest expandable field count is `checkout.session` with 34 expandable fields. This correctly appears after payment_method_configuration (54) in descending order, completing the top-3 ordering requirement.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 45 [Accuracy - Row 3]
**Description:** States 34 in the Expandable Fields column (third row).
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The `checkout.session` schema's `x-expandableFields` array contains exactly 34 entries. These represent expandable relationships to: customer object, subscription object, payment_intent object, line_items collection, shipping details, payment method collections, and various UI/automation configuration objects used in Stripe Checkout flows.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

## CRITERION 46 [Accuracy - Row 3]
**Description:** States 51.5% in the Expandability Ratio column (third row).
**Weight:** Minor
**Numerical Weight:** 2
**Rationale:** The checkout.session schema has 34 expandable fields out of 66 total properties. Calculation: 34/66 = 0.5151 = 51.5% (rounded to 1 decimal place). This notably lower ratio compared to payment_method (87.5%) and payment_method_configuration (87.1%) reflects checkout.session's hybrid nature: containing both expandable relationships AND significant inline configuration data (UI customization, expiration settings, success/cancel URLs, consent collection flags), resulting in only ~half of properties being expandable.
**Sources:** https://github.com/stripe/openapi/blob/38f2785cfd2cc036c10e68d4c25e7be3a26ca927/latest/openapi.spec3.yaml

---

## Scoring Summary

**Total Points:** 158
- Minor criteria (2-3 points): 27 criteria × average 2.6 = 70 points
- Major criteria (4-5 points): 19 criteria × average 4.6 = 88 points

**Breakdown by Section:**
- Q1 Expandable Fields (C1-C4): 15 points
- Q2 Parameter Serialization (C5-C11): 26 points
- Q3 Nullability Patterns (C12-C20): 30 points
- Q4 Polymorphic Asymmetry (C21-C27): 27 points
- Q5 Table Analysis (C28-C29): 10 points
- Q5 Table Structure (C30-C46): 50 points

**Pass Threshold:** 70% = 111 points
