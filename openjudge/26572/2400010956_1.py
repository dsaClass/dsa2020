import sys
sys.setrecursionlimit(10000)
def chai(line):
    num = 0
    pre = -1
    aft = -1
    cur = 2
    ans = ''
    i = 0
    while i < len(line):
        stack = []
        if line[i] != '(':
            if line[i] == '+':
                pre = 0
                cur = 0
            elif line[i] == '*':
                pre = 1
                cur = min(cur, 1)
            ans += line[i]
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
            tmp = chai(stack)
            if tmp[1] < pre:
                ans += '(' + tmp[0] + ')'
                i = j
                continue
            else:
                if j < len(line):
                    aft = 0 if line[j] == '+' else 1
                    if tmp[1] >= aft:
                        ans += tmp[0]
                        i = j
                        aft = -1
                        continue
                    else:
                        ans += '(' + tmp[0] + ')'
                        i = j
                        aft = -1
                        continue
                else:
                    ans += tmp[0]
                    i = j
                    continue
    return (ans, cur)
                        
                    
for line in sys.stdin:
    line = line.strip()
    if line:
        print(chai(line)[0])
    