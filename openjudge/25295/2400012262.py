def find_counterfeit(weighings):
    coins = set('ABCDEFGHIJKL')
    possible_light = set(coins)
    possible_heavy = set(coins)

    for left, right, res in weighings:
        if res == 'even':
            possible_light -= set(left + right)
            possible_heavy -= set(left + right)
        elif res == 'up':
            possible_heavy &= set(left)
            possible_light &= set(right)
        elif res == 'down':
            possible_light &= set(left)
            possible_heavy &= set(right)

    if len(possible_light) == 1:
        coin = possible_light.pop()
        return f"{coin} is the counterfeit coin and it is light."
    elif len(possible_heavy) == 1:
        coin = possible_heavy.pop()
        return f"{coin} is the counterfeit coin and it is heavy."
    else:
        return "No counterfeit coin found."

n = int(input())
for _ in range(n):
    weighings = []
    for _ in range(3):
        left, right, res = input().split()
        weighings.append((left, right, res))
    print(find_counterfeit(weighings))
