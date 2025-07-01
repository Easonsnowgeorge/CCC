repeats = int(input())  # 读取操作次数
stack = []  # 初始化栈

# 根据用户输入的操作次数进行循环
for i in range(repeats):
    value = int(input())  # 读取用户输入的整数
    if value == 0:
        stack.pop()  # 如果值为0，则弹出栈顶元素
    else:
        stack.append(value)  # 否则，将值压入栈中

total = 0  # 初始化用于计算总和的变量
for j in stack:
    total += j  # 计算栈中所有元素的总和

print(total)  # 输出总和
