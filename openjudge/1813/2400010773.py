import copy


Move = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def isLegal(r, c):
    return 0 <= r < 5 and 0 <= c < 6


def reverseBits(r, c, temp, m):
    temp[r][c] ^= 1  # 0 变为 1，1 变为 0
    for dr, dc in Move:
        rr, cc = r + dr, c + dc
        if isLegal(rr, cc):
            temp[rr][cc] ^= 1


def solve(m):
    for i in range(32):  
        temp = copy.deepcopy(m)
        solution = [[0 for _ in range(6)] for _ in range(5)]
        t = i
        for j in range(5):  
            if t & 1:
                reverseBits(j, 0, temp, m)
                solution[j][0] = 1
            t >>= 1
        for j in range(1, 6):  
            for k in range(5):
                if temp[k][j - 1]:  
                    reverseBits(k, j, temp, m)
                    solution[k][j] = 1
        flag = True
        for j in range(5):  
            if temp[j][5]:
                flag = False
                break
        if flag:
            for r in range(5):  
                print(' '.join(str(solution[r][c]) for c in range(6)))
            return


def main():
    m = [[int(x) for x in input().split()] for _ in range(5)]
    solve(m)

if __name__ == "__main__":
    main()