import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N, M = map(int, input[ptr:ptr+2])
    ptr +=2
    numbers = list(map(int, input[ptr:ptr+N]))
    ptr +=N
    
    max_bits = 16
    mods = [1 << (i+1) for i in range(max_bits)]
    bit_mod_counts = []
    for i in range(max_bits):
        mod = mods[i]
        count = [0] * mod
        for num in numbers:
            r = num % mod
            count[r] += 1
        bit_mod_counts.append(count)
    
    total_add = 0
    output = []
    for _ in range(M):
        cmd = input[ptr]
        if cmd == 'C':
            d = int(input[ptr+1])
            ptr +=2
            total_add += d
            total_add %= 65536
        elif cmd == 'Q':
            i = int(input[ptr+1])
            ptr +=2
            mod = mods[i]
            total_add_mod = total_add % mod
            target_low = (1 << i)
            target_high = (1 << (i+1)) - 1
            res = 0
            count = bit_mod_counts[i]
            # The range is [target_low - total_add_mod, target_high - total_add_mod] mod mod
            low = (target_low - total_add_mod) % mod
            high = (target_high - total_add_mod) % mod
            if low <= high:
                res = sum(count[low:high+1])
            else:
                res = sum(count[low:mod]) + sum(count[0:high+1])
            output.append(str(res))
    print('\n'.join(output))

if __name__ == '__main__':
    main()