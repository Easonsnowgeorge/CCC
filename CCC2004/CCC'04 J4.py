cypher = input()
m = input().replace(" ", "")
n = ""
for char in m:
    if char.isalpha():
        n += char
alp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
asc = [65, 66,    67,  68,  69,  70,   71, 72,  73,  74,  75,  76,  77,  78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90]
a = len(cypher)
b = len(n)
# c = int(b/a)
# d = b % a
for i in range(b):
    e = i % a
    shiftval = int(ord(cypher[e]))
    shift = asc.index(shiftval)
    letter = ord(n[i])
    ans = int(shift + letter)
    ans = ans % 91
    if ans < 65:
        ans += 65
    print(chr(ans), end = '')