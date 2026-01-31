# PROMPT

**Subdomain:** Blockchain Synchronization & Data Retrieval

**Routing:** Scratch

---

## Main Prompt

Blockchain indexing systems must efficiently synchronize historical state while balancing resource consumption, query latency, and data freshness. The [indexer](https://github.com/enviodev/velodrome-indexer) repository implements a multi-chain event indexer using optimized batch processing and caching strategies as of January 28, 2026, while the [airdrop-template](https://github.com/rsksmart/airdrop-template) repository demonstrates on-chain eligibility tracking with historical state queries as of January 28, 2026.

Both implementations employ distinct strategies for processing blockchain data, with indexer using high-throughput batch processing with intelligent caching, and airdrop-template leveraging block rounding for efficient historical queries. Understanding which approach optimizes throughput versus latency requires comparing batch sizes, analyzing cache hit rates, and evaluating memory utilization patterns.

Examine the synchronization mechanisms in both indexer and airdrop-template implementations. Determine performance patterns by comparing batch processing strategies, caching approaches, and resource utilization characteristics:

1. Analyze indexer's batch processing configuration to identify the default block batch size for event indexing. Examine airdrop-template's block rounding logic to determine the rounding interval in blocks. Calculate the ratio between indexer's batch size and airdrop-template's rounding interval to reveal relative processing granularity.

2. Examine indexer's cache implementation to identify the maximum cache size in number of entries. Analyze airdrop-template's historical query optimization to determine how many recent blocks it caches. Count the total number of cached items across both implementations.

3. Analyze indexer's processing throughput to determine blocks per second at peak performance. Examine airdrop-template's query latency to identify average response time in milliseconds for historical state queries. Express the relationship as throughput-to-latency ratio.

4. Examine indexer's memory utilization to identify the approximate memory footprint in megabytes during batch processing. Analyze airdrop-template's state storage to determine its memory usage per cached block. Calculate how many airdrop-template cached blocks would equal one indexer batch in memory consumption.

5. Survey both implementations to identify all processing strategies: indexer may use batch processing, parallel execution, and incremental updates; airdrop-template may use snapshot-based queries and block rounding. Count the total number of distinct synchronization strategies across both repositories.

6. Analyze indexer's state consistency mechanism to determine whether it uses atomic transactions or eventual consistency. Examine airdrop-template's data integrity approach to identify its consistency model. Categorize these as strong versus eventual consistency and express the distribution as a ratio.

7. Examine indexer's RPC call optimization to identify the number of parallel RPC connections maintained. Analyze airdrop-template's query batching to determine maximum batch size for historical queries. Calculate the total concurrent operations across both systems.

8. Analyze the space complexity for indexer's batch processing where n = number of events. Examine the space complexity for airdrop-template's block rounding cache where b = cached blocks. Determine which implementation achieves better memory efficiency relative to data volume.

9. Create a performance comparison chart showing how key metrics evolve across different operational scales. The chart should display operational scale on the X-axis (block ranges from 1K to 1M blocks), performance metrics on the Y-axis (throughput in blocks/second or latency in milliseconds), and multiple data series for different strategies: batch processing (indexer), real-time streaming (indexer), snapshot-based (airdrop-template), and cache-optimized (airdrop-template).

---

## Expected Image

A performance comparison chart showing:
- X-axis: Operational scale (1K, 10K, 100K, 500K, 1M blocks)
- Y-axis: Performance metrics (throughput blocks/s or latency ms)
- 4 data series: Batch Processing, Real-time Streaming, Snapshot-based, Cache-optimized
- Proper axis labels, units, and legend
