def merge_sort(arr):
    def sort(l,r): #左闭右闭区间 计算每次合并时的逆序对数
        if l >= r:
            return 0
        mid = (l+r)//2
        count = sort(l,mid) +sort(mid+1,r)
        i = l
        j = mid+1
        tem = []
        while i <= mid and j <= r:
            if arr[i] <= arr[j]:
                tem.append(arr[i])
                i+=1
            else:
                tem.append(arr[j])
                count += (mid-i+1)
                j+=1
        while i<= mid:
            tem.append(arr[i])
            i += 1
        while j<=r:
            tem.append(arr[j])
            j += 1
        arr[l:r+1]=tem
        return count
    return sort(0,len(arr)-1)
n=int(input())
arr = list(map(int, input().split()))
print(merge_sort(arr))