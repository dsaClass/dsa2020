import sys


def build_tree(lines):
    root = {'label': lines[0].strip(), 'children': []}
    stack = [{'node': root, 'depth': 0}]

    for line in lines[1:]:
        depth = line.count('\t')
        label = line.strip()

        # Find the parent node
        while stack[-1]['depth'] >= depth:
            stack.pop()

        parent = stack[-1]['node']
        new_node = {'label': label, 'children': []}
        parent['children'].append(new_node)
        stack.append({'node': new_node, 'depth': depth})

    return root


def preorder(node):
    result = [node['label']]
    for child in node['children']:
        result.extend(preorder(child))
    return result


def postorder(node):
    result = []
    for child in node['children']:
        result.extend(postorder(child))
    result.append(node['label'])
    return result


if __name__ == "__main__":
    lines = [line.rstrip('\n') for line in sys.stdin]
    if not lines:
        print("")
        print("")
    else:
        tree = build_tree(lines)
        pre = ''.join(preorder(tree))
        post = ''.join(postorder(tree))
        print(pre)
        print(post)