class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def part_tree(i,n):
    if 2*i+1<=n:
        return (2*i,2*i+1)
    elif 2*i==n:
        return (n,-1)
    else:
        return (-1,-1)


def build_tree(m,n):
    tree_nodes=[None]*(n+1)
    for i in range(m,n+1):
        tree_nodes[i]=TreeNode(i)
    for i in range(m,n+1):
        
        left,right=part_tree(i,n)
        
        if left!=-1:
            tree_nodes[i].left=tree_nodes[left]
        if right!=-1:
            tree_nodes[i].right=tree_nodes[right]
        
    return tree_nodes[m]
def count_nodes(m,n):
    
    
    root=build_tree(m,n)
    
    def count(root):
        if root is None:
            return 0
        else:
            return 1+count(root.left)+count(root.right)

    return count(root)
    
statistics=[]
while True:
    
    nums=list(map(int,(input().strip()).split()))
    if nums!=[0,0]:
        statistics.append(nums)
    else:
        break
for nums in statistics:
    m,n=nums
    print(count_nodes(m,n))