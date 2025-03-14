
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

n,k=map(int,input().split())
head=Node(1)
cur=head
for i in range(2,n+1):
    cur.next=Node(i)
    cur=cur.next
cur.next=head
while(n>1):
    n-=1
    for _ in range(k-1):
        cur=cur.next
    print (cur.next.val,end=' ')
    cur.next=cur.next.next

