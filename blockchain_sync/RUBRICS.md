# RUBRICS

## Accuracy Criteria (13 total)

### C1: RPC Timeout Value [Accuracy]
**Description:** Response correctly states the RPC timeout in indexer is 60000 milliseconds.
**Rationale:** The Constants.ts file defines "export const RPC_TIMEOUT_MS = 60000;" as the timeout for all RPC requests.
**Source Quote:** `export const RPC_TIMEOUT_MS = 60000;` (Constants.ts, line 120)

### C2: Effect Rate Limit Value [Accuracy]
**Description:** Response correctly identifies the effect rate limit as 5000 calls per second.
**Rationale:** The EFFECT_RATE_LIMITS constant TOKEN_EFFECTS is defined as "TOKEN_EFFECTS: 5000" showing 5000 calls per second.
**Source Quote:** `TOKEN_EFFECTS: 5000` (Constants.ts, line 62)

### C3: Token Price Update Interval [Accuracy]
**Description:** Response correctly states the token price update interval is 3600 seconds.
**Rationale:** The PriceOracle.ts file uses "const SECONDS_IN_AN_HOUR = 3600;" as the refresh threshold for token prices.
**Source Quote:** `const SECONDS_IN_AN_HOUR = 3600;` (PriceOracle.ts, line 81)

### C4: Snapshot Interval Duration [Accuracy]
**Description:** Response correctly identifies the snapshot interval for liquidity pools as 3600000 milliseconds.
**Rationale:** The LiquidityPoolAggregator.ts defines "const UPDATE_INTERVAL = 60 * 60 * 1000;" for snapshot creation timing.
**Source Quote:** `const UPDATE_INTERVAL = 60 * 60 * 1000;` (LiquidityPoolAggregator.ts, line 13)

### C5: L2 Block Time [Accuracy]
**Description:** Response correctly states the block time for L2 chains is 2 seconds.
**Rationale:** The roundBlockToInterval function uses conditional logic "const blockTimeSeconds = chainId === 1 ? 12 : 2;" where L2s default to 2 seconds.
**Source Quote:** `const blockTimeSeconds = chainId === 1 ? 12 : 2;` (Effects/Token.ts, line 455)

### C6: Maximum Gas Limit Cap [Accuracy]
**Description:** Response correctly identifies the maximum gas limit cap as 30 million.
**Rationale:** The OUT_OF_GAS retry logic caps gas limit scaling at 30M using "Math.min(Number(currentGasLimit) * 2, 30000000)".
**Source Quote:** `currentGasLimit = BigInt(Math.min(Number(currentGasLimit) * 2, 30000000));` (Effects/Token.ts, line 206)

### C7: Supported Chain Count [Accuracy]
**Description:** Response correctly states the indexer supports 11 chains.
**Rationale:** The config.yaml file lists 11 networks: Optimism, Base, Celo, Soneium, Ink, Mode, Lisk, Unichain, Fraxtal, Metal, Swell.
**Source Quote:** Network definitions in config.yaml listing 11 distinct chains (config.yaml, lines 10-730)

### C8: Last Known Price Fallback Duration [Accuracy]
**Description:** Response correctly identifies the last known price fallback duration as 7 days.
**Rationale:** The PriceOracle.ts uses last known prices only if "Date.now() - token.lastUpdatedTimestamp.getTime() < 7 * 24 * 60 * 60 * 1000" which equals 7 days.
**Source Quote:** Conditional check for 7-day threshold (PriceOracle.ts, line 119)

### C9: RPC Batching Enabled [Accuracy]
**Description:** Response correctly confirms RPC batching is enabled in indexer.
**Rationale:** RPC client configuration explicitly sets "batch: true" in the transport options.
**Source Quote:** `transport: http(process.env.ENVIO_OPTIMISM_RPC_URL || DefaultRPC.optimism, { batch: true, timeout: RPC_TIMEOUT_MS })` (Constants.ts, line 267)

### C10: Merkle Proof Hashing Algorithm [Accuracy]
**Description:** Response correctly identifies Keccak256 as the hashing algorithm used in Merkle proofs.
**Rationale:** The contract uses "keccak256(bytes.concat(keccak256(abi.encode(origin_, amount_))))" for leaf construction.
**Source Quote:** `return keccak256(bytes.concat(keccak256(abi.encode(origin_, amount_))));` (CustomAirdrop1155ClaimMerkle.sol, line 91)

### C11: Maximum Staking Score [Accuracy]
**Description:** Response correctly states the maximum staking score in MultiCriteriaAirdrop is 100.
**Rationale:** The staking score calculation returns values 0-100 with 50 points max for amount and 50 points max for duration.
**Source Quote:** Score calculation logic totaling to 100 maximum (MultiCriteriaAirdrop1155.sol, lines 158-169)

### C12: MultiCriteriaAirdrop Scoring Criteria Count [Accuracy]
**Description:** Response correctly identifies 3 as the number of scoring criteria.
**Rationale:** The calculateUserScore function invokes three scoring functions showing three distinct criteria types.
**Source Quote:** Three score calculation function calls (MultiCriteriaAirdrop1155.sol, lines 131-137)

### C13: Blocks Per Hour for L2 Chains [Accuracy]
**Description:** Response correctly calculates 1800 blocks per hour for L2 chains.
**Rationale:** The roundBlockToInterval function computes "Math.floor(3600 / blockTimeSeconds)" which equals 1800 when blockTimeSeconds is 2.
**Source Quote:** `const blocksPerHour = Math.floor(3600 / blockTimeSeconds);` (Effects/Token.ts, line 456)

## Quality Criteria (17 total)

### C14: Introduction Contextualizes Indexer System [Quality]
**Description:** Response explains the indexer's multi-chain event processing architecture.
**Rationale:** Understanding Envio's event-driven architecture provides context for why specific optimizations are necessary.

### C15: Introduction Contextualizes Airdrop System [Quality]
**Description:** Response explains the airdrop template's on-chain eligibility tracking approach.
**Rationale:** Understanding the on-demand state query model contrasts with the indexer's batch processing approach.

### C16: Block Rounding Optimization Explanation [Quality]
**Description:** Response explains how block rounding to hourly intervals reduces RPC calls.
**Rationale:** Block rounding is the core optimization enabling 1800× reduction in price queries, critical to understanding performance gains.

### C17: Cache Hit Rate Impact Analysis [Quality]
**Description:** Response analyzes how high cache hit rates enable constant latency regardless of scale.
**Rationale:** Cache effectiveness determines whether latency scales linearly or remains constant, fundamentally affecting system behavior.

### C18: Effect-Level Caching Explanation [Quality]
**Description:** Response explains effect-level caching with cache invalidation on errors.
**Rationale:** Effect-level caching stores results keyed by input parameters including rounded block numbers.

### C19: State-Level Caching Explanation [Quality]
**Description:** Response explains state-level caching with time-based refresh strategy.
**Rationale:** State-level caching implements refresh when blockTimestampMs minus lastUpdatedTimestamp exceeds threshold.

### C20: RPC Batching Impact [Quality]
**Description:** Response analyzes how RPC batching improves throughput.
**Rationale:** RPC batching allows multiple contract calls to bundle into single HTTP requests.

### C21: Parallel Query Impact [Quality]
**Description:** Response analyzes how Promise.all() patterns improve throughput.
**Rationale:** Parallel execution reduces network round trips from O(n) to O(1).

### C22: Snapshot Mechanism Trade-offs [Quality]
**Description:** Response discusses how hourly snapshots enable time-series queries.
**Rationale:** Snapshot intervals represent a trade-off between temporal resolution and storage efficiency.

### C23: Merkle Tree Storage Efficiency [Quality]
**Description:** Response analyzes how Merkle trees reduce on-chain storage from O(n) to O(1).
**Rationale:** Merkle roots provide constant storage regardless of eligibility set size.

### C24: Merkle Tree Verification Cost [Quality]
**Description:** Response analyzes O(log n) verification cost per claim for Merkle proofs.
**Rationale:** Verification cost grows logarithmically with eligibility set size.

### C25: Multi-Criteria Scoring Gas Cost Analysis [Quality]
**Description:** Response analyzes gas costs for external contract calls in eligibility scoring.
**Rationale:** Understanding gas costs helps evaluate when on-chain scoring becomes prohibitively expensive versus off-chain alternatives.

### C26: Rate Limit Retry Strategy Analysis [Quality]
**Description:** Response describes the rate limit backoff strategy progression from 1 second to 60 seconds.
**Rationale:** Rate limit errors trigger exponential backoff with special case delays at specific retry attempts.

### C27: Network Error Retry Strategy Analysis [Quality]
**Description:** Response describes the network error backoff strategy progression from 500 milliseconds to 30 seconds.
**Rationale:** Network errors receive faster exponential backoff assuming network disruptions resolve faster than quota exhaustion.

### C28: Batch Plus Cache Throughput Scaling [Quality]
**Description:** Response analyzes how throughput for batch plus cache strategy scales with load.
**Rationale:** Scaling behavior determines appropriate use cases for this strategy.

### C29: Real-Time Stream Latency Scaling [Quality]
**Description:** Response analyzes how latency for real-time stream strategy scales with event volume.
**Rationale:** Latency scaling patterns affect user experience and system responsiveness under load.

### C30: Strategy Selection Recommendations [Quality]
**Description:** Response provides guidance on selecting strategies based on operational requirements.
**Rationale:** Practical recommendations help readers apply the analysis to their own architectural decisions.

## Image Criteria (12 total)

### C31: Chart Shows Multiple Data Series [Image]
**Description:** Chart displays at least 3 distinct strategies as separate lines.
**Rationale:** Multiple series enable visual comparison of performance characteristics across approaches.

### C32: Chart X-Axis Shows Operational Scale [Image]
**Description:** Chart X-axis represents operational scale with clear labeling.
**Rationale:** Scale progression demonstrates how performance changes as load increases.

### C33: Chart Y-Axis Includes Units [Image]
**Description:** Chart Y-axis includes proper units for the metric displayed.
**Rationale:** Units are essential for interpreting quantitative performance data.

### C34: Throughput Chart Included [Image]
**Description:** Response includes a chart showing throughput across different strategies.
**Rationale:** Throughput is a primary performance metric determining how much work the system can handle.

### C35: Latency Chart Included [Image]
**Description:** Response includes a chart showing latency across different strategies.
**Rationale:** Latency affects user experience and real-time responsiveness of the system.

### C36: Memory Usage Chart Included [Image]
**Description:** Response includes a chart showing memory usage across different strategies.
**Rationale:** Memory consumption determines infrastructure costs and scalability limits.

### C37: Chart Legend Clearly Identifies Strategies [Image]
**Description:** Chart includes clear legend identifying which line represents which strategy.
**Rationale:** Without clear identification, readers cannot map visual data to specific strategies.

### C38: Chart Shows Constant Trend [Image]
**Description:** Chart visually demonstrates constant scaling trend for batch plus cache strategy.
**Rationale:** The constant latency is a key characteristic differentiating this strategy.

### C39: Chart Shows Linear Trend [Image]
**Description:** Chart visually demonstrates linear scaling trend for real-time stream strategy.
**Rationale:** The linear growth pattern indicates how performance degrades with load.

### C40: Chart Shows Superlinear Trend [Image]
**Description:** Chart visually demonstrates superlinear scaling trend for on-chain query strategy.
**Rationale:** The accelerating growth curve indicates exponentially worsening performance at scale.

### C41: Chart Axis Labels Present [Image]
**Description:** Chart includes axis labels for both X and Y axes.
**Rationale:** Axis labels are essential for interpreting what the chart displays.

### C42: Chart Title Present [Image]
**Description:** Chart includes a title describing what metric is being visualized.
**Rationale:** Chart titles provide context for understanding the visualization.
