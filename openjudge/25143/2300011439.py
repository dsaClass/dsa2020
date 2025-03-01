n = int(input())
left = [-1] * n
right = [-1] * n
children = set()

for i in range(n):
    l, r = map(int, input().split())
    left[i] = l
    right[i] = r
    if l != -1:
        children.add(l)
    if r != -1:
        children.add(r)

root = -1
for i in range(n):
    if i not in children:
        root = i
        break

def get_height(node):
    if node == -1:
        return 0
    return max(get_height(left[node]), get_height(right[node])) + 1

height = get_height(root) - 1

def count_leaves(node):
    if node == -1:
        return 0
    if left[node] == -1 and right[node] == -1:
        return 1
    return count_leaves(left[node]) + count_leaves(right[node])

leaves = count_leaves(root)

print(height, leaves)