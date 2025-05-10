import bisect
n=int(input())
lst=[]
count=0
for i in range(n):
    a=int(input())
    pos = bisect.bisect_left(lst,a)
    bisect.insort_left(lst, a)
    count += pos
print(count)