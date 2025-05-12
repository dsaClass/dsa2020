class Tree: # 树类
    def __init__(self, val):
        self.value = val
        self.lc = None
        self.rc = None
    def addlc(self, lct): # 添加左子
        self.lc = lct
    def addrc(self, rct): # 添加右子
        self.rc = rct
    def pre(self, op): # 前序周游
        op(self)
        if self.lc:
            self.lc.pre(op)
        if self.rc:
            self.rc.pre(op)
    def mid(self, op): # 中序周游
        if self.lc:
            self.lc.mid(op)
        op(self)
        if self.rc:
            self.rc.mid(op)
    def post(self, op): # 后续周游
        if self.lc:
            self.lc.post(op)
        if self.rc:
            self.rc.post(op)
        op(self)

nodelist = []
while True: # 读入每一行，将其表示为含有含有层和值的元组。
    try:
        anode = input()
        nodelist.append((len(anode) - 1, anode[-1]))
    except:
        break

inx = 0 # 序号
def buildtree(): # 通过递归建立树
    global inx
    tree = Tree(nodelist[inx][1]) # 根节点
    level = nodelist[inx][0] # 根节点对应的层数
    inx += 1 # 移动到下一个节点
    if inx < len(nodelist) and nodelist[inx][0] == level + 1: # 有左子树或者有右子树
        if nodelist[inx][1] != '*': # 有左子树
            lct = buildtree() # 递归得到左子树
            tree.addlc(lct) # 本树的左子树设置为得到的左子树
        else:
            inx += 1 # 没有左子树，考虑下一行
        if inx < len(nodelist) and nodelist[inx][0] == level + 1: # 有右子树
            rct = buildtree() # 递归得到右子树
            tree.addrc(rct) # 当前树的右子树设置为得到的右子树
    else: # 无左子树或者右子树：
        pass
    return tree

st = buildtree() # 建立树
st.pre(lambda x: print(x.value, end='')) # 前序周游并且输出
print('')
st.mid(lambda x: print(x.value, end='')) # 中序周游并且输出
print('')
st.post(lambda x: print(x.value, end='')) # 后序周游并且输出
