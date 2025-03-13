from collections import defaultdict  #免去普通dict的一些麻烦
count = 0  #data set 序数

class doc: #定义文件（夹）
    def __init__(self,name = None):
        self.name = name
        self.children = defaultdict(doc)
        self.father = None
        self.layer = 0
    def add(self,k): #向children中加入文件
        self.children[k]
    def getList(self): #按题目要求get .children中的文件
        D = []
        F = []
        for i in self.children:
            if i.name[0] == 'd':
                D.append(i)
            else:
                F.append(i)
        return D+sorted(F,key = lambda x:x.name)
    def clean(self): #清空信息，以免不同data set之间同名文件出现混用（似乎不太需要这一步）
        self.children = defaultdict(doc)
        self.father = None

def show(x): #递归方法实现目录输出
    l = x.getList()
    for i in range(len(l)):
        if l[i].name[0] == 'd':
            print('|     '*l[i].layer+l[i].name)
            show(l[i])
        else:
            print('|     '*l[i].layer+l[i].name)
            if i == len(l)-1:
                l[i].clean()

def work(x): #处理一份data
    global count
    flag = 1
    current = doc('ROOT')
    root = current
    root.layer = 0
    while True:
        if flag:
            s = x
            flag = 0
        else:
            s = input()
        if s == '*':
            layer = 0
            print(f'DATA SET {count}:')
            print('ROOT')
            show(root)
            break
        if s[0] == 'd':
            d = doc(s)
            current.add(d)
            c = current
            current = d
            current.father = c
            current.layer = c.layer+1
        elif s[0] == 'f':
            d = doc(s)
            current.add(d)
            d.layer = current.layer
        else: #类似栈结构处理']'
            current = current.father

while True:
    s = input()
    if s == '#':
        break
    count += 1
    if count > 1:
        print() #不要忘记输出data sets间空行
    work(s)
