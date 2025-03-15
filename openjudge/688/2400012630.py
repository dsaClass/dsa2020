import re
from collections import defaultdict

def tokenize(expr):
    expr=expr.replace(" ", "")  # 移除空格
    return re.findall(r'\d+|[a-zA-Z]+|[+\-*/()]',expr)  

def parse_expression(expr) :
    expr=expr.replace(" ", "")  # 清除空格
    tokens=tokenize(expr) 
    postfix=infix_to_postfix(tokens)  # 转换为后缀表达式
    return evaluate_postfix(postfix)  # 计算后缀表达式，返回系数字典

def infix_to_postfix(tokens) :
    precedence={'+':1,'-':1,'*':1}  
    output=[]
    stack=[]

    for token in tokens :
        if token.isalnum() :  
            output.append(token)
        elif token in precedence: 
            while stack and stack[-1] in precedence and precedence[stack[-1]]>=precedence[token] :
                output.append(stack.pop())
            stack.append(token)
        elif token=='(' :
            stack.append(token)
        elif token==')' :
            while stack and stack[-1]!='(' :
                output.append(stack.pop())
            stack.pop()  
    while stack :
        output.append(stack.pop())  
    return output

def evaluate_postfix(postfix) :
    stack = []
    for token in postfix :
        if token.isdigit() :  
            stack.append({'':int(token)}) 
        elif token.isalpha() :
            stack.append({token: 1})  
        else :
            b=stack.pop()
            a=stack.pop()
            result=defaultdict(int)

            if token=='+' :
                for key in a :
                    result[key]+=a[key]
                for key in b :
                    result[key]+=b[key]
            elif token=='-' :
                for key in a :
                    result[key]+=a[key]
                for key in b :
                    result[key]-=b[key]
            elif token=='*' :
                for key_a,val_a in a.items() :
                    for key_b,val_b in b.items() :
                        combined_vars=''.join(sorted(key_a+key_b))
                        result[combined_vars]+=val_a*val_b

            filtered=defaultdict(int)
            for k,v in result.items() :
                if v!=0:
                    filtered[k]=v
            stack.append(filtered)

    final_result={k:v for k,v in stack[0].items() if v!=0}
    return final_result

def judge_equivalence(expr1,expr2):
    return "YES" if parse_expression(expr1)==parse_expression(expr2) else "NO"

# 读取输入
N=int(input())
for _ in range(N):
    expr1=input().strip()
    expr2=input().strip()
    print(judge_equivalence(expr1,expr2))