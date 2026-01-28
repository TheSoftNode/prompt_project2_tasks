# PROMPT

## Main Prompt

Blockchain indexing systems must efficiently synchronize historical state while balancing resource consumption, query latency, and data freshness. The [indexer](https://github.com/enviodev/velodrome-indexer) repository implements a multi-chain event indexer using optimized batch processing and caching strategies, while the [airdrop-template](https://github.com/rsksmart/airdrop-template) repository demonstrates on-chain eligibility tracking with historical state queries.

Examine the synchronization and data retrieval strategies implemented across these two repositories. Compare the algorithmic approaches used for processing blockchain data, maintaining state consistency, and optimizing query performance.

Analyze the trade-offs between different synchronization strategies in terms of processing throughput, memory utilization, and latency characteristics. Consider approaches that may use batch processing, incremental updates, caching mechanisms, or snapshot-based strategies.

Create a performance comparison chart showing how key metrics evolve across different operational scales. The chart should display:
- X-axis: Operational scale (block ranges, event counts, or time progression)
- Y-axis: Performance metrics (throughput in blocks/second, latency in milliseconds, or memory usage in MB)
- Multiple data series for different strategies (batch processing, real-time streaming, snapshot-based, cache-optimized)

Include a detailed analysis of how block rounding intervals, cache hit rates, and retry mechanisms influence overall system performance and reliability.
