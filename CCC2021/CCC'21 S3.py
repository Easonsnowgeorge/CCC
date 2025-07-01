import sys

input = sys.stdin.readline  # 使用更快的输入方法，因为可能有多达200k行的输入

n = int(input())  # 读取参与者的数量
pos = []  # 存储参与者的初始位置
speed = []  # 存储参与者的移动速度
max_range = []  # 存储参与者已经能听到的范围

# 读取每个参与者的信息
for _ in range(n):
    p, s, r = map(int, input().split())
    pos.append(p)
    speed.append(s)
    max_range.append(r)


def get_time(target, pos, speed, max_range):
    diff = abs(target - pos)  # 计算到目标点的距离
    if max_range >= diff:  # 如果已经在能听到的范围内
        return 0
    else:  # 如果不在范围内，计算所需时间
        return (diff - max_range) * speed


low, high = 0, 1_000_000_000  # 初始化二分查找的范围
while high >= low:
    mid = low + (high - low) // 2
    middle = sum(get_time(mid, pos[i], speed[i], max_range[i]) for i in range(n))
    lower = sum(get_time(mid-1, pos[i], speed[i], max_range[i]) for i in range(n))
    upper = sum(get_time(mid+1, pos[i], speed[i], max_range[i]) for i in range(n))

    # 找到总时间最小的点
    lowest = min(lower, middle, upper)
    if lowest == lower:
        high = mid - 1
    elif lowest == middle:
        print(middle)  # 找到最佳点，输出总时间并结束循环
        break
    elif lowest == upper:
        low = mid + 1
