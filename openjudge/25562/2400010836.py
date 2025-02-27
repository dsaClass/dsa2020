def c(k):
    if ans[k]+1:
        return ans[k]
    else:
        s = sum(c(k-1-j)*c(j) for j in range(k))  #见学号.md文件
        ans[k] = s
        return s
n = int(input())
ans = [-1 for i in range(n+1)]
ans[0] = 1
print(c(n))