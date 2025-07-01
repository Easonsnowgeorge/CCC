for _ in range(int(input())):  # 读取测试用例的数量
    max_num = int(input())  # 读取每个测试用例中的整数数量
    current = 1  # 初始化当前需要弹出的下一个数字
    arr = []  # 初始化输入序列的列表
    stack = []  # 初始化栈

    # 读取每个测试用例中的整数
    for _ in range(max_num):
        arr.append(int(input()))

    # 尝试通过栈操作重排序列
    for _ in range(max_num):
        car = arr.pop()  # 弹出序列中的最后一个整数
        if car == current:  # 如果当前整数是需要弹出的下一个数字
            current += 1
            while stack and stack[-1] == current:  # 如果栈顶元素是需要弹出的下一个数字
                stack.pop()  # 弹出栈顶元素
                current += 1
        else:
            stack.append(car)  # 将当前整数推入栈中

    # 检查是否成功重排为升序
    if not stack:
        print("Y")  # 如果栈为空，则重排成功
    else:
        print("N")  # 如果栈不为空，则重排失败
