'''
描述
   二叉搜索树在动态查表中有特别的用处，一个无序序列可以通过构造一棵二叉搜索树变成一个有序序列，构造树的过程即为对无序序列进行排序的过程。每次插入的新的结点都是二叉搜索树上新的叶子结点，在进行插入操作时，不必移动其它结点，只需改动某个结点的指针，由空变为非空即可。

   这里，我们想探究二叉树的建立和序列输出。

输入
只有一行，包含若干个数字，中间用空格隔开。（数字可能会有重复）
输出
输出一行，对输入数字建立二叉搜索树后进行前序周游的结果。
样例输入
41 467 334 500 169 724 478 358 962 464 705 145 281 827 961 491 995 942 827 436 
样例输出
41 467 334 169 145 281 358 464 436 500 478 491 724 705 962 827 961 942 995
'''


class node:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
    
def preOrderTraverse(root):
    if root is not None:
        print (root.data,end=" ")
        preOrderTraverse(root.lchild)
        preOrderTraverse(root.rchild)

def insert(root,value):
    if root is None:
        return node(value)
    if value<root.data:
        root.lchild=insert(root.lchild,value)
    elif value>root.data:
        root.rchild=insert(root.rchild,value)
    return root 


nums=list(map(int,input().split()))
head=node(nums[0])
for i in range(1,len(nums)):
    head=insert(head,nums[i])
preOrderTraverse(head)
