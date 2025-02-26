def tablenach(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return tablenach(n-1)+tablenach(n-2)+tablenach(n-3)
    
print(tablenach(int(input())))