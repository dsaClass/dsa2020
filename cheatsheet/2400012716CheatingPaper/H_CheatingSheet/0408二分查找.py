'''
250408:矩形分割
查看提交统计提问
总时间限制: 1000ms 内存限制: 65536kB
描述
平面上有一个大矩形，其左下角坐标（0，0），右上角坐标（R,R)。大矩形内部包含一些小矩形，小矩形都平行于坐标轴且互不重叠。所有矩形的顶点都是整点。要求画一根平行于y轴的直线x=k（k是整数) ，使得这些小矩形落在直线左边的面积必须大于等于落在右边的面积，且两边面积之差最小。并且，要使得大矩形在直线左边的的面积尽可能大。注意：若直线穿过一个小矩形，将会把它切成两个部分，分属左右两侧。

输入
第一行是整数R，表示大矩形的右上角坐标是(R,R) (1 <= R <= 1,000,000)。
接下来的一行是整数N,表示一共有N个小矩形(0 < N <= 10000)。
再接下来有N 行。每行有4个整数，L,T, W 和 H, 表示有一个小矩形的左上角坐标是(L,T),宽度是W，高度是H (0<=L,T <= R, 0 < W,H <= R). 小矩形不会有位于大矩形之外的部分。
输出
输出整数n，表示答案应该是直线 x=n。 如果必要的话，x=R也可以是答案。
样例输入
1000
2
1 1 2 1
5 1 2 1
样例输出
5
'''

def cut_rectangle(lef,rig):
    if lef==rig:
        return lef
    elif lef+1==rig:
        return lef
    else:
        mid=(lef+rig)//2
        m=sum(rou[:mid])
        n=sum(rou[mid:])
        if m>=n:
            return cut_rectangle(lef,mid)
        else:
            return cut_rectangle(mid,rig)


R=int(input())
rectangle_number=int(input())
rou=[0]*R
for _ in range(rectangle_number):
    L,T,W,H=map(int,input().split())
    for i in range(L,L+W):
        rou[i]+=H
division=cut_rectangle(0,R)
for i in range(division,R+1):
    m=sum(rou[:i])
    n=sum(rou[i:])
    if n==0:
        print(R)
        break
    if m>=n:
        if rou[i]!=0:
            print(i)
            break
        else:
            while rou[i]==0 and i!=R:
                i+=1
            print(i)
            break
            
