#先读一遍整个列表，然后在maxPrice[i]中存储第i天及以后的最高价格，然后计算每一天可能的收益。

a=list(map(int,input().split())) # 读入一列不知个数的整数，并把它们存入列表a。这是很常用的写法，应该记住

n=len(a)
maxPrice=[0 for i in range(n)]

for i in range(n-1,-1,-1):
    if i==n-1:
        maxPrice[i]=a[i]
    else:
        maxPrice[i]=max(a[i],maxPrice[i+1])

maxProfit=max(maxPrice[i]-a[i] for i in range(n)) #这里是省略的写法，用了Python中的迭代器。感兴趣的同学可以自行向ai或者助教询问这句代码的原理.

print(maxProfit)