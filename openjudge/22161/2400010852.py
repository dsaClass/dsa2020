import heapq
import re
import sys
class Node:
    def __init__(self,weight,min_char,left=None,right=None):
        self.weight=weight
        self.min_char=min_char
        self.left=left
        self.right=right
    def __lt__(self,other):
        if self.weight<other.weight:
            return True
        elif self.weight==other.weight:
            return self.min_char<other.min_char
        else:
            return False
def build_huffman_tree(n,characters):
    heap=[]
    for char,weight in characters:
        heapq.heappush(heap,Node(weight,char))
    while len(heap)>1:
        left=heapq.heappop(heap)
        right=heapq.heappop(heap)
        new_weight=left.weight+right.weight
        new_min_char=min(left.min_char,right.min_char)
        parent=Node(new_weight,new_min_char,left,right)
        heapq.heappush(heap,parent)
    return heapq.heappop(heap)if heap else None
def build_code_dict(root):
    code_dict={}
    def traverse(node,current_code):
        if node is None:
            return
        if node.left is None and node.right is None:
            code_dict[node.min_char]=current_code
            return
        traverse(node.left,current_code+'0')
        traverse(node.right,current_code+'1')
    traverse(root,'')
    return code_dict
def main():
    n=int(sys.stdin.readline())
    characters=[]
    for _ in range(n):
        parts=sys.stdin.readline().split()
        char=parts[0]
        weight=int(parts[1])
        characters.append((char,weight))
    root=build_huffman_tree(n,characters)
    code_dict=build_code_dict(root)
    for line in sys.stdin:
        line=line.strip()
        if re.fullmatch('[01]*',line):
            result=[]
            current_node=root
            if current_node is None:
                print('')
                continue
            for bit in line:
                if current_node is None:
                    break
                if bit=='0':
                    current_node=current_node.left
                else:
                    current_node=current_node.right
                if current_node is None:
                    break
                if current_node.left is None and current_node.right is None:
                    result.append(current_node.min_char)
                    current_node=root
            if current_node==root and root is not None and root.left is None and root.right is None:
                result.append(root.min_char)
            print(''.join(result))
        else:
            encoded=[]
            valid=True
            for char in line:
                if char not in code_dict:
                    valid=False
                    break
                encoded.append(code_dict[char])
            if valid:
                print(''.join(encoded))
            else:
                print('')
if __name__=="__main__":
    main()
