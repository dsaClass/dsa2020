import math

def solve_case(n, d, islands):
    # Step 1: 计算每个岛屿的可覆盖的x坐标区间
    ranges = []
    for x, y in islands:
        # 计算岛屿到海岸线的距离
        distance_from_coast = abs(y)
        # 如果岛屿的距离大于雷达的覆盖距离 d，直接返回-1
        if distance_from_coast > d:
            return -1
        # 计算岛屿在x轴上的覆盖范围
        max_x = x + math.sqrt(d ** 2 - distance_from_coast ** 2)
        min_x = x - math.sqrt(d ** 2 - distance_from_coast ** 2)
        ranges.append((min_x, max_x))
    
    # Step 2: 按照每个岛屿的最小x坐标排序
    ranges.sort(key=lambda x: x[1])  # 按照最大x坐标排序
    
    # Step 3: 贪心算法
    radar_count = 0
    last_installed_radar = -float('inf')
    
    for start, end in ranges:
        # 如果当前岛屿无法被上一个雷达覆盖
        if last_installed_radar < start:
            radar_count += 1
            last_installed_radar = end
    
    return radar_count

def main():
    case_number = 1
    while True:
        n, d = map(int, input().split())
        if n == 0 and d == 0:
            break
        
        islands = []
        for _ in range(n):
            x, y = map(int, input().split())
            islands.append((x, y))
        
        # 计算并输出结果
        result = solve_case(n, d, islands)
        if result == -1:
            print(f"Case {case_number}: -1")
        else:
            print(f"Case {case_number}: {result}")
        
        case_number += 1
        input()  # 跳过空行

if __name__ == "__main__":
    main()
