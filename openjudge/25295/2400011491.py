n = int(input())
coin_w = ['heavy','light']
for _ in range(n):
    fake = {}
    true = []
    for i in range(3):
        inp = input().split()
        if inp[2] == 'even':
            for j in inp[0]+inp[1]:
                if j not in true:
                    true.append(j)
        elif inp[2] == 'up':
            for j in inp[0]:
                if fake.get(j) ==1:
                    true.append(j)
                    continue
                fake[j] = 0
            for j in inp[1]:
                if fake.get(j) ==0:
                    true.append(j)
                    continue
                fake[j] = 1
        elif inp[2] == 'down':
            for j in inp[0]:
                if fake.get(j) ==0:
                    true.append(j)
                    continue
                fake[j] = 1
            for j in inp[1]:
                if fake.get(j) ==1:
                    true.append(j)
                    continue
                fake[j] = 0
    for k in fake:
        if k not in true:
            print(f'{k} is the counterfeit coin and it is {coin_w[fake[k]]}.')
            break