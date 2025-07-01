from numpy.ma.core import remainder

s = input()
n = int(input())

letter = []
number = []

temp = ""
for i in range(len(s)):

    if s[i].isalpha():
        if temp != "":
            number.append(int(temp))
            temp =""
        letter.append(s[i])
    elif s[i].isdigit():
        temp += s[i]
number.append(int(temp))

# print(letter)
# print(number)

sum_number = sum(number)
remainder = n % sum_number

for i in range(len(letter)):
    if sum(number[:i+1]) >= remainder:
        print(letter[i])
        break