import sys


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        # 创建哈希表，存储中序遍历中每个值的索引
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            # 前序遍历的第一个元素是根节点
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            # 在哈希表中查找根节点在中序遍历中的索引
            root_index = inorder_index_map[root_val]
            # 计算左子树的节点数量
            left_subtree_size = root_index - in_start
            # 递归构建左子树
            root.left = helper(pre_start + 1, pre_start + left_subtree_size, in_start, root_index - 1)
            # 递归构建右子树
            root.right = helper(pre_start + left_subtree_size + 1, pre_end, root_index + 1, in_end)
            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)

    def postorder(self, root):
        res = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return "".join(res)


s = Solution()
# 一次性读取所有输入
input_data = sys.stdin.read().split()
for i in range(0, len(input_data), 2):
    preorder = input_data[i]
    inorder = input_data[i + 1]
    root = s.buildTree(preorder, inorder)
    print(s.postorder(root))