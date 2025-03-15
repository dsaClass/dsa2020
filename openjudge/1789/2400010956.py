import functools
que = list(map(int, input().split()))
ans = []
@functools.lru_cache
def calculate(*num:int):
    if len(num) == 1:
        return {num[0]}
    elif len(num) == 2:
        if num[0] != 0:
            if num[1] != 0:
                return {num[0] + num[1], num[0] - num[1], num[0] * num[1], num[0] / num[1], num[1] / num[0], num[1] - num[0]}
            else:
                return {num[0], 0, - num[0]}
        else:
            if num[1] != 0:
                return {num[1], 0, - num[1]}
            else:
                return {0}
    elif len(num) == 3:
        ans = set()
        for i in calculate(num[1], num[2]):
            ans.update(calculate(num[0], i))
        for i in calculate(num[0], num[2]):
            ans.update(calculate(num[1], i))
        for i in calculate(num[0], num[1]):
            ans.update(calculate(num[2], i))
        return ans
        
while que != [0, 0, 0, 0]:
    over = False
    for i in calculate(que[1], que[2], que[3]):
        for k in calculate(que[0], i):
            if -1e-3 < k - 24 < 1e-3: 
                ans.append('YES')
                over = True
                break
        else:
            continue
        break
    if not over:
        for i in calculate(que[0], que[2], que[3]):
            for k in calculate(que[1], i):
                if -1e-3 < k - 24 < 1e-3: 
                    ans.append('YES')
                    over = True
                    break
            else:
                continue
            break
    if not over:
        for i in calculate(que[0], que[1], que[3]):
            for k in calculate(que[2], i):
                if -1e-3 < k - 24 < 1e-3: 
                    ans.append('YES')
                    over = True
                    break
            else:
                continue
            break
    if not over:
        for i in calculate(que[0], que[1], que[2]):
            for k in calculate(que[3], i):
                if -1e-3 < k - 24 < 1e-3: 
                    ans.append('YES')
                    over = True
                    break
            else:
                continue
            break
    if not over:
        for i in calculate(que[0], que[1]):
            for j in calculate(que[2], que[3]):
                for k in calculate(i, j):
                    if -1e-3 < k - 24 < 1e-3: 
                        ans.append('YES')
                        over = True
                        break
                else:
                    continue
                break
            else:
                continue
            break
    if not over:
        for i in calculate(que[0], que[2]):
            for j in calculate(que[1], que[3]):
                for k in calculate(i, j):
                    if -1e-3 < k - 24 < 1e-3: 
                        ans.append('YES')
                        over = True
                        break
                else:
                    continue
                break
            else:
                continue
            break
    if not over:
        for i in calculate(que[0], que[3]):
            for j in calculate(que[1], que[2]):
                for k in calculate(i, j):
                    if -1e-3 < k - 24 < 1e-3: 
                        ans.append('YES')
                        over = True
                        break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            ans.append('NO')
    que = list(map(int, input().split()))
for i in ans:
    print(i)
