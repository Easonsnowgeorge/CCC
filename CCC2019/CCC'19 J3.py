# 读取要处理的字符串数量
repeats = int(input())

# 初始化一个列表来存储压缩后的字符串
to_print = []

# 初始化用于记录当前字符和计数的变量
letter = ""
count = 0

# 初始化计数器
current = 0
while current < repeats:
    # 读取字符串并在末尾添加一个不会出现的字符（作为结束标志）
    text = str(input()) + "~"
    letter = text[0]

    # 遍历字符串中的每个字符
    for i in text:
        prev_letter = letter
        if letter == i:
            count += 1
        elif letter != i:
            # 如果字符发生变化，将前一个字符和其计数添加到列表中
            to_print.append(f"{count} {prev_letter} ")
            letter = i
            count = 1

    # 添加换行符，表示一个字符串的结束
    to_print.append("\n")
    # 更新计数器
    current += 1
    # 重置字符和计数变量
    letter = ""
    count = 0

# 打印所有压缩后的字符串
for j in to_print:
    print(j, end="")
