#感觉和分盘子有点像
def num_of_plates(n,m):
    if n==0:
        return 1
    elif m==1:
        return 1
    else:
        if n-m>=0:
            return num_of_plates(n-m,m)+num_of_plates(n,m-1)

        else:
            return num_of_plates(n,n)
while True:
    try:
        n = int(input())
        if 0 < n <= 50:
            print(num_of_plates(n,n))
    except EOFError:
        break
