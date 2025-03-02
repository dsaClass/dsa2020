class TreeNode:
    def __init__(self, value): 
        self.value = value
        self.children = []

def parse_tree(s):
    stack = []
    node = None
    for char in s:
        if char.isalpha():  
            node = TreeNode(char)
            if stack:  
                stack[-1].children.append(node)
        elif char == '(':  
            if node:
                stack.append(node)  
                node = None
        elif char == ')':  
            if stack:
                node = stack.pop()  
    return node  

def preorder(node):
    output = [node.value]
    for child in node.children:
        output.extend(preorder(child))
    return ''.join(output)

def postorder(node):
    output = []
    for child in node.children:
        output.extend(postorder(child))
    output.append(node.value)
    return ''.join(output)


def main():
    s = input().strip()
    s = ''.join(s.split())  
    root = parse_tree(s)  
    if root:
        print(preorder(root))  
        print(postorder(root))  
    else:
        print("input tree string error!")

if __name__ == "__main__":
    main()
