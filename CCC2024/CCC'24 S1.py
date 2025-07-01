n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
inc = n//2
ans = 0
for i in range(n//2):
    if l[i] == l[i+inc]:
        ans += 2
print(ans)