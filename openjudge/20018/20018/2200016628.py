def count_overtaking_events(speeds):
    n = len(speeds)
    # 创建(位置,速度)对
    ants = [(i, speeds[i]) for i in range(n)]
    
    # 使用归并排序统计赶超事件
    def merge_sort(arr, left, right):
        if left >= right:
            return 0
        
        mid = (left + right) // 2
        count = merge_sort(arr, left, mid) + merge_sort(arr, mid + 1, right)
        
        # 统计跨越中点的赶超事件
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if arr[i][1] < arr[j][1]:  # 如果左边蚂蚁速度小于右边蚂蚁速度
                count += right - j + 1  # 右边所有蚂蚁都会超过左边这只蚂蚁
                i += 1
            else:
                j += 1
        
        # 合并两个有序数组
        temp = []
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if arr[i][1] <= arr[j][1]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        
        while i <= mid:
            temp.append(arr[i])
            i += 1
        
        while j <= right:
            temp.append(arr[j])
            j += 1
        
        # 将临时数组复制回原数组
        for i in range(left, right + 1):
            arr[i] = temp[i - left]
        
        return count
    
    return merge_sort(ants, 0, n - 1)

def main():
    n = int(input())
    speeds = []
    for _ in range(n):
        speeds.append(int(input()))
    
    result = count_overtaking_events(speeds)
    print(result)

if __name__ == "__main__":
    main()