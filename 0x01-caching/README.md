# 0x01-caching

## Overview

This directory contains materials related to various **cache replacement policies** used in computing systems. Cache replacement policies, also known as cache replacement algorithms, are critical to optimizing the performance of caches by deciding which items to discard when the cache is full. These algorithms strike a balance between **hit ratio** and **latency** to improve the overall efficiency of data retrieval in systems.

### Key Concepts

- **Hit Ratio**: The frequency with which the requested data is found in the cache.
- **Latency**: The time it takes to retrieve data from the cache when there's a hit.
- **Cache Pollution**: The situation where streaming data fills the cache, pushing out useful data.

### Cache Replacement Policies

#### 1. **Bélády's Anomaly**
   - An ideal algorithm that discards data that will not be needed for the longest time in the future, though impractical as it requires future knowledge.

#### 2. **Random Replacement (RR)**
   - Selects and discards an item at random to make space. Simple and used in ARM processors.

#### 3. **Simple Queue-Based Policies**
   - **First In First Out (FIFO)**: Discards the oldest items first.
   - **Last In First Out (LIFO)**: Discards the most recent items first.
   - **SIEVE**: A web cache-specific algorithm that quickly demotes newly inserted objects with a high one-hit-wonder ratio.

#### 4. **Recency-Based Policies**
   - **Least Recently Used (LRU)**: Discards the least recently used items.
   - **Most Recently Used (MRU)**: Discards the most recently used items.
   - **Segmented LRU (SLRU)**: Combines LRU with protected and probationary segments for better performance.

#### 5. **Frequency-Based Policies**
   - **Least Frequently Used (LFU)**: Discards items used the least often.
   - **Least Frequent Recently Used (LFRU)**: Combines LFU and LRU for network cache applications.
   - **LFU with Dynamic Aging (LFUDA)**: Adds a cache-age factor to reference count for better handling of popular objects.

#### 6. **RRIP-Style Policies**
   - **Re-Reference Interval Prediction (RRIP)**: Attempts to provide good scan resistance while evicting lines that have not been reused.
   - **Static RRIP (SRRIP)**: Inserts lines with a high re-reference prediction value (RRPV).
   - **Bimodal RRIP (BRRIP)**: Uses probabilistic insertion to reduce cache thrashing.
   - **Dynamic RRIP (DRRIP)**: Selects between SRRIP and BRRIP based on workload patterns.

#### 7. **Policies Approximating Bélády's Algorithm**
   - **Hawkeye**: Predicts cache-friendly and cache-averse accesses by emulating Bélády's algorithm.
   - **Mockingjay**: Refines Hawkeye by making more fine-grained decisions.

#### 8. **Machine Learning and Other Policies**
   - **Low Inter-Reference Recency Set (LIRS)**: Uses recency and inter-reference recency (IRR) to improve on LRU.

## How to Use

Explore the different caching algorithms to understand their strengths and weaknesses in various scenarios. The content here is suitable for learning, reference, and implementation in systems where caching is a critical performance factor.

## References

This content is adapted from a comprehensive article on cache replacement policies, summarizing the key algorithms and their applications in modern computing systems.

