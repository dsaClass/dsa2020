# P1230:Cow Contest
------

总时间限制: 1000ms 内存限制: 65536kB

### 描述

N (1 ≤ N ≤ 100) cows, conveniently numbered 1..N, are participating in a programming contest. As we
all know, some cows code better than others. Each cow has a certain constant skill rating that is unique
among the competitors.

The contest is conducted in several head-to-head rounds, each between two cows. If cow A has a greater
skill level than cow B (1 ≤ A ≤ N; 1 ≤ B ≤ N; A ≠ B), then cow A will always beat cow B.

Farmer John is trying to rank the cows by skill level. Given a list the results of M (1 ≤ M ≤ 4,500) two-
cow rounds, determine the number of cows whose ranks can be precisely determined from the results. It
is guaranteed that the results of the rounds will not be contradictory.

### 输入

* Line 1: Two space-separated integers: N and M
* Lines 2..M+1: Each line contains two space-separated integers that describe the competitors
and results (the first integer, A, is the winner) of a single round of competition: A and B

### 输出

* Line 1: A single integer representing the number of cows whose ranks can be determined

### 样例输入
```
5 5  
4 3  
4 2  
3 2  
1 2  
2 5  
```
### 样例输出
```
2
```
### 来源

USACO 2008 January Silver

