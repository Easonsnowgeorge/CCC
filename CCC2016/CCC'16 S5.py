n, times = map(int, input().split())  # 读取数组长度和时间步数
row = list(map(int, list(input())))  # 读取初始数组状态

def log2(n):
    result = 0
    while n > 1:
        n //= 2
        result += 1
    return result  # 返回 n 的以2为底的对数

while times > 0:
    new_state = []
    p2 = 2 ** log2(times)  # 计算不超过 times 的最大的2的幂次数

    for i in range(n):
        left = (i - p2) % n  # 计算左侧元素的位置，使用模运算处理循环
        right = (i + p2) % n  # 计算右侧元素的位置
        cell = row[left] ^ row[right]  # 新状态是左右两侧元素的 XOR
        new_state.append(cell)

    row = new_state.copy()
    times -= p2  # 更新剩余的时间步数

print(*row, sep="")  # 输出最终的数组状态
