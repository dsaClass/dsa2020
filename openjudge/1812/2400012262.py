n=int(input())
dict={i:i**3 for i in range(2,n+1)}
for a in range(6,n+1):
    for b in range(2,a-2):
        for c in range(b+1,a-1):
            for d in range(c+1,a):
                if dict[a]==dict[b]+dict[c]+dict[d]:
                    print(f'Cube = {a}, Triple = ({b},{c},{d})')
