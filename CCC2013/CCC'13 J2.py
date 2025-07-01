list = ["I", "O", "S", "H","Z","X","N"]
word = input()
for i in range(len(word)):
    if word[i] not in list:
        print("NO")
        break
    if i == len(word)-1:
        print("YES")