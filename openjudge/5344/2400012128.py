n,k = map(int,input().strip().split())
class Node:
    def __init__(self,data1,next=None):
        self.data = data1
        self.next = next
    def jianhuan(self,zch): #构建环链表
        if zch==1:
            self.next=header
        else:
            Node.jianhuan(self.next,zch-1)    

    def kk(self,c): #返回ob后第c个节点的数
        if c==1:
            return self
        else:
            return Node.kk(self.next,c-1)

header=None #header 表示现在所指的数
for i in range(n,0,-1):
    header=Node(i,header)
def chhuan(a,b): #构建环链表
    global header
    if b==1:
        a.next=header

    else:
        chhuan(a.next,b-1)
ans=[]
#chhuan(header,n)
Node.jianhuan(header,n)
ans.append(Node.kk(header,k-1).next.data)
header=Node.kk(header,k-1)
header.next=header.next.next
for i in range(n-2):
    ans.append(Node.kk(header,k).next.data)
    header=Node.kk(header,k)
    header.next=header.next.next
print(" ".join(map(str,ans)))



