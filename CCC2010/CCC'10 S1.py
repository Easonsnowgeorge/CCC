a = 0
b = 0
c = ""
d = ""
n = int(input())
for i in range(n):
    name, x, y, z = input().strip().split()
    score = 2 * int(x) + 3 * int(y) + int(z)
    if (score > a or (score == a and name < c)):
        b = a
        d = c
        a = score
        c = name
    elif (score > b or (score == b and name < d)):
        b = score
        d = name
print(c)
print(d)