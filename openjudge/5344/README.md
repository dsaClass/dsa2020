# 250203:最后的最后

## 描述

<dd><p>&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://baike.baidu.com/item/%E5%BC%97%E6%8B%89%E7%BB%B4%E5%A5%A5%C2%B7%E7%BA%A6%E7%91%9F%E5%A4%AB%E6%96%AF/1894583" target="_self">弗拉维奥·约瑟夫斯</a>是1世纪的一名犹太历史学家。他在自己的日记中写道，在一次战中，他和他的40个战友被罗马军队包围在洞中。他们讨论是自杀还是被俘，最终决定自杀，并以抽签的方式决定谁杀掉谁。约瑟夫斯和另外一个人是最后两个留下的人。约瑟夫斯说服了那个人，他们将向罗马军队投降，不再自杀。约瑟夫斯把他的存活归因于运气或天意，他不知道是哪一个。</p><p>&nbsp;&nbsp; 在计算机科学与数学中，就有一个以此命名的问题：<strong>约瑟夫斯问题</strong>（有时也称为<strong>约瑟夫斯置换</strong>）。在计算机编程的算法中，类似问题又称为<strong>约瑟夫环</strong>。具体描述如下：有<img class="tex" alt="n" src="http://upload.wikimedia.org/math/7/b/8/7b8b965ad4bca0e41ab51de7b31363a1.png">个囚犯站成一个圆圈，准备处决。首先从一个人开始，越过<img class="tex" alt="k-2" src="http://upload.wikimedia.org/math/7/2/1/721e20007292e8066d890e8d365d268d.png">个人（因为第一个人已经被越过），并杀掉第<em>k</em>个人。接着，再越过<img class="tex" alt="k-1" src="http://upload.wikimedia.org/math/1/4/4/14464ac1dfe6fa8ad8fda94bb6f01571.png">个人，并杀掉第<em>k</em>个人。这个过程沿着圆圈一直进行，直到最终只剩下一个人留下，这个人就可以继续活着。问题是，给定了<img class="tex" alt="n" src="http://upload.wikimedia.org/math/7/b/8/7b8b965ad4bca0e41ab51de7b31363a1.png">和<img class="tex" alt="k" src="http://upload.wikimedia.org/math/8/c/e/8ce4b16b22b58894aa86c421e8759df3.png">，一开始要站在什么地方才能避免被处决？</p><p>&nbsp;&nbsp; 为了让大家熟悉循环链表的使用，对该题进行模拟。我们要求将之前的所有被kill掉的囚犯的编号输出。<br></p><p><br></p></dd>

## 输入

题中描述的囚犯数n（即编号为1至n，n不大于1000）和间隔数k（k大于等于2，小于n） 

## 输出

顺序输出被kill掉的囚犯的编号，中间以空格隔开

## 样例输入

`10 2`

## 样例输出

`2 4 6 8 10 3 7 1 9`
