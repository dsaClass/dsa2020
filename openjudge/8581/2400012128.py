
class treenode():
    def __init__(self,val,left = None,right = None,parent = None):
        self.value = val
        self.left = left
        self.right = right
        self.p = parent

s = input().strip()
count = 0
root = treenode(s[0])
current = root

while count <= len(s) - 2:

    k = treenode(s[count+1])
    if current.left == None and current.value != '.':
        current.left = k
        k.p = current
        current = k
        count += 1
    elif current and not current.p.right:
        current.p.right = k
        k.p = current.p
        current = k
        count += 1
    elif current.p.left and current:
        current = current.p
        continue

def in1(root,a):
    if root.value != '.':
        in1(root.left,a)

        a.append(root.value)
        in1(root.right,a)
    return a
def post(root,b):
    if root.value != '.':
        post(root.left,b)
        post(root.right,b) 
        b.append(root.value)
    return b

ans1 = in1(root,[])
ans2 = post(root,[])
print(''.join(ans1))
print(''.join(ans2))
        