n = int(input())

for i in range(n):
    s = input()
    up = []
    number = []
    temp = ""
    for i in s:
        if i.isdigit()==0 and temp!="":
            number.append(int(temp))
            temp = ""
        if i.isupper():
            up.append(i)
        elif i.isdigit():
            temp+=i
        elif i == "-":
            temp += i
    if temp!="":
        number.append(int(temp))
    num = sum(number)


    ans = ""
    for i in up:
        ans += i
    ans += str(num)
    print(ans)