n=int(input())
matrix=[[0 for _ in range(2*n-1)] for _ in range(2*n-1)]
i=1
hang=0
lie=n-1
matrix[hang][lie]=i
while i < (2*n-1)**2 :
    i+=1
    temp_hang=hang
    temp_lie=lie
    hang=(hang+2*n-2)%(2*n-1)
    lie=(lie+2*n)%(2*n-1)
    if matrix[hang][lie] != 0 :
        temp_hang=(temp_hang+1)%(2*n-1)
        matrix[temp_hang][temp_lie]=i
        hang=temp_hang
        lie=temp_lie
    elif matrix[hang][lie] == 0 :
        matrix[hang][lie] = i 
    
for s in matrix:
    print(*s)
