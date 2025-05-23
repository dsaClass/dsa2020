import sys
sys.setrecursionlimit(10000)
class node:
    def __init__(self, data):
        self.data = data
        self.leftson = None
        self.rightson = None

def buildtree(line):
    num = 0
    i = 0
    numstack = []
    opstack = []
    pre_is_num = False
    while i < len(line):
        stack = []
        if line[i] != '(':
            if line[i] == '*':
                opstack.append('*')
                pre_is_num = False
            elif line[i] == '+':
                if not opstack:
                    opstack.append('+')
                    pre_is_num = False
                else:
                    x = opstack.pop()
                    if x == '+':
                        opstack.append('+')
                        opstack.append('+')
                        pre_is_num = False
                    else:
                        b = numstack.pop()
                        a = numstack.pop()
                        n = node('*')
                        n.leftson = a
                        n.rightson = b
                        numstack.append(n)
                        # 把应当优先计算的子表达式树压入numstack
                        opstack.append('+')
                        pre_is_num = False
            else:
                if pre_is_num:
                    x = numstack.pop()
                    x.data += line[i]
                    numstack.append(x)
                else:
                    numstack.append(node(line[i]))
                    pre_is_num = True
            i += 1
        else:
            num += 1
            j = i + 1
            while num:
                if line[j] == ')':
                    num -= 1
                elif line[j] == '(':
                    num += 1
                stack.append(line[j])
                j += 1
            stack.pop()
            numstack.append(buildtree(stack))
            # 得到了括号内的子表达式树，压入numstack
            i = j
            pre_is_num = False
    # numstack与opstack维护完毕，现在构建表达式树
    while opstack:
        op = opstack.pop()
        b = numstack.pop()
        a = numstack.pop()
        n = node(op)
        n.leftson = a
        n.rightson = b
        numstack.append(n)
    # 最后一个n就是整个树
    return numstack.pop()
                        
def write(tree):
    if tree.data == '+':
        return write(tree.leftson) + '+' + write(tree.rightson)
    if tree.data == '*':
        ans = ''
        l = tree.leftson
        r = tree.rightson
        if l.data == '+':
            ans += '(' + write(l) + ')'
        else:
            ans += write(l)
        ans += '*'
        if r.data == '+':
            ans += '(' + write(r) + ')'
        else:
            ans += write(r)
        return ans    
    return tree.data

for line in sys.stdin:
    line = line.strip()
    if line:
        print(write(buildtree(line)))
    