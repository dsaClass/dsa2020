'''可以直接用python的sort()（代码见注释），此处也自己写了一个，两种方法均可AC'''

def merge_sort(lists):
    if len(lists) <= 1:
        return lists

    middle = len(lists) // 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # 将较小值放入到result中
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 剩余直接追加
    if i == len(left):
        result.extend(right[j:])
    else:
        result.extend(left[i:])

    return result

ans=[]
while True:
    n=int(input())
    if n==0:
        break
    line=list(map(int,input().split()))
    # line.sort()
    # ans.append(line)
    ans.append(merge_sort(line))

for i in ans:
    print(*i,sep=' ')