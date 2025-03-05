from collections import deque
import sys
data=sys.stdin.read().strip().split()
t=int(data[0])
idx=1
result=[]
for _ in range(t):
    n = int(data[idx])
    idx += 1
    dq = deque()
    for _ in range(n):
        op = int(data[idx])
        if op == 1:
            dq.append(int(data[idx + 1]))
            idx += 2
        elif op == 2:
            if dq:
                if data[idx + 1] == "0":
                    dq.popleft()
                else:
                    dq.pop()
            idx += 2
    result.append(" ".join(map(str, dq)) if dq else "NULL")
sys.stdout.write("\n".join(result) + "\n")