a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())
e = a-b
f = c-d
x = int(s % (a+b))
g = int(s/(a+b))
h = int(g * e + x)
y = int(s % (c+d))
z = (s/(c+d))
zz = int(z * f + y)
if h > zz:
    print("Nikky")
if zz > h:
    print("Byron")
if zz == h:
    print("Tied")
