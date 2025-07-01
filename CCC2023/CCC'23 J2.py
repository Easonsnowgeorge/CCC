# 定义一个字典，包含不同辣椒的名称及其对应的数值
peppers = {'Poblano': 1500,
           'Mirasol': 6000,
           'Serrano': 15500,
           'Cayenne': 40000,
           'Thai': 75000,
           'Habanero': 125000}

# 读取用户要输入的辣椒名称的次数
repeats = int(input())

# 初始化计数为0
count = 0

# 根据用户输入的次数进行循环
for i in range(repeats):
    # 读取用户输入的辣椒名称
    add = input()
    # 将对应辣椒名称的数值加到计数上
    count += peppers[add]

# 打印最终的总数
print(count)
