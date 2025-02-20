def div(L,M,V):
    sum = 0 
    for i in L:
        sum += int(i/V)
    if sum >= M:
        return 1
    return 0
def find(L,M,V1,V2):
    if V2-V1 <= 1e-5:
        return V1
    else:
        if div(L,M,(V1+V2)/2):
            return find(L,M,(V1+V2)/2,V2)
        return find(L,M,V1,(V1+V2)/2)
if __name__ == '__main__':
    import math
    l = list(map(int,input().split()))
    n = l[0]
    m = l[1]+1 # == F+1
    pie = list(map(lambda x:x*x*math.pi,map(int,input().split())))
    v2 = max(pie)
    print('%.3f' %find(pie,m,0,v2))
    
'''
def find(L,M,V1,V2):
    while V2-V1 > 1e-5:
        if div(L,M,(V1+V2)/2):
            V1 = (V1+V2)/2
        else:
            V2 = (V1+V2)/2
    return V1
'''