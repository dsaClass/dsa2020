import sys
def convert(front, middle):
    if not front or not middle: return ""
    first = front[0]
    Index = middle.find(first)

    left_middle = middle[:Index]
    right_middle = middle[Index+1:]
    left_front = front[1:1+len(left_middle)]
    right_front = front[1+len(left_middle):]

    return convert(left_front, left_middle) + \
        convert(right_front, right_middle) + first

inpt = sys.stdin.readlines()
for line in inpt:
    front, middle = line.strip().split()
    print(convert(front, middle))