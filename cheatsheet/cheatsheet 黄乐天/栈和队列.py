#判断出栈序列是否合法
from collections import deque
def judge(push,pop):
    if len(push)!=len(pop): #确保长度相等
        return 'NO' 
    l=[]
    ss=deque(pop)
    for i in push:
        l.append(i)
        while l and l[-1]==ss[0]:
            l.pop()
            ss.popleft()
    if len(ss)==0:
        return('YES')
    else:
        return('NO')
    

#判断是否为栈（队列：改为popleft即可）
from collections import deque
def judge_stack(l):
    s=[] 
    # s=deque()
    for i in l:
        if i[0]==1:
            s.append(i[1])
        else:
            if not s:
                return False
            n=s.pop() 
            # n=s.popleft()
            if n!=i[1]:
                return False
    return len(s)==0


#计算后缀表达式的值：先弹出在右   输入中以空格分隔，若无空格，用下题c.iddigit部分代码或下下题tokenize
def evaluate_postfix(expr: str) -> float:
    stack = []
    tokens = expr.split()
    for token in tokens:
        if token[0].isdigit():
            stack.append(float(token))
        else:
            b = stack.pop()  # 先弹右操作数
            a = stack.pop()  # 再弹左操作数
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
    return stack[0]

#计算前缀表达式的值，反向遍历，先弹出在左
def eval_prefix(expr: str) -> float:
    stack = []
    tokens = list(expr[::-1])  # 反向遍历字符
    for token in tokens:
        if token[0].isdigit():
            stack.append(float(token))
        else:
            a = stack.pop()
            b = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
    return stack[0]




#计算一个中缀表达式的值。支持整数、多位数、空格、()+-*/^。
def precedence(op: str) -> int:
    """返回运算符优先级：数值越大，优先级越高。"""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':          # 如果支持幂运算
        return 3
    return 0

def apply_op(values: list, ops: list):
    """从 values 栈里弹出两个值，从 ops 栈里弹出一个运算符，计算后把结果压回 values。"""
    right = values.pop()
    left  = values.pop()
    op    = ops.pop()
    if op == '+':
        values.append(left + right)
    elif op == '-':
        values.append(left - right)
    elif op == '*':
        values.append(left * right)
    elif op == '/':
        values.append(left / right)
    elif op == '^':
        values.append(left ** right)

#main
def evaluate_infix(expr: str) -> float:
    values = []   # 值栈
    ops    = []   # 运算符栈

    i = 0
    n = len(expr)
    while i < n:
        c = expr[i]
        # 1) 如果是空格，跳过
        if c.isspace():
            i += 1
            continue

        # 2) 如果是左括号，直接入 ops
        if c == '(':
            ops.append(c)
            i += 1

        # 3) 如果是数字，可能是多位数，一次读完整个数字（支持float)
        elif c.isdigit():
            start=i
            while i < n and (expr[i].isdigit() or expr[i]=='.'):
                i+=1
            num=float(expr[start:i])

            values.append(num)

        # 4) 如果是右括号，持续弹出并计算直到遇到左括号
        elif c == ')':
            while ops and ops[-1] != '(':
                apply_op(values, ops)
            ops.pop()  # 弹出左括号 '('
            i += 1

        # 5) 如果是运算符 + - * / ^
        else:
            # 在将当前运算符压栈之前，
            # 先把栈顶所有优先级 >= 当前的运算符都计算掉
            while ops and precedence(ops[-1]) >= precedence(c):
                apply_op(values, ops)
            ops.append(c)
            i += 1

    # 6) 扫描结束，剩余运算符全部计算
    while ops:
        apply_op(values, ops)

    # 值栈顶即结果
    return values[0]




#中缀表达式转化为前、后缀表达式。同时得到一个拆分字符串中浮点数的函数
PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
RIGHT_ASSOC = {'^'} #左结合

def is_number(tok: str) :
    """判断 token 是否为数字（整数或小数）。输出bool"""
    try:
        float(tok)
        return True
    except ValueError:
        return False
    
#将中缀字符串拆成 token 列表（数字、运算符、括号）。支持多位数与小数，没有强制空格分隔。
def tokenize(expr: str):
    tokens, buf = [], ''
    for ch in expr:
        if ch.isdigit() or ch == '.':
            buf += ch
        else:
            if buf:
                tokens.append(buf)
                buf = ''
            if ch.isspace():
                continue
            tokens.append(ch)
    if buf:
        tokens.append(buf)
    return tokens

# 中缀 → 后缀（Shunting-yard 算法） ----------
def infix_to_postfix(expr: str) -> str:
    """输入：中缀表达式字符串（允许紧凑或带空格）  
    输出：以空格分隔的后缀表达式"""

    output, ops = [], []           # 输出列表与运算符栈
    for tok in tokenize(expr):
        if is_number(tok):  # 数字直接输出
            output.append(tok)
        elif tok == '(':
            ops.append(tok)
        elif tok == ')':
            # 弹出直到遇到左括号，并弹出(
            while ops and ops[-1] != '(':
                output.append(ops.pop())
            ops.pop() 
        else:
            # 运算符：弹出所有优先级更高或相等（且左结合）的运算符
            while (ops and ops[-1] != '(' and
                   (PRECEDENCE[ops[-1]] > PRECEDENCE[tok] or
                    (PRECEDENCE[ops[-1]] == PRECEDENCE[tok] and tok not in RIGHT_ASSOC))):
                output.append(ops.pop())
            ops.append(tok)
    # 最后把剩余运算符都输出
    while ops:
        output.append(ops.pop())
    return ' '.join(output)  #空格分隔

#中缀 → 前缀（反转 + 中缀→后缀 + 再反转）
def infix_to_prefix(expr: str) -> str:
    # 1) 对expr反序并交换括号
    toks = tokenize(expr)[::-1]
    toks = ['(' if t == ')' else ')' if t == '(' else t for t in toks]
    # 2) 得到反向后缀
    rev_post = infix_to_postfix(' '.join(toks)).split()
    # 3) 结果反序即为前缀
    return ' '.join(rev_post[::-1])



#用前、后缀表达式建立表达式树
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree_from_postfix(tokens):
    stack = []
    operators = set('+-*/')

    for token in tokens:
        if token not in operators:
            stack.append(TreeNode(token))  # 操作数：建叶节点
        else:
            right = stack.pop()
            left = stack.pop()
            node = TreeNode(token)
            node.left = left
            node.right = right
            stack.append(node)

    return stack[0]  # 栈中最后一个元素是根

def build_tree_from_prefix(tokens):
    stack = []
    operators = set('+-*/')

    for token in reversed(tokens):
        if token not in operators:
            stack.append(TreeNode(token))
        else:
            left = stack.pop()
            right = stack.pop()
            node = TreeNode(token)
            node.left = left
            node.right = right
            stack.append(node)

    return stack[0]

#表达式树的中序遍历，得到中缀表达式，实现前缀转中缀
def inorder(node):
    if not node:
        return ''
    if not node.left and not node.right:
        return node.val
    return '(' + inorder(node.left) + node.val + inorder(node.right) + ')'



#约瑟夫问题 （n为人数 m为淘汰的序号）
from collections import deque
def remain(n,m):
    q=deque([i for i in range(1,n+1)])
    count=1
    while len(q)>1:
        a=q.popleft()
        if count %m !=0:
            q.append(a)
        count+=1
    return q[0]
