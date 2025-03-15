i0, i1, i2 = 0, 1, 1
for _ in range(0, int(input())-2):
    i2, i1, i0 = i0+i1+i2, i2, i1
print(i2)
