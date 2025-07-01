text = input()  # 读取输入的文本

alphabet = "abcdefghijklmnopqrstuvwxyzzz"  # 定义一个包含所有字母的字符串，最后三个 'z' 是为了避免越界
vowels = "aeiou"  # 定义元音字母
index = 0  # 初始化索引变量
to_print = []  # 初始化输出列表

for i in text:
    if i in vowels:
        to_print.append(i)  # 如果是元音字母，直接添加
    else:
        index = alphabet.find(i)
        to_print.append(alphabet[index])  # 添加辅音字母

        # 根据辅音字母的位置，添加一个特定的元音字母
        if i in alphabet[1:3]:
            to_print.append("a")
        elif i in alphabet[3:7]:
            to_print.append("e")
        elif i in alphabet[7:12]:
            to_print.append("i")
        elif i in alphabet[12:18]:
            to_print.append("o")
        else:
            to_print.append("u")

        # 添加辅音字母之后的一个辅音字母（或下一个非元音字母）
        if alphabet[index + 1] in vowels:
            to_print.append(alphabet[index + 2])
        else:
            to_print.append(alphabet[index + 1])

# 输出转换后的字符串
for j in to_print:
    print(j, end="")
