n=int(input())
string1=input()
string2=input()
list1=string1.split()
list2=string2.split()
i=0
while i<n:
    list1[i]=int(list1[i])
    list2[i]=int(list2[i])
    i=i+1
alist=list1+list2
alist.sort()
j=0
while j<2*n-1:
    print(alist[j],end=" ")
    j=j+1
else:
    print(alist[2*n-1])






