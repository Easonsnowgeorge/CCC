n = int(input())
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(n):
    lw = []
    for i in range(4):
        word = input().split(" ")[-1]
        word = word.lower()
        word = list(word)
        word.reverse()
        a = []
        for i in word:
            a.append(i)
            if i in vowels:
                break
        lw.append(''.join(a))
    a,b,c,d = lw
    if a == b == c == d:
        print("perfect")
    elif a == b and c == d:
        print("even")
    elif a == c and b == d:
        print("cross")
    elif a == d and b == c:
        print("shell")
    else:
        print("free")