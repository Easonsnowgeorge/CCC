m = int(input())
n = int(input())
ans = 0
for i in range(1,m+1):
    for j in range(1,n+1):
        if i + j == 10:
            ans += 1

if ans == 1:
    print("There is 1 way to get the sum 10.")
else:
    print("There are", ans, "ways to get the sum 10.")