# PROMPT

## Main Prompt

Modern distributed systems require sophisticated rate limiting and retry strategies to handle API failures, network instability, and service degradation gracefully. The [hubspot-api-php](https://github.com/HubSpot/hubspot-api-php) repository implements HTTP client rate limiting for REST API interactions, while the [indexer](https://github.com/enviodev/velodrome-indexer) repository implements blockchain RPC retry mechanisms for high-throughput event indexing.

Examine the retry and backoff algorithms implemented across these two repositories. Compare the algorithmic approaches used for handling rate limits, network failures, and service errors.

Analyze the trade-offs between different backoff strategies in terms of recovery time, resource utilization, and failure resilience. Consider approaches that may use constant delays, linear progression, exponential backoff, or adaptive strategies based on error classification.

Create a comparison table showing the following for each implementation:
- Algorithm type and backoff strategy
- Time complexity for retry sequence
- Error detection and classification approach
- Maximum retry attempts and total wait time
- Backoff progression formula

Include a detailed analysis of how error type classification influences retry behavior and how each approach balances aggressive retries against overwhelming already-stressed services.
