# Blockchain Data Synchronization Strategies - Project 2 Task

## Overview

This task compares blockchain synchronization and indexing strategies across two repositories:
- **indexer**: Multi-chain event indexer with batch processing and caching
- **airdrop-template**: On-chain eligibility tracking with real-time state queries

## Task Structure

- **PROMPT.md**: Main research prompt requesting performance analysis with charts
- **SUBPROMPTS.md**: 15 verification questions with 1-5 word answers
- **GOLDEN_RESPONSE.md**: 1100-word analysis with ASCII performance charts
- **RUBRICS.md**: 35 evaluation criteria (13 Accuracy + 13 Quality + 9 Image)
- **CITATIONS.md**: 5 source files with commit hashes
- **COMPARISON_CHART.md**: Standalone ASCII charts for throughput, latency, memory
- **SCAFFOLD.md**: Research framework for analyzing synchronization strategies

## Key Algorithmic Topics

1. **High-Throughput Event Indexing** (indexer)
   - Block rounding to hourly intervals (1800× RPC reduction)
   - Dual-layer caching (effect-level + state-level)
   - RPC batching and parallel queries
   - Hourly snapshots for time-series data
   - Adaptive retry strategies (rate limit vs network errors)

2. **On-Chain Real-Time Queries** (airdrop-template)
   - Multi-criteria eligibility scoring with external contract calls
   - Merkle tree validation (O(1) storage, O(log n) verification)
   - Batch state updates for gas optimization
   - Real-time score calculation on claim

## Performance Comparison Dimensions

- **Throughput**: Batch+Cache (900 blocks/sec) vs Real-time (500 blocks/sec) vs On-chain (100 ops/sec)
- **Latency**: Constant (100ms) vs Linear (1500ms) vs Superlinear (5000ms) at 30K events
- **Memory**: Sublinear (400MB) vs Linear (800MB) vs Minimal (on-chain only)
- **Scaling characteristics**: How each metric evolves with operational scale

## Chart Features

This task includes **ASCII performance charts** showing:
- 3 data series (Batch+Cache, Real-time Stream, On-chain Query)
- X-axis: Operational scale (0-30K events)
- Y-axis: Performance metrics (throughput, latency, memory)
- Visual demonstration of different scaling trends (constant, linear, superlinear)

## Sources

- **Repository 1**: indexer (enviodev/velodrome-indexer)
  - config.yaml
  - Effects/Token.ts
  - Aggregators/LiquidityPoolAggregator.ts

- **Repository 2**: airdrop-template (rsksmart/airdrop-template)
  - MultiCriteriaAirdrop1155.sol
  - build-root.ts

## Learning Objectives

- Understand trade-offs between batch processing and real-time queries
- Analyze how block rounding and caching improve cache hit rates
- Compare on-chain vs off-chain synchronization costs and latency
- Evaluate Merkle tree space-time trade-offs
- Interpret performance charts showing scaling characteristics
- Select appropriate strategies based on freshness requirements and query patterns
