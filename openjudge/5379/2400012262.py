n=int(input())
for j in range(1,1+n):
    s=int(input())
    queue=[] #维护一个队列
    sa=True
    datas=input().split()
    for i in datas:
        if i[0] == '+':
            queue.append(i[1])
        elif i[0] == '-':
            if i[1] in queue:
                if i[1] == queue[0]:
                    queue.pop(0)
                else:
                    sa=False
            else:
                sa=False
    if sa == False:    
        print(f'Case {j}: no')
    elif sa == True:
        print(f'Case {j}: yes')
