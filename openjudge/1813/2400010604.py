def flip(light, x, y, pressed):
    if pressed:
        if x >= 0 and x < 5 and y >= 0 and y < 6:
            light[x][y] ^= 1

def press_button(light, x, y):
    flip(light, x, y, True)
    flip(light, x - 1, y, True)
    flip(light, x + 1, y, True)
    flip(light, x, y - 1, True)
    flip(light, x, y + 1, True)

def find_solution(light):
    for i in range(0, 1 << 6):
        copy_light = [row[:] for row in light]
        button_state = []
        for j in range(6):
            if (i >> j) & 1:
                press_button(copy_light, 0, j)
                button_state.append(1)
            else:
                button_state.append(0)
        
        for x in range(1, 5):
            for y in range(6):
                if copy_light[x - 1][y] == 1:
                    press_button(copy_light, x, y)
                    button_state.append(1)
                else:
                    button_state.append(0)
        
        if all(copy_light[4][y] == 0 for y in range(6)):
            return button_state
    return None

def main():
    light = [list(map(int, input().split())) for _ in range(5)]
    solution = find_solution(light)
    if solution:
        for i in range(5):
            print(' '.join(map(str, solution[i * 6:(i + 1) * 6])))

if __name__ == "__main__":
    main()