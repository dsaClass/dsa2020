import sys

data = sys.stdin.read().splitlines()
pigs = []
m_pigs = []

def push(x,pigs,m_pigs):
    pigs.append(x)
    if not m_pigs:
        m_pigs.append(x)
    elif x<=m_pigs[-1]:
        m_pigs.append(x)

for line in data:
    if line =="min":
        if m_pigs:
            print(m_pigs[-1])
    elif line =="pop":
        if pigs:
            x=pigs.pop()
            if x == m_pigs[-1]:
                m_pigs.pop()
    else:
        a,b = line.split()
        push(int(b),pigs,m_pigs)