def find_perfect_cubes_further_optimized(N):
    cubes = [i ** 3 for i in range(N + 1)]
    cubes_set = set(cubes)
    for a in range(2, N + 1):
        a_cubed = cubes[a]
        for b in range(2, a):
            b_cubed = cubes[b]
            for c in range(b, a):
                c_cubed = cubes[c]
                d_cubed = a_cubed - b_cubed - c_cubed
                if d_cubed < c_cubed:
                    break
                if d_cubed in cubes_set:
                    d = round(pow(d_cubed, 1 / 3))
                    if cubes[d] == d_cubed and c <= d < a:
                        print(f"Cube = {a}, Triple = ({b},{c},{d})")

N = int(input())
find_perfect_cubes_further_optimized(N)
