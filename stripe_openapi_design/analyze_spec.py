#!/usr/bin/env python3
"""Analyze Stripe OpenAPI spec to extract exact counts for golden response."""

import yaml
import json
from collections import defaultdict, Counter
from pathlib import Path

spec_path = Path("/Users/apple/Desktop/TECHDEVJS/rsk-cli/openapi/latest/openapi.spec3.yaml")

print("Loading spec...")
with open(spec_path) as f:
    spec = yaml.safe_load(f)

schemas = spec.get('components', {}).get('schemas', {})
paths = spec.get('paths', {})

print(f"Total schemas: {len(schemas)}")
print(f"Total paths: {len(paths)}")

# === QUESTION 1: Expandable Fields ===
print("\n=== Q1: EXPANDABLE FIELDS ===")

expandable_counts = {}
total_props_counts = {}
schemas_with_expandable = 0
schemas_100pct_expandable = 0

for schema_name, schema_def in schemas.items():
    x_expandable = schema_def.get('x-expandableFields', [])
    if x_expandable:
        schemas_with_expandable += 1
        expandable_count = len(x_expandable)
        expandable_counts[schema_name] = expandable_count

        # Count total properties
        props = schema_def.get('properties', {})
        total_props = len(props)
        total_props_counts[schema_name] = total_props

        # Check if 100% expandable
        if total_props > 0 and expandable_count == total_props:
            schemas_100pct_expandable += 1

schemas_20plus = sum(1 for count in expandable_counts.values() if count >= 20)
max_expandable_schema = max(expandable_counts.items(), key=lambda x: x[1])
pct_100expandable = (schemas_100pct_expandable / schemas_with_expandable * 100) if schemas_with_expandable > 0 else 0

print(f"Schemas with 20+ expandable fields: {schemas_20plus}")
print(f"Max expandable schema: {max_expandable_schema[0]} = {max_expandable_schema[1]} fields")
print(f"Schemas with ≥1 expandable field: {schemas_with_expandable}")
print(f"Schemas 100% expandable: {schemas_100pct_expandable}")
print(f"Percentage 100% expandable: {pct_100expandable:.1f}%")

# === QUESTION 2: Parameter Complexity ===
print("\n=== Q2: PARAMETER COMPLEXITY ===")

total_query_params = 0
deepobject_params = 0
expand_deepobject_params = 0
operations_with_params = []
operations_with_body = set()
post_operations = 0
dual_input_operations = 0

for path, path_item in paths.items():
    for method, operation in path_item.items():
        if method not in ['get', 'post', 'put', 'patch', 'delete']:
            continue

        op_id = f"{method.upper()} {path}"

        # Count POST operations
        if method == 'post':
            post_operations += 1

        # Count parameters
        params = operation.get('parameters', [])
        query_params = [p for p in params if p.get('in') == 'query']
        total_query_params += len(query_params)

        # Count deepObject
        for p in query_params:
            if p.get('style') == 'deepObject':
                deepobject_params += 1
                if p.get('name') == 'expand':
                    expand_deepobject_params += 1

        # Track operation param count
        if query_params:
            operations_with_params.append((op_id, len(query_params)))

        # Check for request body
        if 'requestBody' in operation:
            operations_with_body.add(op_id)

            # Check if ANY method with both query params and body
            if query_params:
                dual_input_operations += 1

deepobject_pct = (deepobject_params / total_query_params * 100) if total_query_params > 0 else 0
max_param_op = max(operations_with_params, key=lambda x: x[1]) if operations_with_params else (None, 0)
dual_input_ratio = f"{dual_input_operations}:{post_operations}"

print(f"Total query parameters: {total_query_params}")
print(f"DeepObject parameters: {deepobject_params}")
print(f"DeepObject percentage: {deepobject_pct:.1f}%")
print(f"Max param operation: {max_param_op[0]} = {max_param_op[1]} params")
print(f"Expand deepObject params: {expand_deepobject_params}")
print(f"POST operations: {post_operations}")
print(f"Dual-input POST operations: {dual_input_operations}")
print(f"Dual-input ratio: {dual_input_ratio}")

# === QUESTION 3: Nullability ===
print("\n=== Q3: NULLABILITY ===")

schemas_with_nullable = 0
nullable_counts = {}
schemas_both_nullable_required = 0
schemas_nullable_no_required = 0
schemas_with_props = 0

for schema_name, schema_def in schemas.items():
    props = schema_def.get('properties', {})
    if not props:
        continue

    schemas_with_props += 1

    nullable_props = [p for p, pdef in props.items() if pdef.get('nullable') == True]
    required_props = schema_def.get('required', [])

    if nullable_props:
        schemas_with_nullable += 1
        nullable_counts[schema_name] = len(nullable_props)

        if required_props:
            schemas_both_nullable_required += 1
        else:
            schemas_nullable_no_required += 1

max_nullable_schema = max(nullable_counts.items(), key=lambda x: x[1]) if nullable_counts else (None, 0)
pct_nullable_no_required = (schemas_nullable_no_required / schemas_with_props * 100) if schemas_with_props > 0 else 0

# Get specific schema counts
invoice_nullable = len([p for p, pdef in schemas.get('invoice', {}).get('properties', {}).items() if pdef.get('nullable') == True])
invoice_required = len(schemas.get('invoice', {}).get('required', []))
checkout_session_nullable = len([p for p, pdef in schemas.get('checkout.session', {}).get('properties', {}).items() if pdef.get('nullable') == True])
checkout_session_required = len(schemas.get('checkout.session', {}).get('required', []))

print(f"Schemas with ≥1 nullable property: {schemas_with_nullable}")
print(f"Max nullable schema: {max_nullable_schema[0]} = {max_nullable_schema[1]} nullable props")
print(f"Schemas with BOTH nullable AND required: {schemas_both_nullable_required}")
print(f"Schemas with nullable but NO required: {schemas_nullable_no_required}")
print(f"Total schemas with properties: {schemas_with_props}")
print(f"Percentage nullable-no-required: {pct_nullable_no_required:.1f}%")
print(f"invoice: nullable={invoice_nullable}, required={invoice_required}")
print(f"checkout.session: nullable={checkout_session_nullable}, required={checkout_session_required}")

# === QUESTION 4: Polymorphism ===
print("\n=== Q4: POLYMORPHISM (anyOf) ===")

def find_anyof_in_schema(schema_def, path=""):
    """Recursively find anyOf in schema definition."""
    anyof_list = []

    if isinstance(schema_def, dict):
        if 'anyOf' in schema_def:
            anyof_list.append((path, len(schema_def['anyOf'])))

        for key, value in schema_def.items():
            if key == 'properties':
                for prop_name, prop_def in value.items():
                    anyof_list.extend(find_anyof_in_schema(prop_def, f"{path}.{prop_name}"))
            elif key not in ['anyOf', 'oneOf', 'allOf']:
                anyof_list.extend(find_anyof_in_schema(value, path))

    return anyof_list

schemas_with_anyof = 0
max_anyof_property = (None, None, 0)

for schema_name, schema_def in schemas.items():
    anyof_found = find_anyof_in_schema(schema_def, schema_name)
    if anyof_found:
        schemas_with_anyof += 1
        for prop_path, count in anyof_found:
            if count > max_anyof_property[2]:
                max_anyof_property = (schema_name, prop_path, count)

# Count operations with anyOf in request/response
operations_anyof_request = 0
operations_anyof_response = 0

def has_anyof_recursive(obj):
    """Check if anyOf exists anywhere in nested structure."""
    if isinstance(obj, dict):
        if 'anyOf' in obj:
            return True
        for value in obj.values():
            if has_anyof_recursive(value):
                return True
    elif isinstance(obj, list):
        for item in obj:
            if has_anyof_recursive(item):
                return True
    return False

for path, path_item in paths.items():
    for method, operation in path_item.items():
        if method not in ['get', 'post', 'put', 'patch', 'delete']:
            continue

        # Check request body
        req_body = operation.get('requestBody', {}).get('content', {})
        for content_type, content_def in req_body.items():
            schema_ref = content_def.get('schema', {})
            if has_anyof_recursive(schema_ref):
                operations_anyof_request += 1
                break

        # Check response
        responses = operation.get('responses', {})
        for code, response in responses.items():
            resp_content = response.get('content', {})
            for content_type, content_def in resp_content.items():
                schema_ref = content_def.get('schema', {})
                if has_anyof_recursive(schema_ref):
                    operations_anyof_response += 1
                    break

anyof_ratio = f"{operations_anyof_request}:{operations_anyof_response}"

print(f"Schemas using anyOf: {schemas_with_anyof}")
print(f"Max anyOf property: schema={max_anyof_property[0]}, prop={max_anyof_property[1]}, count={max_anyof_property[2]}")
print(f"Operations with anyOf in request: {operations_anyof_request}")
print(f"Operations with anyOf in response: {operations_anyof_response}")
print(f"Request:Response ratio: {anyof_ratio}")

# === QUESTION 5: Top 5 Resources by Expandable Fields ===
print("\n=== Q5: TOP 5 RESOURCES ===")

# Get schemas with x-resourceId
resource_schemas = {}
for schema_name, schema_def in schemas.items():
    resource_id = schema_def.get('x-resourceId')
    if resource_id:
        resource_schemas[schema_name] = {
            'resource_id': resource_id,
            'expandable': len(schema_def.get('x-expandableFields', [])),
            'nullable': len([p for p, pdef in schema_def.get('properties', {}).items() if pdef.get('nullable') == True]),
            'required': len(schema_def.get('required', [])),
            'total_props': len(schema_def.get('properties', {}))
        }

# Sort by expandable fields and get top 5
top5 = sorted(resource_schemas.items(), key=lambda x: x[1]['expandable'], reverse=True)[:5]

print("\nTOP 5 RESOURCES BY EXPANDABLE FIELDS:")
print(f"{'Schema Name':<60} {'Resource ID':<30} {'Expandable':<12} {'Nullable':<10} {'Required':<10} {'Total':<8} {'Ratio %'}")
print("=" * 150)
for schema_name, data in top5:
    ratio = (data['expandable'] / data['total_props'] * 100) if data['total_props'] > 0 else 0
    print(f"{schema_name:<60} {data['resource_id']:<30} {data['expandable']:<12} {data['nullable']:<10} {data['required']:<10} {data['total_props']:<8} {ratio:.1f}%")

print("\n=== ANALYSIS COMPLETE ===")
