n, w = map(int, input().split())
candies = []

for _ in range(n):
    value, weight = map(int, input().split())
    candies.append((value, weight, value / weight))  # 添加性价比

# 按照单位价值从高到低排序
candies.sort(key=lambda x: x[2], reverse=True)

total_value = 0.0
remaining_weight = w

for value, weight, ratio in candies:
    if remaining_weight >= weight:
        total_value += value
        remaining_weight -= weight
    else:
        total_value += ratio * remaining_weight
        break

print(f"{total_value:.1f}")
