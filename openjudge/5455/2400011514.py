import sys
from collections import deque

# 定义二叉树节点结构
class Node:
    def __init__(self, val):
        self.val = val      # 节点的值
        self.left = None    # 左子节点
        self.right = None   # 右子节点

# 插入函数：在BST中插入新值，并忽略重复值
def insert(root, val):
    if root is None:
        # 如果当前树为空，创建一个新节点
        return Node(val)
    if val < root.val:
        # 如果插入值小于当前节点值，则递归插入到左子树
        root.left = insert(root.left, val)
    elif val > root.val:
        # 如果插入值大于当前节点值，则递归插入到右子树
        root.right = insert(root.right, val)
    # 当val等于root.val时（重复），直接返回不插入
    return root

def main():
    # 从标准输入读取所有数据并去除两端的空白符
    data = sys.stdin.read().strip()
    if not data:
        return
    
    # 将输入字符串以空格拆分，并转换为整数列表
    numbers = list(map(int, data.split()))
    
    root = None
    seen = set()  # 用于记录已出现的数字，防止重复插入
    # 遍历输入的数字列表
    for num in numbers:
        if num not in seen:
            seen.add(num)
            root = insert(root, num)  # 只对未出现的数字进行插入操作
    
    # 如果树为空，直接结束
    if root is None:
        return
    
    # 层次遍历BST，使用deque作为队列实现
    queue = deque([root])
    result = []  # 存储遍历结果的列表
    while queue:
        node = queue.popleft()  # 弹出队首节点
        result.append(str(node.val))  # 将节点的值转换为字符串并加入结果列表
        if node.left:
            queue.append(node.left)  # 如果左子节点存在，加入队列
        if node.right:
            queue.append(node.right)  # 如果右子节点存在，加入队列
    
    # 输出结果。使用" ".join(result)连接所有节点的值，并确保输出结尾没有多余空格和换行。
    print(" ".join(result), end="")

if __name__ == "__main__":
    main()
