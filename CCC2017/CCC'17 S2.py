n = int(input())  # 读取数组元素个数
arr = input().split()  # 读取数组元素
arr = [int(i) for i in arr]  # 将数组元素转换为整数
arr.sort()  # 对数组进行排序

lowest = None  # 初始化用于存储最小元素的变量
res = []  # 初始化结果数组
if n % 2 != 0:
    # 如果元素个数是奇数
    lowest = arr.pop(0)  # 移除并保存数组中的最小元素

mid = n // 2  # 计算中间索引

# 将数组分为两部分：较小的值和较大的值
# 较小的值从索引0到mid-1，较大的值从索引mid到末尾
lower = mid - 1
while lower >= 0:
    res.append(arr[lower])  # 添加较小的值
    res.append(arr[mid])  # 添加较大的值
    lower -= 1  # 移动到下一个较小的值
    mid += 1  # 移动到下一个较大的值

# 如果存在最小的元素（即元素个数是奇数），则将其添加到结果数组的末尾
if lowest:
    res.append(lowest)
print(*res, sep=" ")  # 输出结果数组
