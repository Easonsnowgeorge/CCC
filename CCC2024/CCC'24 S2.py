n, m = map(int, input().split())
l = []
for i in range(n):
    l = []
    s = input()
    f = 0
    for j in range(m):
        if s.count(s[j]) > 1:
            l.append(1)
        else:
            l.append(2)
    for j in range(m-1):
        if l[j] == l[j+1]:
            print("F")
            f = 1
            break
    if f == 0:
        print("T")