# Restructuring Plan for rate_limiting and blockchain_sync

## Overview
Both tasks will be restructured following the langchain model with exactly **38 criteria each** (analytical + table/chart criteria).

---

## rate_limiting Task

### PROMPT_NEW.md
✅ **Created** with 9 questions leading to 38 criteria

### RUBRICS_ADVANCED_NEW.md Structure
**Total: 38 criteria (28 analytical + 10 table)**

#### Analytical Criteria (C1-C28)
- **Q1 (C1-C3)**: Retry count comparison
  - C1: hubspot-api-php default max retry count = 5
  - C2: indexer default max retry count = 7
  - C3: Difference = 2

- **Q2 (C4-C6)**: Error classification breadth
  - C4: hubspot-api-php rate limit HTTP status code = 429
  - C5: indexer error type count = 6
  - C6: Total unique error categories = 7

- **Q3 (C7-C9)**: Backoff base values
  - C7: hubspot-api-php constant delay = 10 seconds
  - C8: indexer exponential base = 2
  - C9: Ratio (exponential base : constant delay) = 1:5

- **Q4 (C10-C12)**: Delay progression analysis
  - C10: hubspot-api-php linear formula = 1000 × attempt milliseconds
  - C11: indexer max delay cap = 60 seconds
  - C12: Linear iterations to reach cap = 60

- **Q5 (C13-C15)**: Strategy diversity
  - C13: hubspot-api-php strategy count = 3 (constant, linear, exponential)
  - C14: indexer primary strategy = adaptive exponential
  - C15: Total distinct strategies = 4

- **Q6 (C16-C18)**: Classification approach distribution
  - C16: hubspot-api-php uses HTTP status codes
  - C17: indexer uses error message keyword matching
  - C18: Code-based:text-based ratio = 1:1

- **Q7 (C19-C21)**: Blockchain-specific limits
  - C19: indexer max gas limit cap = 30 million
  - C20: indexer RPC timeout = 60000 milliseconds
  - C21: Timeout per million gas = 2 ms/million

- **Q8 (C22-C24)**: Time complexity analysis
  - C22: hubspot-api-php error detection = O(1)
  - C23: indexer error detection = O(m×k)
  - C24: Count of O(1) implementations = 1

- **Additional Verification (C25-C28)**:
  - C25: hubspot-api-php exponential formula verification
  - C26: indexer network error initial delay = 500ms
  - C27: indexer special cap at attempt 5 = 30s
  - C28: hubspot-api-php supports 5xx status codes

#### Table Criteria (C29-C38)
- **C29**: Outputs comparison in table format
- **C30**: Table has 5 columns
- **C31**: Table has 5 rows (excluding header)
- **C32**: Includes "Implementation" column header
- **C33**: Includes "Algorithm Type" column header
- **C34**: Includes "Time Complexity" column header
- **C35**: Includes "Error Classification" column header
- **C36**: Includes "Max Retries & Total Wait" column header
- **C37**: Includes "Backoff Formula" column header
- **C38**: All 5 implementations represented as rows

**Maximum Score**: TBD (following langchain weight distribution)

---

## blockchain_sync Task

### PROMPT_NEW.md Structure (To Be Created)
**9 questions** covering:
1. Batch size comparison (indexer vs airdrop-template)
2. Block rounding intervals
3. Cache hit rate optimization
4. Memory utilization patterns
5. Query latency characteristics
6. State consistency mechanisms
7. Throughput calculations (blocks/second)
8. Processing strategy types
9. Performance chart creation request

### RUBRICS_ADVANCED_NEW.md Structure
**Total: 38 criteria (28 analytical + 10 chart)**

#### Analytical Criteria (C1-C28)
Similar structure to rate_limiting, with 3-4 criteria per question addressing:
- Batch processing parameters
- Caching strategies
- Memory management
- Query optimization
- State consistency
- Performance metrics
- Snapshot mechanisms
- Incremental update patterns

#### Chart Criteria (C29-C38)
- C29: Outputs performance data in chart format
- C30: X-axis represents operational scale
- C31: Y-axis represents performance metrics
- C32: Multiple data series for different strategies
- C33: Chart includes batch processing series
- C34: Chart includes real-time streaming series
- C35: Chart includes snapshot-based series
- C36: Chart includes cache-optimized series
- C37: Proper axis labels and units
- C38: Clear legend identifying each strategy

---

## Implementation Notes

1. **Code Snippets**: All analytical criteria should include source code snippets from the actual repositories where applicable
2. **Weight Distribution**: Follow langchain model (Critical 8-10, Major 4-7, Minor 1-3)
3. **Sources**: Reference exact GitHub commit hashes and file paths
4. **Verification**: Ensure all code snippets are accurate and verifiable
5. **Format**: Use consistent "## CRITERION N" format matching langchain

---

## Next Steps

1. ✅ Create rate_limiting/PROMPT_NEW.md
2. ⏳ Create rate_limiting/RUBRICS_ADVANCED_NEW.md (38 criteria)
3. ⏳ Create blockchain_sync/PROMPT_NEW.md
4. ⏳ Create blockchain_sync/RUBRICS_ADVANCED_NEW.md (38 criteria)
5. ⏳ Update CITATIONS.md for both tasks
6. ⏳ Update COMPARISON_TABLE.md / COMPARISON_CHART.md
7. ⏳ Update GOLDEN_RESPONSE.md for both tasks
