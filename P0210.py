def count(A, B, C, D):
    count = 0
    map = {}
    for a in A:
        for b in B:
            sum_ab = a + b
            if sum_ab in map:
                map[sum_ab] += 1
            else:
                map[sum_ab] = 1
    for c in C:
        for d in D:
            sum_cd = c + d
            if -sum_cd in map:
                count += map[-sum_cd]
    return count
n = int(input())
A = [0] * n
B = [0] * n
C = [0] * n
D = [0] * n
for i in range(n):
    a, b, c, d = map(int, input().split())
    A[i], B[i], C[i], D[i] = a, b, c, d
result = count(A, B, C, D)
print(result)
