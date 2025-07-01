# 读取翻转操作的字符串
flip = input()

# 初始化2x2方阵
square = [1, 2, 3, 4]

# 遍历翻转操作字符串中的每个字符
for i in flip:
    if i == "H":
        # 水平翻转：上下行交换位置
        square[0], square[1], square[2], square[3] = square[2], square[3], square[0], square[1]
    else:
        # 垂直翻转：左右列交换位置
        square[0], square[1], square[2], square[3] = square[1], square[0], square[3], square[2]

# 打印最终的方阵
print(square[0], square[1])
print(square[2], square[3])
