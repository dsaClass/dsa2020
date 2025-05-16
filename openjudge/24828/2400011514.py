import sys
from collections import deque

def sliding_window_min_max(nums, k):
    n = len(nums)
    min_deque = deque()
    max_deque = deque()
    min_result = []
    max_result = []
    
    for i in range(n):
        # 维护最小值队列
        while min_deque and nums[i] <= nums[min_deque[-1]]:
            min_deque.pop()
        min_deque.append(i)
        # 移除不在窗口内的元素
        if min_deque[0] <= i - k:
            min_deque.popleft()
        
        # 维护最大值队列
        while max_deque and nums[i] >= nums[max_deque[-1]]:
            max_deque.pop()
        max_deque.append(i)
        # 移除不在窗口内的元素
        if max_deque[0] <= i - k:
            max_deque.popleft()
        
        # 当窗口大小达到k时记录结果
        if i >= k - 1:
            min_result.append(nums[min_deque[0]])
            max_result.append(nums[max_deque[0]])
    
    return min_result, max_result

def main():
    input_lines = sys.stdin.read().split()
    n, k = map(int, input_lines[:2])
    nums = list(map(int, input_lines[2:2+n]))
    min_res, max_res = sliding_window_min_max(nums, k)
    print(' '.join(map(str, min_res)))
    print(' '.join(map(str, max_res)))

if __name__ == '__main__':
    main()