a = int(input())
b = int(input())
for i in range(1, b + 1):
    A = -6 * i ** 4 + a * i ** 3 + 2 * i ** 2 + i
    if A <= 0:
        print("The balloon first touches ground at hour:")
        print(i)
        break
    if i == b:
        print("The balloon does not touch ground in the given time.")
