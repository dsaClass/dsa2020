n=int(input())
def ways(s,l):
    num = 0
    if s in l:
        return l[s]
    elif s<3:
        return 1
        l[s] = 1
    elif s<5:
        return ways(s-1,l)+ways(s-3,l)
        l[s] =  ways(s-1,l)+ways(s-3,l)
    else:
        return ways(s-1,l)+ways(s-3,l)+ways(s-5,l)
        l[s] = ways(s-1,l)+ways(s-3,l)+ways(s-5,l)
print(ways(n,{}))


