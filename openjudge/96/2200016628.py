from collections import deque


def topological_sort(n, graph, in_degree):
    q = deque()
    temp_in = in_degree[:]
    result = ''
    for i in range(n):
        if temp_in[i] == 0:
            q.append(i)
    multiple_choices = False

    while q:
        if len(q) > 1:
            multiple_choices = True  # 多种可能
        u = q.popleft()
        result += chr(ord('A') + u)
        for v in graph[u]:
            temp_in[v] -= 1
            if temp_in[v] == 0:
                q.append(v)

    if len(result) < n:
        return "INCONSISTENT", ''
    elif multiple_choices:
        return "UNCERTAIN", ''
    else:
        return "DETERMINED", result


def main():
    while True:
        line = input()
        if not line:
            continue
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break

        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        determined = False

        for i in range(m):
            relation = input().strip()
            a = ord(relation[0]) - ord('A')
            b = ord(relation[2]) - ord('A')
            graph[a].append(b)
            in_degree[b] += 1

            status, seq = topological_sort(n, graph, in_degree)
            if status == "INCONSISTENT":
                print(f"Inconsistency found after {i + 1} relations.")
                # 丢弃剩余输入
                for _ in range(i + 1, m):
                    input()
                break
            elif status == "DETERMINED":
                print(f"Sorted sequence determined after {i + 1} relations: {seq}.")
                # 丢弃剩余输入
                for _ in range(i + 1, m):
                    input()
                break
        else:
            print("Sorted sequence cannot be determined.")


if __name__ == "__main__":
    main()