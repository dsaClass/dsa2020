n=input()
while(n!='0'):
    a=input().split()
    b=sorted(a,key=int)
    print(' '.join(map(str,b)))
    n = input()

