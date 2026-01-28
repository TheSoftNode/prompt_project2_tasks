# COMPARISON CHART

## Performance Metrics vs Operational Scale

### Chart 1: Throughput (blocks/second)

```mermaid
%%{init: {'theme':'base'}}%%
xychart-beta
    title "Throughput (blocks/second) vs Event Count"
    x-axis "Event Count (thousands)" [0, 5, 10, 15, 20, 25, 30]
    y-axis "Throughput (blocks/sec)" 0 --> 1000
    line "Batch + Cache" [100, 300, 500, 650, 750, 850, 900]
    line "Real-time Stream" [50, 150, 250, 350, 420, 470, 500]
    line "On-chain Query" [20, 40, 55, 68, 78, 88, 100]
```

### Chart 2: Latency (milliseconds)

```mermaid
%%{init: {'theme':'base'}}%%
xychart-beta
    title "Latency (milliseconds) vs Event Count"
    x-axis "Event Count (thousands)" [0, 5, 10, 15, 20, 25, 30]
    y-axis "Latency (ms)" 0 --> 5500
    line "Batch + Cache" [100, 100, 100, 100, 100, 100, 100]
    line "Real-time Stream" [200, 400, 650, 900, 1150, 1350, 1500]
    line "On-chain Query" [500, 1200, 2000, 2900, 3700, 4400, 5000]
```

### Chart 3: Memory Usage (MB)

```mermaid
%%{init: {'theme':'base'}}%%
xychart-beta
    title "Memory Usage (MB) vs Event Count"
    x-axis "Event Count (thousands)" [0, 5, 10, 15, 20, 25, 30]
    y-axis "Memory (MB)" 0 --> 900
    line "Batch + Cache" [50, 120, 180, 240, 300, 350, 400]
    line "Real-time Stream" [80, 220, 370, 500, 630, 730, 800]
    line "On-chain Query" [10, 10, 10, 10, 10, 10, 10]
```

## Strategy Characteristics

| Strategy | Throughput @ 30K | Latency @ 30K | Memory @ 30K | Best For |
|:---------|:----------------|:--------------|:-------------|:---------|
| **Batch + Cache** | 900 blocks/sec | 100ms (constant) | 400MB (sublinear) | Historical analytics, reporting |
| **Real-time Stream** | 500 blocks/sec | 1500ms (linear) | 800MB (linear) | Live dashboards, monitoring |
| **On-chain Query** | 100 ops/sec | 5000ms (superlinear) | Minimal (on-chain only) | User-initiated claims, infrequent queries |
