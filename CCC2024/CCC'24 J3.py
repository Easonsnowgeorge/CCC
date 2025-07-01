n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l.sort(reverse=True)
a = 1
ans = 0
for i in range(1, n):
    if l[i-1] != l[i]:
        a += 1
    if a == 3:
        for j in range(i, n):
            if l[j] == l[i]:
                ans += 1
            if l[j] != l[i]:
                break
        print(l[i], ans)
        break