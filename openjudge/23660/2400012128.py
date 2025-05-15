t = int(input().strip())

def search(n, nums, target):
    if n == 0 and target%7 == 0:
        return 1
   
    elif n ==0  and target%7 != 0:
        return 0
    
    a = nums[n-1]
    return search(n-1, nums[:n-1], target) + search(n-1, nums[:n-1], (target-a)%7)
for _ in range(t):
    lst0 = list(map(int, input().strip().split()))
    n = lst0[0]
    nums = lst0[1:]
    ans = search(n,nums,0)
    print(ans)