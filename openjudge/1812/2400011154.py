N=int(input())
a,b,c,d=1,1,1,1
s=[]
l=[]
for i in range (N+1):
    s.append(i**3)
for a in range (2,N+1):
    for b in range(a,2,-1):
        for c in range(b,2,-1):
            if s[a]-s[b]-s[c] in s and 1<s[a]-s[b]-s[c]<=s[c]:
                d=s.index(s[a]-s[b]-s[c])
                l.append((a,d,c,b))
l.sort(key=lambda x :( x[0] , x[1] , x [2]))
for i in l :
    print(f'Cube = {i[0]}, Triple = ({i[1]},{i[2]},{i[3]})')
