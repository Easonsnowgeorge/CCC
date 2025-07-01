n = int(input())
for i in range(n):
    number = list(map(str, input().split("-")))
    s = "".join(number)[:10]
    ans = ""
    for j in s:
        try:
            a = int(j)
            ans += j
        except:
            if j == "A" or j == "B" or j == "C":
                ans += "2"
            if j == "D" or j == "E" or j == "F":
                ans += "3"
            if j == "G" or j == "H" or j == "I":
                ans += "4"
            if j == "J" or j == "K" or j == "L":
                ans += "5"
            if j == "M" or j == "N" or j == "O":
                ans += "6"
            if j == "P" or j == "Q" or j == "R" or j == "S":
                ans += "7"
            if j == "T" or j == "U" or j == "V":
                ans += "8"
            if j == "W" or j == "X" or j == "Y" or j == "Z":
                ans += "9"
    print("%s-%s-%s" % (ans[:3], ans[3:6], ans[6:]))
