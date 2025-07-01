a = int(input())
b = int(input())
l = [a, b]
ans = 0
while True:
    a = l[-2] - l[-1]
    l.append(a)
    if l[-2] < l[-1]:
        print(ans+3)
        break
    ans += 1