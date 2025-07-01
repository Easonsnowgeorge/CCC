# 读取要处理的字符串数量
repeats = int(input())

# 初始化一个列表来存储解压缩后的字符串
to_print = []

# 初始化计数器
i = 0
while i < repeats:
    # 读取并分割每个输入字符串
    decompress = input()
    decompress = decompress.split()

    # 将字符重复指定的次数，并添加到列表中
    to_print.append(int(decompress[0]) * decompress[1])

    # 更新计数器
    i += 1

# 打印所有解压缩后的字符串
for j in to_print:
    print(j)
