# P0210：4 Values whose Sum is 0 (2442)
总时间限制: 15000ms 单个测试点时间限制: 5000ms 内存限制: 228000kB
## 描述
The SUM problem can be formulated as follows: given four lists A, B, C, D of integer values, compute how many quadruplet (a, b, c, d ) ∈ A x B x C x D are such that a + b + c + d = 0 . In the following, we assume that all lists have the same size n .

## 输入
The first line of the input file contains the size of the lists n (this value can be as large as 4000). We then have n lines containing four integer values (with absolute value as large as 228 ) that belong respectively to A, B, C and D .

## 输出
For each input file, your program has to write the number quadruplets whose sum is zero.

## 样例输入
    6
    -45 22 42 -16
    -41 -27 56 30
    -36 53 -37 77
    -36 30 -75 -46
    26 -38 -10 62
    -32 -54 -6 45

## 样例输出
    5

## 提示
Sample Explanation: Indeed, the sum of the five following quadruplets is zero: (-45, -27, 42, 30), (26, 30, -10, -46), (-32, 22, 56, -46),(-32, 30, -75, 77), (-32, -54, 56, 30).

