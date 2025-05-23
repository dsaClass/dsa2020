import heapq

data_set_count = 0

class Dir:
    def __init__(self, name):
        self.name = name #目录名
        self.subdirs = [] #子目录列表
        self.subfiles = [] #用最小堆存储文件，保证输出时文件按字母序排列

    def add_subdir(self, subdir):
        self.subdirs.append(subdir)

    def add_file(self, filename):
        heapq.heappush(self.subfiles, filename)

def get_sub(): #递归读取目录内容（目录名和文件名），直到遇到]表示当前目录结束
    root = Dir("ROOT")
    stack = [root]

    while True:
        line = input().strip()

        if line == "#":
            break

        if line == "*":
            global data_set_count
            data_set_count += 1
            print(f"DATA SET {data_set_count}:")
            print_dir(root, 0)
            print()
            return True

        elif line == "]":
            stack.pop()

        elif line[0] == 'd':
            new_dir = Dir(line)
            stack[-1].add_subdir(new_dir)
            stack.append(new_dir)

        elif line[0] == 'f':
            stack[-1].add_file(line)

    return False

def print_dir(d, level):
    print("|     " * level + d.name)
    for subdir in d.subdirs:
        print_dir(subdir, level + 1)
    while d.subfiles:
        print("|     " * level + heapq.heappop(d.subfiles))

if __name__ == "__main__":
    while get_sub():
        continue
