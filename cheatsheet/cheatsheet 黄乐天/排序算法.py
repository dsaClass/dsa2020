#插入排序
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#二分插入排序：用二分查找确定插入位置
def binary_insertion_sort(arr):
    def binary_search(sub_arr, key, start, end):
        while start < end:
            mid = (start + end) // 2
            if sub_arr[mid] < key:
                start = mid + 1
            else:
                end = mid
        return start

    for i in range(1, len(arr)):
        key = arr[i]
        # 找到应该插入的位置
        insert_pos = binary_search(arr, key, 0, i)
        # 移动元素为 key 腾出位置
        for j in range(i, insert_pos, -1):
            arr[j] = arr[j - 1]
        arr[insert_pos] = key


#Shell 排序
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # 初始间隔

    while gap > 0: #可替换为 for gap in gaps
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # 对每个组执行插入排序
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2 
    return arr


#选择排序
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


#堆排序
def heapify(arr, n, i):
    largest = i         # 假设当前节点是最大值
    l = 2 * i + 1        # 左子节点
    r = 2 * i + 2        # 右子节点

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        heapify(arr, n, largest)  # 递归调整子树

def heap_sort(arr):
    n = len(arr)

    # 1. 建堆：从最后一个非叶子节点向上调整
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 2. 取出堆顶元素放末尾
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # 最大值移到末尾
        heapify(arr, i, 0)  # 重新构建堆


#冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # 标记是否发生交换
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # 提前结束：数组已经有序


#快速排序
def partition(alist, start, end):
    pivot = alist[start]      
    low = start
    high = end

    while low < high:
        # 从右向左找第一个比 pivot 小的数
        while low < high and alist[high] >= pivot:
            high -= 1
        alist[low] = alist[high]  # 把小的值移到左边空位

        # 从左向右找第一个比 pivot 大的数
        while low < high and alist[low] <= pivot:
            low += 1
        alist[high] = alist[low]  # 把大的值移到右边空位

    # 最后把 pivot 填回当前 low 所在的空位
    alist[low] = pivot
    return low  # 返回 pivot 的最终位置

def quick_sort(alist, start, end):
    if start < end:
        pivot_index = partition(alist, start, end)
        quick_sort(alist, start, pivot_index - 1)  # 左边
        quick_sort(alist, pivot_index + 1, end)    # 右边

#归并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # 合并两个有序数组
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # 稳定排序（相等取左边）
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 剩余元素直接拼接
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort([1,2,3]))