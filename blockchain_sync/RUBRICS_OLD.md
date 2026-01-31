# RUBRICS

## Accuracy Criteria (13 total)

### C1: RPC Timeout Value [Accuracy]
**Description:** Response correctly states the RPC timeout in indexer is 60000 milliseconds (60 seconds).
**Rationale:** The Constants.ts file defines `export const RPC_TIMEOUT_MS = 60000;` as the timeout for all RPC requests.
**Source Quote:** `export const RPC_TIMEOUT_MS = 60000;` (Constants.ts, line 120)

### C2: Effect Rate Limit Value [Accuracy]
**Description:** Response correctly identifies the effect rate limit as 5000 calls per second.
**Rationale:** The EFFECT_RATE_LIMITS constants define all effect types (TOKEN_EFFECTS, VOTER_EFFECTS, DYNAMIC_FEE_EFFECTS, ROOT_POOL_EFFECTS) as 5000.
**Source Quote:** `export const EFFECT_RATE_LIMITS = { TOKEN_EFFECTS: 5000, VOTER_EFFECTS: 5000, ... }` (Constants.ts, lines 61-66)

### C3: Token Price Update Interval [Accuracy]
**Description:** Response correctly states the token price update interval is 3600 seconds (1 hour).
**Rationale:** The PriceOracle.ts file uses `const SECONDS_IN_AN_HOUR = 3600;` as the refresh threshold for token prices.
**Source Quote:** `const SECONDS_IN_AN_HOUR = 3600;` (PriceOracle.ts, line 81)

### C4: Snapshot Interval Duration [Accuracy]
**Description:** Response correctly identifies the snapshot interval for liquidity pools as 1 hour (3600000 milliseconds).
**Rationale:** The LiquidityPoolAggregator.ts defines `const UPDATE_INTERVAL = 60 * 60 * 1000;` for snapshot creation timing.
**Source Quote:** `const UPDATE_INTERVAL = 60 * 60 * 1000;` (LiquidityPoolAggregator.ts, line 13)

### C5: L2 Block Time [Accuracy]
**Description:** Response correctly states the block time for L2 chains is 2 seconds.
**Rationale:** The roundBlockToInterval function uses conditional logic: `const blockTimeSeconds = chainId === 1 ? 12 : 2;` where L2s default to 2 seconds.
**Source Quote:** `const blockTimeSeconds = chainId === 1 ? 12 : 2;` (Effects/Token.ts, line 455)

### C6: Maximum Gas Limit Cap [Accuracy]
**Description:** Response correctly identifies the maximum gas limit cap as 30 million.
**Rationale:** The OUT_OF_GAS retry logic caps gas limit scaling at 30M: `Math.min(Number(currentGasLimit) * 2, 30000000)`.
**Source Quote:** `currentGasLimit = BigInt(Math.min(Number(currentGasLimit) * 2, 30000000));` (Effects/Token.ts, line 206)

### C7: Supported Chain Count [Accuracy]
**Description:** Response correctly states the indexer supports 11 chains.
**Rationale:** The config.yaml file lists 11 networks: Optimism, Base, Celo, Soneium, Ink, Mode, Lisk, Unichain, Fraxtal, Metal, Swell.
**Source Quote:** Network definitions in config.yaml listing 11 distinct chains (config.yaml, lines 10-730)

### C8: Last Known Price Fallback Duration [Accuracy]
**Description:** Response correctly identifies the last known price fallback duration as 7 days.
**Rationale:** The PriceOracle.ts uses last known prices only if `Date.now() - token.lastUpdatedTimestamp.getTime() < 7 * 24 * 60 * 60 * 1000` (7 days).
**Source Quote:** Conditional check for 7-day threshold (PriceOracle.ts, line 119)

### C9: RPC Batching Enabled [Accuracy]
**Description:** Response correctly confirms RPC batching is enabled in indexer.
**Rationale:** RPC client configuration explicitly sets `batch: true` in the transport options.
**Source Quote:** `transport: http(process.env.ENVIO_OPTIMISM_RPC_URL || DefaultRPC.optimism, { batch: true, timeout: RPC_TIMEOUT_MS })` (Constants.ts, line 267)

### C10: Merkle Proof Hashing Algorithm [Accuracy]
**Description:** Response correctly identifies Keccak256 as the hashing algorithm used in Merkle proofs.
**Rationale:** The contract uses `keccak256(bytes.concat(keccak256(abi.encode(origin_, amount_))))` for leaf construction.
**Source Quote:** `return keccak256(bytes.concat(keccak256(abi.encode(origin_, amount_))));` (CustomAirdrop1155ClaimMerkle.sol, line 91)

### C11: Maximum Staking Score [Accuracy]
**Description:** Response correctly states the maximum staking score in MultiCriteriaAirdrop is 100.
**Rationale:** The staking score calculation returns values 0-100 with 50 points max for amount and 50 points max for duration.
**Source Quote:** Score calculation logic totaling to 100 maximum (MultiCriteriaAirdrop1155.sol, lines 158-169)

### C12: MultiCriteriaAirdrop Scoring Criteria Count [Accuracy]
**Description:** Response correctly identifies 3 scoring criteria: staking, activity, and RNS.
**Rationale:** The calculateUserScore function invokes three scoring functions: `_calculateStakingScore()`, `_calculateActivityScore()`, and `_calculateRNSScore()`.
**Source Quote:** Three score calculation function calls (MultiCriteriaAirdrop1155.sol, lines 131-137)

### C13: Blocks Per Hour for L2 Chains [Accuracy]
**Description:** Response correctly calculates 1800 blocks per hour for L2 chains with 2-second block times.
**Rationale:** The roundBlockToInterval function computes `Math.floor(3600 / blockTimeSeconds)` which equals 1800 when blockTimeSeconds is 2.
**Source Quote:** `const blocksPerHour = Math.floor(3600 / blockTimeSeconds);` (Effects/Token.ts, line 456)

## Quality Criteria (13 total)

### C14: Introduction Contextualizes Indexer System [Quality]
**Description:** Response explains the indexer's multi-chain event processing architecture and operational scope.
**Rationale:** Understanding the 11-chain scope and Envio's event-driven architecture provides context for why specific optimizations are necessary.

### C15: Introduction Contextualizes Airdrop System [Quality]
**Description:** Response explains the airdrop template's on-chain eligibility tracking and Merkle tree distribution approach.
**Rationale:** Understanding the on-demand state query model contrasts with the indexer's batch processing approach.

### C16: Block Rounding Optimization Explanation [Quality]
**Description:** Response explains how block rounding to hourly intervals improves cache hit rates and reduces RPC calls.
**Rationale:** Block rounding is the core optimization enabling 1800× reduction in price queries, critical to understanding performance gains.

### C17: Cache Hit Rate Impact Analysis [Quality]
**Description:** Response analyzes how cache hit rates (95%+) after warm-up enable constant latency regardless of scale.
**Rationale:** Cache effectiveness determines whether latency scales linearly or remains constant, fundamentally affecting system behavior.

### C18: Dual-Layer Caching Strategy Analysis [Quality]
**Description:** Response explains effect-level caching and state-level caching with their respective invalidation strategies.
**Rationale:** The two-layer approach balances data freshness with query efficiency, requiring separate analysis of each layer.

### C19: Batch Processing Performance Impact [Quality]
**Description:** Response analyzes how RPC batching and Promise.all() patterns improve throughput.
**Rationale:** Batch processing reduces network round trips from O(n) to O(1), fundamentally changing performance characteristics.

### C20: Snapshot Mechanism Trade-offs [Quality]
**Description:** Response discusses how hourly snapshots enable time-series queries without storing every block's state.
**Rationale:** Snapshot intervals represent a trade-off between temporal resolution and storage efficiency.

### C21: Merkle Tree Space-Time Trade-off [Quality]
**Description:** Response analyzes how Merkle trees reduce on-chain storage from O(n) to O(1) while adding O(log n) verification cost per claim.
**Rationale:** This fundamental trade-off affects deployment costs versus per-user claim costs, critical for cost analysis.

### C22: Multi-Criteria Scoring Gas Cost Analysis [Quality]
**Description:** Response analyzes gas costs for external contract calls in eligibility scoring (minimum 6 calls for 3 RNS domains).
**Rationale:** Understanding gas costs helps evaluate when on-chain scoring becomes prohibitively expensive versus off-chain alternatives.

### C23: Retry Strategy Comparison [Quality]
**Description:** Response compares rate limit retry (1s→60s) versus network error retry (500ms→30s) backoff strategies.
**Rationale:** Different failure modes require different recovery strategies, and understanding this adaptation demonstrates sophistication.

### C24: Throughput Scaling Analysis [Quality]
**Description:** Response analyzes how throughput scales differently for batch+cache (constant), real-time (linear degradation), and on-chain (constrained by gas limits).
**Rationale:** Scaling behavior determines appropriate use cases for each strategy.

### C25: Latency Characteristics Analysis [Quality]
**Description:** Response explains why latency remains constant for batch+cache, scales linearly for real-time, and scales superlinearly for on-chain queries.
**Rationale:** Latency scaling patterns affect user experience and system responsiveness under load.

### C26: Strategy Selection Recommendations [Quality]
**Description:** Response provides guidance on selecting strategies based on data freshness requirements, query frequency, and resource constraints.
**Rationale:** Practical recommendations help readers apply the analysis to their own architectural decisions.

## Image Criteria (9 total)

### C27: Chart Shows Multiple Data Series [Image]
**Description:** Chart displays at least 3 distinct strategies (Batch+Cache, Real-time Stream, On-chain Query) as separate lines/series.
**Rationale:** Multiple series enable visual comparison of performance characteristics across approaches.

### C28: Chart X-Axis Shows Operational Scale [Image]
**Description:** Chart X-axis represents operational scale (event counts, block ranges, or time) with clear labeling.
**Rationale:** Scale progression demonstrates how performance changes as load increases.

### C29: Chart Y-Axis Shows Performance Metrics [Image]
**Description:** Chart Y-axis represents quantifiable metrics (throughput in blocks/sec, latency in ms, or memory in MB) with units.
**Rationale:** Quantitative metrics enable objective comparison rather than subjective assessment.

### C30: Throughput Chart Included [Image]
**Description:** Response includes a chart showing throughput (blocks/second) across different strategies.
**Rationale:** Throughput is a primary performance metric determining how much work the system can handle.

### C31: Latency Chart Included [Image]
**Description:** Response includes a chart showing latency (milliseconds) across different strategies.
**Rationale:** Latency affects user experience and real-time responsiveness of the system.

### C32: Memory Usage Chart Included [Image]
**Description:** Response includes a chart showing memory usage (MB) across different strategies.
**Rationale:** Memory consumption determines infrastructure costs and scalability limits.

### C33: Chart Legend Clearly Identifies Strategies [Image]
**Description:** Chart includes clear legend or labels identifying which line represents which strategy.
**Rationale:** Without clear identification, readers cannot map visual data to specific strategies.

### C34: Chart Shows Trend Differences [Image]
**Description:** Chart visually demonstrates different scaling trends (constant, linear, superlinear) for different strategies.
**Rationale:** The visual difference in slopes/curves is the primary insight the chart should convey.

### C35: Chart Formatting and Readability [Image]
**Description:** Chart uses proper ASCII formatting, alignment, axis labels, and spacing for clear visual presentation.
**Rationale:** Poor formatting reduces comprehension and makes the chart difficult to interpret.
