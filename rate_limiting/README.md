# Rate Limiting and Retry Algorithms - Project 2 Task

## Overview

This task compares retry and backoff algorithms across two repositories:
- **hubspot-api-php**: HTTP client rate limiting for REST API interactions
- **indexer**: Blockchain RPC retry mechanisms for event indexing

## Task Structure

- **PROMPT.md**: Main research prompt requesting algorithmic comparison
- **SUBPROMPTS.md**: 15 verification questions with 1-5 word answers
- **GOLDEN_RESPONSE.md**: 850-word scientific analysis with comparison table
- **RUBRICS.md**: 35 evaluation criteria (13 Accuracy + 11 Quality + 11 Image)
- **CITATIONS.md**: 4 source files with commit hashes
- **COMPARISON_TABLE.md**: Standalone comparison table
- **SCAFFOLD.md**: Research framework for analyzing retry strategies

## Key Algorithmic Topics

1. **HTTP Status Code-Based Retry** (hubspot-api-php)
   - Middleware pattern using Guzzle
   - Three backoff strategies: constant, linear, exponential
   - Default 5 retry attempts

2. **Error-Type Classified Retry** (indexer)
   - Multi-strategy approach with 6 error types
   - Adaptive exponential backoff with special cases
   - Default 7 retry attempts

## Comparison Dimensions

- Algorithm type and backoff strategy
- Time complexity for error detection and space complexity
- Error classification approach (HTTP codes vs keyword matching)
- Maximum retry attempts and total wait time
- Backoff formula (mathematical expressions)

## Sources

- **Repository 1**: hubspot-api-php (HubSpot/hubspot-api-php)
  - RetryMiddlewareFactory.php
  - Delay.php

- **Repository 2**: indexer (enviodev/velodrome-indexer)
  - Effects/Token.ts
  - Effects/Helpers.ts

## Learning Objectives

- Understand trade-offs between simplicity and adaptability in retry logic
- Compare constant, linear, and exponential backoff strategies
- Analyze error classification approaches and their complexity implications
- Evaluate adaptive retry strategies for heterogeneous failure modes
- Calculate total wait times and recovery characteristics
