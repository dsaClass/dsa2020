## P0910:Common Subsequence

- 总时间限制: 1000ms
- 内存限制: 65536kB

- 描述

  A subsequence of a given sequence is the given sequence with some elements (possible none) left out. Given a sequence X = < x1, x2, ..., xm > another sequence Z = < z1, z2, ..., zk > is a subsequence of X if there exists a strictly increasing sequence < i1, i2, ..., ik > of indices of X such that for all j = 1,2,...,k, xij = zj. For example, Z = < a, b, f, c > is a subsequence of X = < a, b, c, f, b, c > with index sequence < 1, 2, 4, 6 >. Given two sequences X and Y the problem is to find the length of the maximum-length common subsequence of X and Y.

- 输入

  The program input is from the std input. Each data set in the input contains two strings representing the given sequences. The sequences are separated by any number of white spaces. The input data are correct.

- 输出

  For each set of data the program prints on the standard output the length of the maximum-length common subsequence from the beginning of a separate line.

- 样例输入

  ```
  abcfbc         abfcab 
  programming    contest  
  abcd           mnp
  ```

- 样例输出

  ```
  4 
  2 
  0
  ```