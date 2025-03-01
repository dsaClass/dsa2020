# 数据结构与算法B

谢正茂老师所授的13班在这里进行信息发布和课程讨论。
### 课程代码

代码行数多了，没有bug是不可能的。欢迎同学们批判的学习这里的课程代码，发现并解决其中的bug。对于代码可读性和效率的改进，讲出自己的道理，更是非常欢迎的。

### 上机作业

上机作业在openjudge子目录下，目前只收录两个来源的题目：
 - [数据结构与算法(Python语言实现)教材题库](http://dsbpython.openjudge.cn/dspythonbook/)
 - [课程同步作业](http://xzmdsa.openjudge.cn)

登录OJ账号之后请加入[数算B谢正茂班](http://xzmdsa.openjudge.cn),选择“数算B13班-2025春季”，把在班中的昵称改为“学号+姓名”，这样每次的作业和考试才会有成绩。

上机课时间为每周四5-6节，地点为计算中心7-8号机房
- 【腾讯文档】[数算B-13班上机座次表]( https://docs.qq.com/sheet/DSnhIcVJDTnVHcER0?tab=txwm2e)

前者里面有200道题；后者随课程进度发布，共8次左右作业，每次5-7题。

请阅读该目录下的README文件，本学期针对**先登**荣誉，每登提供0.2分的加分；对**夺旗**荣誉，每旗提供0.8的加分。为了让每个人都有参与的机会，限制每个github账户每天只能发起一次pull_request。

### Markdown格式

一种很受欢迎的写文档的工具。如果要写一本很“漂亮”的书，那是比不上LaTex的。Markdown可以通过嵌入html来获得一些丰富的格式，但对于在线文档，最简单的格式和功能就足够了。Markdown最大的好处是**简单高效**，高端的食材往往只需要最简单的烹饪方法。

参考：<br>
- [Markdown基本语法](https://www.markdownguide.org/basic-syntax/)
- [Obsidian](https://obsidian.md/) Markdown编辑工具

### 如何协作--提交代码并参与讨论

利用github.com的pull request功能，进行线上协作与讨论。

我们用的是一种Crowdsource的松散协作方式，maintainer之外的contributor对主仓库并不具有直接的写权限，需要先fork主仓库到自己的github账户下进行工作，根据工作的主题新开一个branch，在该branch下面完成工作后向主仓库提出pull request(pr)申请，maintainer和其他contributor可以review该pr，contributor根据别人的review可以修改pr的内容，最终满意后由maintainer把pr的工作内容合并进主仓库。流程基本就是：<br>
fork ==> branch ==> commit* ==> pull_request ==> (review, commit)* ==> merge,close<br>
contributor下次开新的branch的时候，并不需要每次都fork主仓库，和主仓库多同步以获得最新的内容。

常见的问题：
- contributor不要修改自己的main分支，而是新建branch上commit。为了避免版本冲突问题，main分支需要经常同步maintainer的仓库，尽可能每次branch前同步一次，在最新main上建新branch。
- 新建branch的名字应该与准备提交的内容有关，而且不应包含中文字符，否则github会报警；在发起pull request时应该对工作内容有简单的描述，描述中可以使用中文。
- 如果pr一个branch1有比较多的错误被退回，从main上新开一个branch2，比在branch1上作修改更方便。
- git主要的优势在于管理文本内容，因此非文本的内容在git仓库中尽量避免。非必要也不要在文档中插入图片。
- 对于一个pr，maintainer只能全部接受或全部拒绝，所以每次pr最好只有一个独立的工作。限制了一次pr频率，也即限制了工作的提交频率。


参考：<br>
[How to contribute to open source projects (our community project walkthrough)](https://www.youtube.com/watch?v=dLRA1lffWBw)

#### 国内镜像地址

由于在大陆地区访问github网站连接有不稳定的情况，这里另外提供了一个国内的[镜像](https://gitee.com/patrickxzm/dsa2020)。需要注意的是，该镜像是只读的，前面的协作功能只在github上进行。

这里有一些上网的资源可供利用：[Clash](https://blog.189854.xyz/blog/walless/2023/11/04/clash.html)|[验证PKU邮箱](https://189854.xyz/verify/)

### 课程进度、作业

| 时间  | 课程进度  | 作业                  |
| --- | ----- | ------------------- |
| 第一周 | 引言及概论 | 自学git，熟悉github、OJ功能| 
| 第二周 | Python入门| OJ作业[Python入门](http://xzmdsa.openjudge.cn/2025python/)|

###  重要通知
- 2/23/2025 因为在大家的提交中存在一些通病，暂停先登刷题的pr
- 2/25/2025 第三周（3/4/2025）上课时间随堂小测，考察Python基础技能

