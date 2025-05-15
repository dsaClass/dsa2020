import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    num = int(line)
    print(bin(num)[2:])