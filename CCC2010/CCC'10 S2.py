n = int(input())
d = {}
for i in range(n):
    a = input().split(" ")
    d[a[1]] = a[0]
s = input()
ans = ''
i = 0
while s != "":
    try:
        if d[s[0:i]] == d[s[0:i]]:
            ans += (d[s[0:i]])
            s = s[i:]
            i = 0
    except:
        i += 1
        continue
print(ans)