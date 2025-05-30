import sys

def find_sum(line,n):
    dp=[0]*(n+1)
    for i in range(1,n+1):
        dp[i]=max(dp[i-1]+line[i-1],line[i-1])
    return max(dp)

def calculate_column(height,matrix,n):#height*k(k从1-n)矩阵和的最大值
    global max_sum
    for j in range(n - height):  # j表示取得是哪几个连续行（从j开始）
        column = []
        for i in range(0,n):#如tie可考虑用列前缀和处理，此处的i表示横坐标到哪行了
            column.append(sum(line[i] for line in matrix[j:j+height+1]))
        summ=find_sum(column,n)
        if summ>max_sum:
            max_sum=summ

def main():
    global max_sum
    max_sum=-10000000
    n=int(input())
    inp=sys.stdin.read().strip()
    matrix=[[0]*n for _ in range(n)]
    i=j=0
    for strs in inp.split():
        matrix[i][j]=int(strs)
        j+=1
        if j==n:
            j-=n
            i+=1
    for h in range(n):
        calculate_column(h, matrix, n)
    print(max_sum)

if __name__=='__main__':
    main()