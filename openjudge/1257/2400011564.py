def premidtopost(pre:str, mid:str):
    if len(pre) <= 1:
        return pre
    root = pre[0] # 前序表达式的第一个是root
    pos = mid.index(root) # 找到root在中序表达式中的位置。
    lmid = mid[0:pos] # 中序表达式中，在root左边的是左子树的中序表达式。
    lpre = pre[1:pos + 1] # 前序表达式中，root后面紧跟着是左子树的前序表达式，注意到前序表达式的长度应该和中序表达式一样。
    rmid = mid[pos + 1:] # 中序表达式中root右边的是右子树的中序表达式。
    rpre = pre[pos + 1:] # 前序表达式中，左子树的前序表达式之后紧跟着右子树的前序表达式。
    return premidtopost(lpre, lmid) + premidtopost(rpre, rmid) + root # 按照“左，右，根”来返回后序表达式。

while True:
    try:
        a, b = input().split()
    except:
        exit(0) # 读入长度未知的数据。
        
    print(premidtopost(a, b))
