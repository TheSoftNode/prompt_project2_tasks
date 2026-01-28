# COMPARISON TABLE

| **Implementation** | **Algorithm Type** | **Time Complexity** | **Error Classification** | **Max Retries & Total Wait** | **Backoff Formula** |
|:------------------|:------------------|:-------------------|:------------------------|:----------------------------|:-------------------|
| **hubspot-api-php (Constant)** | Constant delay with HTTP middleware | O(1) error detection, O(r) space | HTTP status codes (429, 5xx ranges) | 5 retries, 50 seconds total (10s × 5) | delay_ms = 10000 (constant) |
| **hubspot-api-php (Linear)** | Linear backoff with HTTP middleware | O(1) error detection, O(r) space | HTTP status codes (429, 5xx ranges) | 5 retries, 15 seconds total (1+2+3+4+5) | delay_ms = 1000 × attempt |
| **hubspot-api-php (Exponential)** | Exponential backoff with HTTP middleware | O(1) error detection, O(r) space | HTTP status codes (429, 5xx ranges) | 5 retries, 31 seconds total (1+2+4+8+16) | delay_ms = 1000 × 2^attempt |
| **indexer (Rate Limit)** | Adaptive exponential with error type classification | O(m×k) error classification, O(r) space | Error message keyword matching (6 error types) | 7 retries, ~121 seconds total (1+2+4+8+10+30+60) | delay_ms = min(1000 × 2^attempt, 10000); special: attempt 5→30s, 6→60s |
| **indexer (Network Error)** | Fast exponential with error type classification | O(m×k) error classification, O(r) space | Error message keyword matching (6 error types) | 7 retries, ~58.5 seconds total (0.5+1+2+4+8+15+30) | delay_ms = min(500 × 2^attempt, 8000); special: attempt 5→15s, 6→30s |
