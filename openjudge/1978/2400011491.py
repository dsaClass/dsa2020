p,e,i,d = map(int,input().split())
s = 1
if d < max(p,e,i):
    s = max(p,e,i)-d
while (d+s-p)%23 !=0 or (d+s-e)%28 !=0 or (d+s-i)%33 !=0:
    s+=1
print(s)