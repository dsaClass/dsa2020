def hanoi(n, start, end, auxiliary):
    if n == 1:
        print(f"{start}->{end}")
    else:
        hanoi(n-1, start, auxiliary, end)
        print(f"{start}->{end}")
        hanoi(n-1, auxiliary, end, start)

n = int(input())
hanoi(n, 'A', 'C', 'B')