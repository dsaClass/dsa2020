def merge_and_count(arr, temp_arr, left, right):
    if left == right:
        return 0
    mid = (left + right) // 2
    inv_count = merge_and_count(arr, temp_arr, left, mid)
    inv_count += merge_and_count(arr, temp_arr, mid + 1, right)
    inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count

def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

def count_inversions(arr, n):
    temp_arr = [0] * n
    return merge_and_count(arr, temp_arr, 0, n - 1)

n = int(input())
arr = list(map(int, input().split()))
print(count_inversions(arr, n))