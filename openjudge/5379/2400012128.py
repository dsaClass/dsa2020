from collections import deque
t= int(input().strip())
def check(a):  #检查是否合法
    queue=deque()
    try:
        for j in a:
            if j[0]=="+":
                queue.append(j[1])
            elif j[0]=="-":
                if j[1] == queue.popleft():
                    continue
                else:
                    return False
    except Exception:
        return False
    else:
        return True
for i in range(1,t+1):
    n=int(input().strip())
    lst=[_ for _ in input().strip().split()]
    if check(lst):
        print(f"Case {i}: yes")
    else:
        print(f"Case {i}: no")