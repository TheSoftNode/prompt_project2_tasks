# SCAFFOLD

## Research Framework for Rate Limiting and Retry Algorithms

This scaffold provides a structured approach to analyzing retry and backoff strategies in distributed systems.

### 1. Repository Context Analysis

**For each repository:**
- What is the primary operational domain? (REST API client, blockchain RPC, database queries, etc.)
- What types of failures does the system expect? (rate limits, network errors, service unavailability)
- What are the performance requirements? (latency sensitivity, throughput demands)
- What is the deployment model? (synchronous request-response, asynchronous event processing)

### 2. Error Detection and Classification

**HTTP Status Code Approach:**
- Which HTTP status codes trigger retry logic?
- Are there separate retry strategies for different status code ranges?
- How does the system distinguish between retriable and non-retriable errors?

**Message Parsing Approach:**
- What keywords or patterns identify different error types?
- How many error categories does the system recognize?
- What is the time complexity of error classification?

### 3. Backoff Strategy Analysis

**For each backoff strategy:**
- What is the mathematical formula for delay calculation?
- What is the initial delay value?
- What is the maximum delay cap (if any)?
- Are there special cases for specific retry attempts?
- What is the total maximum wait time across all retries?

**Strategy Types:**
- Constant: `delay = k` (fixed delay)
- Linear: `delay = k × attempt` (arithmetic progression)
- Exponential: `delay = k × base^attempt` (geometric progression)
- Adaptive: Different formulas based on error type or other conditions

### 4. Retry Configuration

**Parameters:**
- What is the maximum retry count?
- Is the retry count configurable?
- What is the default configuration?
- Are there different retry counts for different error types?

### 5. Complexity Analysis

**Time Complexity:**
- Error detection: O(?) per retry attempt
- Delay calculation: O(?) per retry attempt

**Space Complexity:**
- Retry state storage: O(?) across all retries
- Error history tracking: O(?) if applicable

### 6. Advanced Features

**Adaptive Mechanisms:**
- Does the system adjust retry behavior based on error types?
- Are there resource allocation adjustments (e.g., gas limit increases)?
- Does the system implement circuit breakers or rate limiting?

**Redundancy Mechanisms:**
- Does the system implement fallback endpoints or services?
- Are there timeout mechanisms?
- How does the system handle cascading failures?

### 7. Trade-offs and Design Decisions

**Simplicity vs Adaptability:**
- Does the implementation prioritize predictable behavior or adaptive optimization?
- How maintainable is the error detection logic?
- What is the code complexity cost?

**Recovery Time vs Service Protection:**
- Do aggressive retries risk overwhelming already-stressed services?
- Do conservative delays extend recovery time unacceptably?
- How does the strategy balance these competing concerns?

**Operational Context:**
- What failure mode characteristics justify the chosen approach?
- Would alternative strategies be more appropriate in different contexts?
- What are the cost implications (API quota consumption, infrastructure resources)?

### 8. Comparison Table Construction

**Required Columns:**
- Implementation/Strategy name
- Algorithm type and category
- Time/space complexity
- Error classification approach
- Maximum retries and total wait time
- Backoff formula (mathematical expression)

**Additional Columns (Optional):**
- Framework/library dependencies
- Configuration flexibility
- Special features
- Best suited use cases

### 9. Recommendations

**Selection Criteria:**
- When to use constant delay (fixed rate limit windows, simple retry scenarios)
- When to use linear backoff (moderate escalation needs)
- When to use exponential backoff (preventing service overload, standard best practice)
- When to use adaptive strategies (heterogeneous error types, complex failure modes)

**Implementation Guidance:**
- How to compose multiple retry strategies for different error classes
- How to tune retry parameters for specific operational contexts
- How to monitor and measure retry effectiveness
