amount = int(input())

first = input()
second = input()
index = 0
count = 0

for _ in range(amount):
    if first[index] == second[index] == "C":
        count += 1

    index += 1
    amount += 1

print(count)