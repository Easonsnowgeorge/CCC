j = int(input())  # 读取运动服的数量
athletes = int(input())  # 读取运动员的数量

jerseys = {}  # 初始化用于存储运动服的字典

# 读取每件运动服的大小，并存入字典
for i in range(1, j+1):
    jerseys[i] = input()

count = 0  # 初始化计数器，用于计算成功匹配的运动员数量
for i in range(athletes):
    size, num = input().split()  # 读取运动员的理想运动服大小和编号
    num = int(num)
    # 检查运动服是否符合运动员的大小要求
    if jerseys[num] < size or jerseys[num] == size:
        count += 1  # 如果符合要求，增加计数器
        jerseys[num] = "a"  # 将运动服大小设置为比S、M、L都小的值，以避免重复分配

print(count)  # 输出成功匹配的运动员数量
