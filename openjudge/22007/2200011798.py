answer=False
def output(A):
    global answer
    answer=True
    s=''
    for i in A:
        s+=str(i)+' '
    print(s)
        

def queen(A, cur=0):
    if cur == len(A):
        output(A)
        return 0
    for col in range(len(A)):  # 遍历当前行的所有位置
        A[cur] = col
        for row in range(cur):  # 检查当前位置是否相克
            if A[row] == col or abs(col - A[row]) == cur - row:
                break
        else:  # 如果完成了整个遍历，则说明位置没有相克
            queen(A, cur+1)  # 计算下一行的位置
queen([None]*int(input()))
if answer==False:
    print('NO ANSWER')