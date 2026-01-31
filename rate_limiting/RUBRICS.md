# RUBRICS

## Accuracy Criteria (13 total)

### C1: HubSpot Max Retry Count [Accuracy]
**Description:** Response correctly states the default maximum retry count in hubspot-api-php is 5.
**Rationale:** The RetryMiddlewareFactory.php source code defines "public const DEFAULT_MAX_RETRIES = 5;" as the default value used across all middleware factory methods.
**Source Quote:** `public const DEFAULT_MAX_RETRIES = 5;` (RetryMiddlewareFactory.php, line ~12)

### C2: Indexer Max Retry Count [Accuracy]
**Description:** Response correctly states the default maximum retry count in indexer is 7.
**Rationale:** The fetchTokenPrice() function in Token.ts uses "maxRetries = 7" as the default parameter.
**Source Quote:** `async function fetchTokenPrice(..., maxRetries = 7): Promise<...>` (Token.ts, line ~81)

### C3: HTTP Rate Limit Status Code [Accuracy]
**Description:** Response correctly identifies HTTP status code 429 as the rate limiting indicator in hubspot-api-php.
**Rationale:** The createRateLimitMiddleware() method specifically targets HTTP 429 responses for retry logic.
**Source Quote:** Documentation and standard HTTP semantics indicate 429 is the rate limit status code used by HubSpot API.

### C4: Indexer Exponential Base [Accuracy]
**Description:** Response correctly states the exponential backoff base in indexer is 2.
**Rationale:** The rate limit error handling uses formula "1000 * 2 ** attempt" with explicit base 2 for exponential progression.
**Source Quote:** `delayMs = Math.min(1000 * 2 ** attempt, 10000);` (Token.ts, line ~179)

### C5: HubSpot Constant Delay [Accuracy]
**Description:** Response correctly states the default constant delay is 10 seconds.
**Rationale:** The getConstantDelayFunction() in Delay.php uses "int $secondsDelay = 10" as the default parameter.
**Source Quote:** `public static function getConstantDelayFunction(int $secondsDelay = 10)` (Delay.php, line ~15)

### C6: Indexer Maximum Rate Limit Delay [Accuracy]
**Description:** Response correctly identifies 60 seconds as the maximum delay for rate limit errors in indexer.
**Rationale:** The special case for attempt 6 sets delayMs to 60000 milliseconds as the longest wait time.
**Source Quote:** `} else if (attempt === 6) { delayMs = 60000; // 60 seconds (1 minute) for 7th retry` (Token.ts, line ~184)

### C7: HubSpot Linear Backoff Formula [Accuracy]
**Description:** Response correctly states the linear backoff formula is 1000 * retries milliseconds.
**Rationale:** The getLinearDelayFunction() returns a function that calculates delay as "1000 * $retries" milliseconds.
**Source Quote:** `return 1000 * $retries;` (Delay.php, line ~27)

### C8: Indexer Error Type Count [Accuracy]
**Description:** Response correctly identifies that indexer classifies 6 error types.
**Rationale:** The ErrorType enum in Helpers.ts defines exactly 6 variants.
**Source Quote:** `export enum ErrorType { RATE_LIMIT = "RATE_LIMIT", OUT_OF_GAS = "OUT_OF_GAS", CONTRACT_REVERT = "CONTRACT_REVERT", NETWORK_ERROR = "NETWORK_ERROR", HISTORICAL_STATE_NOT_AVAILABLE = "HISTORICAL_STATE_NOT_AVAILABLE", UNKNOWN = "UNKNOWN" }` (Helpers.ts)

### C9: Indexer Effect Rate Limit [Accuracy]
**Description:** Response correctly states the effect rate limit is 5000 calls per second.
**Rationale:** The EFFECT_RATE_LIMITS constant TOKEN_EFFECTS is defined as 5000.
**Source Quote:** `TOKEN_EFFECTS: 5000` (Constants.ts)

### C10: Indexer Initial Network Error Delay [Accuracy]
**Description:** Response correctly identifies 500 milliseconds as the initial network error delay.
**Rationale:** Network error handling uses formula "500 * 2 ** attempt" with 500ms as the base multiplier for attempt 0.
**Source Quote:** `delayMs = Math.min(500 * 2 ** attempt, 8000);` (Token.ts, line ~196)

### C11: HubSpot Constant Strategy Name [Accuracy]
**Description:** Response correctly identifies constant as one of the backoff strategies in hubspot-api-php.
**Rationale:** The Delay.php class provides getConstantDelayFunction() method.
**Source Quote:** `public static function getConstantDelayFunction` (Delay.php)

### C12: HubSpot Linear Strategy Name [Accuracy]
**Description:** Response correctly identifies linear as one of the backoff strategies in hubspot-api-php.
**Rationale:** The Delay.php class provides getLinearDelayFunction() method.
**Source Quote:** `public static function getLinearDelayFunction` (Delay.php)

### C13: HubSpot Exponential Strategy Name [Accuracy]
**Description:** Response correctly identifies exponential as one of the backoff strategies in hubspot-api-php.
**Rationale:** The Delay.php class provides getExponentialDelayFunction() method.
**Source Quote:** `public static function getExponentialDelayFunction` (Delay.php)

## Quality Criteria (15 total)

### C14: Introduction Contextualizes HubSpot System [Quality]
**Description:** Response provides context for hubspot-api-php implementation.
**Rationale:** Understanding the HTTP client context helps evaluate why status code-based retry strategies are appropriate for this use case.

### C15: Introduction Contextualizes Indexer System [Quality]
**Description:** Response provides context for indexer implementation.
**Rationale:** Understanding the blockchain indexing context helps evaluate why error classification-based strategies are necessary for this use case.

### C16: HTTP Middleware Pattern Explanation [Quality]
**Description:** Response explains how hubspot-api-php uses Guzzle's middleware pattern for retry logic.
**Rationale:** The middleware pattern is the architectural foundation enabling composable retry strategies.

### C17: Error Type Classification Analysis [Quality]
**Description:** Response analyzes how indexer's error type classification system enables adaptive retry strategies.
**Rationale:** The multi-type classification is the core innovation allowing different retry behaviors for different failure modes.

### C18: Backoff Formula Comparison [Quality]
**Description:** Response compares mathematical formulas across implementations.
**Rationale:** The mathematical progression determines total wait time and recovery characteristics.

### C19: Total Wait Time Calculations [Quality]
**Description:** Response calculates total maximum wait times for different strategies.
**Rationale:** Total wait time is a critical operational metric affecting user experience and system responsiveness under failure conditions.

### C20: Time Complexity Analysis [Quality]
**Description:** Response analyzes time complexity of error detection.
**Rationale:** Time complexity analysis is essential for understanding performance characteristics and scalability implications.

### C21: Space Complexity Analysis [Quality]
**Description:** Response analyzes space complexity for retry state storage.
**Rationale:** Space complexity affects memory usage patterns and resource requirements for the retry mechanism.

### C22: Special Case Delay Analysis [Quality]
**Description:** Response analyzes special case delays at specific retry attempts in indexer.
**Rationale:** Special case handling demonstrates sophisticated adaptation to domain-specific failure modes.

### C23: Gas Limit Doubling Analysis [Quality]
**Description:** Response analyzes gas limit doubling for OUT_OF_GAS errors in indexer.
**Rationale:** Resource allocation adjustment is a different approach to retrying compared to time-based delays.

### C24: Simplicity vs Adaptability Trade-off [Quality]
**Description:** Response discusses trade-off between simple status code approach and adaptive keyword matching.
**Rationale:** Understanding this trade-off guides appropriate strategy selection.

### C25: Aggressive Retry Risk Analysis [Quality]
**Description:** Response discusses risk of overwhelming already-stressed services with aggressive retries.
**Rationale:** Retry strategies must balance recovery speed against service protection.

### C26: Composability Pattern Analysis [Quality]
**Description:** Response analyzes how hubspot-api-php's middleware composition enables separate retry policies.
**Rationale:** Composability is an architectural quality enabling flexible configuration without code modification.

### C27: Fallback Mechanism Analysis [Quality]
**Description:** Response discusses indexer's RPC fallback mechanism.
**Rationale:** The fallback mechanism represents a redundancy strategy adding resilience through provider diversity.

### C28: Operational Context Recommendations [Quality]
**Description:** Response provides guidance on selecting appropriate strategies based on operational context.
**Rationale:** Practical recommendations help readers apply the analysis to their own system design decisions.

## Image Criteria (12 total)

### C29: Table Includes HubSpot Constant Strategy [Image]
**Description:** Comparison table includes a row for hubspot-api-php constant delay strategy.
**Rationale:** Constant delay is one of the three configurable strategies, representing the simplest backoff approach.

### C30: Table Includes HubSpot Linear Strategy [Image]
**Description:** Comparison table includes a row for hubspot-api-php linear backoff strategy.
**Rationale:** Linear backoff represents moderate escalation between constant and exponential approaches.

### C31: Table Includes HubSpot Exponential Strategy [Image]
**Description:** Comparison table includes a row for hubspot-api-php exponential backoff strategy.
**Rationale:** Exponential backoff is the most aggressive escalation strategy.

### C32: Table Includes Indexer Rate Limit Strategy [Image]
**Description:** Comparison table includes a row for indexer's rate limit error handling.
**Rationale:** Rate limit handling is the primary use case for retry mechanisms.

### C33: Table Includes Indexer Network Error Strategy [Image]
**Description:** Comparison table includes a row for indexer's network error handling.
**Rationale:** Network errors receive different treatment than rate limits, demonstrating adaptive strategy selection.

### C34: Column for Algorithm Type [Image]
**Description:** Table includes a column describing the algorithm type.
**Rationale:** Algorithm type categorization enables high-level comparison of approaches.

### C35: Column for Time Complexity [Image]
**Description:** Table includes a column analyzing time complexity for error detection.
**Rationale:** Complexity analysis is essential for understanding performance characteristics.

### C36: Column for Space Complexity [Image]
**Description:** Table includes a column analyzing space complexity for retry state.
**Rationale:** Space complexity affects memory usage patterns.

### C37: Column for Error Classification [Image]
**Description:** Table includes a column describing the error classification approach.
**Rationale:** Error classification method fundamentally affects reliability and maintenance burden of retry logic.

### C38: Column for Max Retries [Image]
**Description:** Table includes a column specifying maximum retry attempts.
**Rationale:** Maximum retries determines the longest possible recovery time.

### C39: Column for Total Wait Time [Image]
**Description:** Table includes a column showing calculated total wait time.
**Rationale:** Total wait time directly affects user experience during failure scenarios.

### C40: Column for Backoff Formula [Image]
**Description:** Table includes a column showing the mathematical formula for delay calculation.
**Rationale:** The formula enables readers to predict retry timing behavior.
