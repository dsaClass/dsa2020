def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

def count_trees(m, pre, post):
    if not pre or not post:
        return 1
    if pre[0] != post[-1]:
        return 0
    root = pre[0]
    pre = pre[1:]
    post = post[:-1]
    n = len(pre)
    if n == 0:
        return 1
    child_indices = []
    i = 0
    while i < n:
        child = pre[i]
        j = post.find(child)
        child_indices.append((i, j))
        i = j + 1
    k = len(child_indices)
    if k == 0:
        return 1
    res = 1
    for i in range(k):
        start_pre = pre[child_indices[i][0]:child_indices[i][1]+1]
        start_post = post[child_indices[i][0]:child_indices[i][1]+1]
        res *= count_trees(m, start_pre, start_post)
    res *= comb(m, k)
    return res

def main():
    while True:
        line = input().strip()
        if line == '0':
            break
        m, s1, s2 = line.split()
        m = int(m)
        if len(s1) != len(s2):
            print(0)
            continue
        if s1[0] != s2[-1]:
            print(0)
            continue
        result = count_trees(m, s1, s2)
        print(result)

if __name__ == '__main__':
    main()