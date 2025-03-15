# 字符串全排列
def permute(s,curent,used,result):
    if len(curent) == len(s): # 如果长度相等，则说明已经排列完毕，加入result中
        result.append(curent)
        return
    
    for i in range(len(s)): 
        if not used[i]: # 如果没有使用过，则使用
            used[i] = True
            permute(s,curent + s[i],used,result) # 递归调用
            used[i] = False # 回溯，探索下一个分支

def generate(s):
    result = []
    used = [False] * len(s)
    permute(s,'',used,result)
    return result

s = input()

result = generate(s)
for r in result:
    print(r)