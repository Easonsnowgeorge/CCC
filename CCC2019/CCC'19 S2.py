t = int(input())  # 读取测试用例的数量

def is_prime(num):
    if num < 2:  # 排除小于2的数
        return False
    for i in range(2, int(num ** 0.5 + 1)):  # 遍历从2到sqrt(num)的数
        if num % i == 0:  # 如果能被整除，则不是质数
            return False
    return True  # 如果没有被整除，则是质数

for i in range(t):
    num = int(input())  # 读取每个测试用例的数值
    start = num - 1  # 初始化较小的数
    end = num + 1  # 初始化较大的数

    # 找到一对质数，使得一个小于num，另一个大于num
    while is_prime(end) == False or is_prime(start) == False:
        start -= 1  # 减小较小的数
        end += 1  # 增加较大的数

    print(f"{start} {end}")  # 输出找到的一对质数
