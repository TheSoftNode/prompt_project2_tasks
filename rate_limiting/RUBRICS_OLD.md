# RUBRICS

## Accuracy Criteria (13 total)

### C1: HubSpot Max Retry Count [Accuracy]
**Description:** Response correctly states the default maximum retry count in hubspot-api-php is 5.
**Rationale:** The RetryMiddlewareFactory.php source code defines `public const DEFAULT_MAX_RETRIES = 5;` as the default value used across all middleware factory methods.
**Source Quote:** `public const DEFAULT_MAX_RETRIES = 5;` (RetryMiddlewareFactory.php, line ~12)

### C2: Indexer Max Retry Count [Accuracy]
**Description:** Response correctly states the default maximum retry count in indexer is 7.
**Rationale:** The fetchTokenPrice() function in Token.ts uses `maxRetries = 7` as the default parameter, allowing 8 total execution attempts (initial + 7 retries).
**Source Quote:** `async function fetchTokenPrice(..., maxRetries = 7): Promise<...>` (Token.ts, line ~81)

### C3: HTTP Rate Limit Status Code [Accuracy]
**Description:** Response correctly identifies HTTP status code 429 as the rate limiting indicator in hubspot-api-php.
**Rationale:** The createRateLimitMiddleware() method specifically targets HTTP 429 ("Too Many Requests") responses for retry logic.
**Source Quote:** Documentation and standard HTTP semantics indicate 429 is the rate limit status code used by HubSpot API.

### C4: Indexer Exponential Base [Accuracy]
**Description:** Response correctly states the exponential backoff base in indexer is 2.
**Rationale:** The rate limit error handling uses formula `1000 * 2 ** attempt` with explicit base 2 for exponential progression.
**Source Quote:** `delayMs = Math.min(1000 * 2 ** attempt, 10000);` (Token.ts, line ~179)

### C5: HubSpot Constant Delay [Accuracy]
**Description:** Response correctly states the default constant delay is 10 seconds.
**Rationale:** The getConstantDelayFunction() in Delay.php uses `int $secondsDelay = 10` as the default parameter.
**Source Quote:** `public static function getConstantDelayFunction(int $secondsDelay = 10)` (Delay.php, line ~15)

### C6: Indexer Maximum Rate Limit Delay [Accuracy]
**Description:** Response correctly identifies 60 seconds as the maximum delay for rate limit errors in indexer.
**Rationale:** The special case for attempt 6 sets delayMs to 60000 milliseconds (60 seconds) as the longest wait time.
**Source Quote:** `} else if (attempt === 6) { delayMs = 60000; // 60 seconds (1 minute) for 7th retry` (Token.ts, line ~184)

### C7: HubSpot Linear Backoff Formula [Accuracy]
**Description:** Response correctly states the linear backoff formula is 1000 * retries milliseconds.
**Rationale:** The getLinearDelayFunction() returns a function that calculates delay as `1000 * $retries` milliseconds.
**Source Quote:** `return 1000 * $retries;` (Delay.php, line ~27)

### C8: Indexer Error Type Count [Accuracy]
**Description:** Response correctly identifies that indexer classifies 6 error types.
**Rationale:** The ErrorType enum in Helpers.ts defines exactly 6 variants: RATE_LIMIT, OUT_OF_GAS, CONTRACT_REVERT, NETWORK_ERROR, HISTORICAL_STATE_NOT_AVAILABLE, and UNKNOWN.
**Source Quote:** `export enum ErrorType { RATE_LIMIT = "RATE_LIMIT", OUT_OF_GAS = "OUT_OF_GAS", CONTRACT_REVERT = "CONTRACT_REVERT", NETWORK_ERROR = "NETWORK_ERROR", HISTORICAL_STATE_NOT_AVAILABLE = "HISTORICAL_STATE_NOT_AVAILABLE", UNKNOWN = "UNKNOWN" }` (Helpers.ts)

### C9: Indexer Effect Rate Limit [Accuracy]
**Description:** Response correctly states the effect rate limit is 5000 calls per second.
**Rationale:** The EFFECT_RATE_LIMITS constants in Constants.ts define all effect types (TOKEN_EFFECTS, VOTER_EFFECTS, etc.) as 5000 calls per second.
**Source Quote:** `export const EFFECT_RATE_LIMITS = { TOKEN_EFFECTS: 5000, VOTER_EFFECTS: 5000, DYNAMIC_FEE_EFFECTS: 5000, ROOT_POOL_EFFECTS: 5000 }` (Constants.ts)

### C10: Indexer Initial Network Error Delay [Accuracy]
**Description:** Response correctly identifies 500 milliseconds as the initial network error delay.
**Rationale:** Network error handling uses formula `500 * 2 ** attempt` with 500ms as the base multiplier for attempt 0.
**Source Quote:** `delayMs = Math.min(500 * 2 ** attempt, 8000);` (Token.ts, line ~196)

### C11: HubSpot Backoff Strategy Types [Accuracy]
**Description:** Response correctly identifies constant, linear, and exponential as the three backoff strategies provided by hubspot-api-php.
**Rationale:** The Delay.php class provides exactly three static methods: getConstantDelayFunction(), getLinearDelayFunction(), and getExponentialDelayFunction().
**Source Quote:** Method signatures in Delay.php defining the three delay functions.

### C12: HubSpot Error Classification Approach [Accuracy]
**Description:** Response correctly identifies HTTP status codes as the error classification approach.
**Rationale:** RetryMiddlewareFactory methods (createRateLimitMiddleware, createInternalErrorsMiddleware, createMiddlewareByHttpCodes) all operate on HTTP status code ranges.
**Source Quote:** `public const INTERNAL_ERROR_RANGES = [['from' => 500, 'to' => 503], ['from' => 520, 'to' => 599]];` (RetryMiddlewareFactory.php)

### C13: Indexer Error Classification Approach [Accuracy]
**Description:** Response correctly identifies error message keyword matching as the classification approach.
**Rationale:** The classifyError() function in Helpers.ts uses string keyword matching against error messages to determine ErrorType.
**Source Quote:** `if (lowerMsg.includes("rate limit") || lowerMsg.includes("rate limit exceeded") || lowerMsg.includes("429") || lowerMsg.includes("too many requests")) { return ErrorType.RATE_LIMIT; }` (Helpers.ts)

## Quality Criteria (13 total)

### C14: Introduction Contextualizes HubSpot System [Quality]
**Description:** Response provides context for hubspot-api-php implementation, explaining its REST API client operational domain.
**Rationale:** Understanding the HTTP client context helps evaluate why status code-based retry strategies are appropriate for this use case.

### C15: Introduction Contextualizes Indexer System [Quality]
**Description:** Response provides context for indexer implementation, explaining its blockchain RPC operational domain.
**Rationale:** Understanding the blockchain indexing context helps evaluate why error classification-based strategies are necessary for this use case.

### C16: HTTP Middleware Pattern Explanation [Quality]
**Description:** Response explains how hubspot-api-php uses Guzzle's middleware pattern for retry logic.
**Rationale:** The middleware pattern is the architectural foundation enabling composable retry strategies, distinguishing this implementation from inline retry loops.

### C17: Error Type Classification Analysis [Quality]
**Description:** Response analyzes how indexer's 6-error-type classification system enables adaptive retry strategies.
**Rationale:** The multi-type classification is the core innovation allowing different retry behaviors for different failure modes, worth detailed analysis.

### C18: Backoff Formula Comparison [Quality]
**Description:** Response compares mathematical formulas across implementations (constant, linear, exponential with different bases and caps).
**Rationale:** The mathematical progression determines total wait time and recovery characteristics, requiring explicit formula comparison.

### C19: Total Wait Time Calculations [Quality]
**Description:** Response calculates and compares total maximum wait times for different strategies (e.g., 121 seconds for indexer rate limit, 31 seconds for HubSpot exponential base-2).
**Rationale:** Total wait time is a critical operational metric affecting user experience and system responsiveness under failure conditions.

### C20: Time Complexity Analysis [Quality]
**Description:** Response analyzes time complexity of error detection (O(1) for status codes, O(m×k) for keyword matching).
**Rationale:** Time complexity analysis is essential for understanding performance characteristics and scalability implications.

### C21: Space Complexity Analysis [Quality]
**Description:** Response analyzes space complexity for retry state storage (O(r) across retry attempts).
**Rationale:** Space complexity affects memory usage patterns and resource requirements for the retry mechanism.

### C22: Special Case Handling Analysis [Quality]
**Description:** Response analyzes special cases like indexer's 30-second and 60-second delays at specific retry attempts, and gas limit doubling for OUT_OF_GAS errors.
**Rationale:** Special case handling demonstrates sophisticated adaptation to domain-specific failure modes beyond simple exponential formulas.

### C23: Trade-offs Discussion [Quality]
**Description:** Response discusses trade-offs between simplicity (status codes) and adaptability (keyword matching), and between aggressive retries and overwhelming stressed services.
**Rationale:** Understanding trade-offs guides appropriate strategy selection based on operational requirements and failure mode characteristics.

### C24: Composability and Separation of Concerns [Quality]
**Description:** Response analyzes how hubspot-api-php's middleware composition enables separate retry policies for different error classes.
**Rationale:** Composability is an architectural quality enabling flexible configuration without code modification, worth analyzing as a design pattern.

### C25: Fallback Mechanism Analysis [Quality]
**Description:** Response discusses indexer's RPC fallback mechanism that switches to public endpoints when private endpoints fail.
**Rationale:** The fallback mechanism represents a redundancy strategy orthogonal to retry timing, adding resilience through provider diversity.

### C26: Operational Context Recommendations [Quality]
**Description:** Response provides guidance on selecting appropriate strategies based on operational context (standardized error signaling vs heterogeneous failure modes).
**Rationale:** Practical recommendations help readers apply the analysis to their own system design decisions.

## Image Criteria (9 total)

### C27: Table Includes HubSpot Constant Strategy [Image]
**Description:** Comparison table includes a row for hubspot-api-php constant delay strategy.
**Rationale:** Constant delay is one of the three configurable strategies, representing the simplest backoff approach.

### C28: Table Includes HubSpot Linear Strategy [Image]
**Description:** Comparison table includes a row for hubspot-api-php linear backoff strategy.
**Rationale:** Linear backoff represents moderate escalation between constant and exponential approaches.

### C29: Table Includes HubSpot Exponential Strategy [Image]
**Description:** Comparison table includes a row for hubspot-api-php exponential backoff strategy.
**Rationale:** Exponential backoff is the most aggressive escalation strategy, commonly recommended for preventing service overload.

### C30: Table Includes Indexer Rate Limit Strategy [Image]
**Description:** Comparison table includes a row for indexer's rate limit error handling with adaptive exponential backoff.
**Rationale:** Rate limit handling is the primary use case for retry mechanisms, requiring explicit representation.

### C31: Table Includes Indexer Network Error Strategy [Image]
**Description:** Comparison table includes a row for indexer's network error handling with faster exponential backoff.
**Rationale:** Network errors receive different treatment than rate limits, demonstrating adaptive strategy selection.

### C32: Column for Algorithm Type [Image]
**Description:** Table includes a column describing the algorithm type and backoff strategy.
**Rationale:** Algorithm type categorization (constant, linear, exponential, adaptive) enables high-level comparison of approaches.

### C33: Column for Time Complexity [Image]
**Description:** Table includes a column analyzing time complexity for error detection and space complexity for retry state.
**Rationale:** Complexity analysis is essential for understanding performance characteristics and scalability.

### C34: Column for Error Classification [Image]
**Description:** Table includes a column describing the error classification approach (HTTP status codes vs keyword matching).
**Rationale:** Error classification method fundamentally affects reliability and maintenance burden of retry logic.

### C35: Column for Backoff Formula [Image]
**Description:** Table includes a column showing the mathematical formula for delay calculation.
**Rationale:** The formula enables readers to predict and verify retry timing behavior for their specific use cases.
