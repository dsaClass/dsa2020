import itertools
n = int(input().strip())
# num = [_ for _ in range(1,n+1)]
numbers = [_**3 for _ in range(1,n+1)]
numbers_set = set(numbers)
ans = []
for i in itertools.combinations_with_replacement(numbers[1:],3):
    if sum(i) in numbers_set:
        ans.append((round(sum(i)**(1/3)),round(i[0]**(1/3)),round(i[1]**(1/3)),round(i[2]**(1/3))))
ans.sort(key = lambda x:x[0])
for i in ans:
    print(f"Cube = {i[0]}, Triple = ({i[1]},{i[2]},{i[3]})")
        