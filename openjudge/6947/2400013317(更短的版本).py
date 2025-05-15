class Node:
    def __init__(self,d1,d2,father=None):
        self.d1,self.d2,self.father=d1,d2,father
a=input()
count=[-1]*(len(a)+1)
d1,d2=0,0
p=Node(0,0)
lst=[p]
for k in a:
    if k=='d':
        d2+=1
        count[d2]+=1
        d1+=1+count[d2]
        p=Node(d1,d2,father=p)
        lst.append(p)
    if k=='u':
        d1-=1+count[d2]
        d2-=1
        count[d2+2]=-1
        p=p.father
for node in lst:
    if node.d1>d1:
        d1=node.d1
    if node.d2>d2:
        d2=node.d2
print(f'{d2} => {d1}')
