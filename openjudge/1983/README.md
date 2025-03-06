# P1150:Sudoku

总时间限制: 2000ms 内存限制: 65536kB
# 描述
Sudoku is a very simple task. A square table with 9 rows and 9 columns is divided to 9 smaller squares 3x3 as shown on the Figure. In some of the cells are written decimal digits from 1 to 9. The other cells are empty. The goal is to fill the empty cells with decimal digits from 1 to 9, one digit per cell, in such way that in each row, in each column and in each marked 3x3 subsquare, all the digits from 1 to 9 to appear. Write a program to solve a given Sudoku-task. 
![图片](http://media.openjudge.cn/images/2982_1.jpg)
# 输入
The input data will start with the number of the test cases. For each test case, 9 lines follow, corresponding to the rows of the table. On each line a string of exactly 9 decimal digits is given, corresponding to the cells in this line. If a cell is empty it is represented by 0.
# 输出
For each test case your program should print the solution in the same format as the input data. The empty cells have to be filled according to the rules. If solutions is not unique, then the program may print any one of them.
# 样例输入
```
1
103000509
002109400
000704000
300502006
060000050
700803004
000401000
009205800
804000107
```
# 样例输出
```
143628579
572139468
986754231
391542786
468917352
725863914
237481695
619275843
854396127
```
