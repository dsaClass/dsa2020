sym = ['+','-','*','/']
def calculate(L):
    if len(L) == 1:
        return L[0]
    i = -1
    while True:
        i += 1
        if L[i] in sym and L[i+1] not in sym and L[i+2] not in sym:
            if L[i] == '+':
                L[i] = L[i+1]+L[i+2]
            elif L[i] == '-':
                L[i] = L[i+1]-L[i+2]
            elif L[i] == '*':
                L[i] = L[i+1]*L[i+2]
            elif L[i] == '/':
                L[i] = L[i+1]/L[i+2]
            return calculate(L[:i+1:]+L[i+3::])
if __name__ == '__main__':
    l = list(input().split(' '))
    for i in range(len(l)):
        try:
            l[i] = float(l[i])
        except Exception:
            continue
    print('%.6f' %calculate(l))
