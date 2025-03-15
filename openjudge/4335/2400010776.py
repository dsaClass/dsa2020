n=int(input())
ban=[]
for i in range(n):
    l=int(input())
    ban.append(l)
s=0
for i in range(n-1):
    ban.sort()
    s+=ban[0]+ban[1]
    ban.append(ban[0]+ban[1])
    ban.remove(ban[0])
    ban.remove(ban[0])
print(s)