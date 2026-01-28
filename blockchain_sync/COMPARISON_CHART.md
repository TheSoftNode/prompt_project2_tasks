# COMPARISON CHART

## Performance Metrics vs Operational Scale

### Throughput (blocks/second)

```
     ┃
 900 ┃                    ╱─────────────────  Batch + Cache (indexer)
     ┃                 ╱╱╱
 700 ┃              ╱╱╱
     ┃           ╱╱╱
 500 ┃        ╱╱╱              ╱──────────────  Real-time Stream
     ┃     ╱╱╱               ╱╱
 300 ┃  ╱╱╱                ╱╱
     ┃╱╱                 ╱╱
 100 ┃                 ╱╱            ╱─────────  On-chain Query
     ┃              ╱╱            ╱╱╱
   0 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     0      5K      10K     15K     20K     25K     30K    Events
```

### Latency (milliseconds)

```
     ┃
5000 ┃                               ╱──────────  On-chain Query
     ┃                            ╱╱╱
4000 ┃                         ╱╱╱
     ┃                      ╱╱╱
3000 ┃                   ╱╱╱
     ┃                ╱╱╱
2000 ┃             ╱╱╱
     ┃          ╱╱╱        ╱─────────────────────  Real-time Stream
1000 ┃       ╱╱╱        ╱╱╱
     ┃    ╱╱╱        ╱╱╱
     ┃ ╱╱╱        ╱╱╱
     ┃──────────────────────────────────────────  Batch + Cache
   0 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     0      5K      10K     15K     20K     25K     30K    Events
```

### Memory Usage (MB)

```
     ┃
 800 ┃                          ╱──────────────────  Real-time Stream
     ┃                       ╱╱╱
 600 ┃                    ╱╱╱
     ┃                 ╱╱╱
 400 ┃              ╱╱╱     ╱────────────────────── Batch + Cache
     ┃           ╱╱╱     ╱╱╱
 200 ┃        ╱╱╱     ╱╱╱
     ┃     ╱╱╱     ╱╱╱
     ┃  ╱╱╱     ╱╱╱                ────────────────  On-chain Query
   0 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     0      5K      10K     15K     20K     25K     30K    Events
```

## Strategy Characteristics

| Strategy | Throughput @ 30K | Latency @ 30K | Memory @ 30K | Best For |
|:---------|:----------------|:--------------|:-------------|:---------|
| **Batch + Cache** | 900 blocks/sec | 100ms (constant) | 400MB (sublinear) | Historical analytics, reporting |
| **Real-time Stream** | 500 blocks/sec | 1500ms (linear) | 800MB (linear) | Live dashboards, monitoring |
| **On-chain Query** | 100 ops/sec | 5000ms (superlinear) | Minimal (on-chain only) | User-initiated claims, infrequent queries |
