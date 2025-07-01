d = int(input())
e = int(input())
for i in range(e):
    symbol = input()
    q = int(input())
    if symbol =="+":
        d += q
    elif symbol == "-":
        d -= q

print(d)