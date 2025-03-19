class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class linklist:
    def __init__(self):
        nd = node(None, None)
        self.head = nd
        self.length = 0

    def push(self, data):
        nd = node(data, self.head.next)
        self.head.next = nd
        self.length += 1
        return None

    def pick(self):
        if self.length == 0:
            return None
        else:
            nd = self.head.next
            self.head.next = nd.next
            self.length -= 1
            return nd.data
        

s = input().split()
op = linklist()
num = linklist()
pre_is_number = False
for i in s:
    try:
        i = float(i)
    except:
        op.push((i, pre_is_number))
        pre_is_number = False
    else:
        while pre_is_number:
            # 连续两个数字出现，开始计算
            x = op.pick()
            if x[0] == '+':
                i = num.pick() + i
            elif x[0] == '-':
                i = num.pick() - i
            elif x[0] == '*':
                i = num.pick() * i
            else:
                i = num.pick() / i
            pre_is_number = x[1]
        num.push(i)
        pre_is_number = True
print(f'{num.pick():.1f}')
