import sys
m=0
flag=True
for line in sys.stdin:
  c=list(map(int,line.strip().split()))
  if m==0:
    if flag:
      flag=False
    else:
      print(' ')
    n=c[0]
    m=c[1]
    a=[]
    b=[]
    s=n
    for i in range(n):
      a.append([i+1])
      b.append(i+1)
  else:
    x=c[0]
    y=c[1]
    m-=1
    if b[x-1]!=b[y-1]:
      print('No')
      a[b[x-1]-1]+=a[b[y-1]-1]
      a[b[y-1]-1]=[]
      for l in a[b[x-1]-1]:
        b[l-1]=b[x-1]
      s-=1
    else:
      print('Yes')
    if m==0:
      print(s)
      ma=0
      for i in range(n):
        if len(a[i])!=0:
          ma=i
      for i in range(n):
        if len(a[i])!=0:
          print(i+1,end='')
          if ma!=i:
            print(' ',end='')
          
          
      
  





        
    
    
