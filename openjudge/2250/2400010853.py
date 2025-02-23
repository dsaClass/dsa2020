import sys
for num in sys.stdin:
    num=int(num.strip())
    print(bin(num)[2:])