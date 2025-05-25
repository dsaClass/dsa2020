from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read().split()
    n = int(input[0])
    data = list(map(int, input[1:]))
    
    A = data[0::4]
    B = data[1::4]
    C = data[2::4]
    D = data[3::4]
    
    sum_ab = defaultdict(int)
    for a in A:
        for b in B:
            sum_ab[a + b] += 1
    
    count = 0
    for c in C:
        for d in D:
            target = - (c + d)
            count += sum_ab.get(target, 0)
    
    print(count)

if __name__ == "__main__":
    main()