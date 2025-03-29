start=list(map(int,input().strip()))
end=list(map(int,input().strip()))
n=len(start)

list1=start.copy()
list2=start.copy()
way1=[1]
way2=[0]

for i in range(n-1):
    list1[i], list1[i+1]=list1[i] ^ way1[i], list1[i+1] ^ way1[i]
    list2[i], list2[i+1]=list2[i] ^ way2[i], list2[i+1] ^ way2[i]
    way1.append(list1[i]^end[i])
    way2.append(list2[i]^end[i])

if list1[n-1]^way1[n-1]!=end[n-1] and list2[n-1]^way2[n-1]!=end[n-1]:
    print("impossible")
elif list1[n-1]^way1[n-1]!=end[n-1]:
    print(way2.count(1))
elif list2[n-1]^way2[n-1]!=end[n-1]:
    print(way1.count(1))
else:
    print(min(way2.count(1),way1.count(1)))
