row,col,str=input().split(maxsplit=2)
row=int(row)
col=int(col)
dict={' ':0}
dict_letters={chr(i) : i-64 for i in range(65,91)}
dict.update(dict_letters)
sk=''
for s in str:
    num=dict[s]
    sk+=format(num,'05b')

required_length=row*col
sk = sk.ljust(required_length, '0')

datas=[[0 for _ in range(col)]for _ in range(row)]

sum=0
top = 0
bottom = row - 1
left = 0
right = col - 1

while top<=bottom and left<=right and sum < required_length:
    for i in range(left, right + 1):
        if sum >= required_length:
            break
        datas[top][i]=sk[sum]
        sum+=1
    top += 1

    for i in range(top, bottom + 1):
        if sum >= required_length:
            break
        datas[i][right]=sk[sum]
        sum+=1
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            if sum >= required_length:
                break
            datas[bottom][i]=sk[sum]
            sum+=1
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            if sum >= required_length:
                break
            datas[i][left]=sk[sum]
            sum+=1
        left += 1

result=''.join(''.join(row) for row in datas)
print(result)
