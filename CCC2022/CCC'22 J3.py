# 读取用户输入的字符串
x = str(input())

# 定义字母和数字的字符集
letters = "ABCDEFGHIJKLMNOPQRST"
numbers = "0123456789"

# 初始化标志，用于标记当前字符是否为数字
is_number = False

# 遍历输入字符串的每个字符
for i in x:
    # 如果字符是数字
    if i in numbers:
        is_number = True
        print(i, end="")  # 打印数字，并不换行

    # 如果字符不是数字
    elif i not in numbers:
        # 如果前一个字符是数字，则换行
        if is_number:
            print()
            is_number = False

        # 如果字符是"+"，打印" tighten "
        if i == "+":
            print(" tighten ", end="")
            is_number = False

        # 如果字符是"-"，打印" loosen "
        elif i == "-":
            print(" loosen ", end="")
            is_number = False

        # 如果字符是字母，直接打印
        elif i in letters:
            print(i, end="")
            is_number = False
