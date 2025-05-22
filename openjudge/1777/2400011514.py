class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirs = []
        self.files = []

def process_test_case(lines, case_number):
    root = Directory('ROOT')
    stack = [root]
    current_dir = root

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line == ']':
            if len(stack) > 1:
                stack.pop()
                current_dir = stack[-1]
        elif line.startswith('d'):
            new_dir = Directory(line)
            current_dir.subdirs.append(new_dir)
            stack.append(new_dir)
            current_dir = new_dir
        elif line.startswith('f'):
            current_dir.files.append(line)

    print(f"DATA SET {case_number}:")
    print("ROOT")
    print_directory(root, 0)

def print_directory(directory, level):
    for subdir in directory.subdirs:
        indent = '|     ' * (level + 1)
        print(f"{indent}{subdir.name}")
        print_directory(subdir, level + 1)
    for filename in sorted(directory.files):
        indent = '|     ' * level
        print(f"{indent}{filename}")

import sys

def main():
    input_lines = []
    for line in sys.stdin:
        line = line.strip()
        if line == '#':
            break
        input_lines.append(line)
    
    test_cases = []
    current_case = []
    for line in input_lines:
        if line == '*':
            test_cases.append(current_case)
            current_case = []
        else:
            current_case.append(line)
    
    for i, case in enumerate(test_cases, 1):
        process_test_case(case, i)
        if i < len(test_cases):
            print()

if __name__ == "__main__":
    main()