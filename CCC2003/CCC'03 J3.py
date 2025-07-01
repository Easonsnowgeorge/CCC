a = 1
while a < 100:
    moves = int(input())
    if moves == 0:
        print("You Quit!")
        break
    a += moves
    if a == 9:
        a = 34
    if a == 40:
        a = 64
    if a == 67:
        a = 86
    if a == 54:
        a = 19
    if a == 90:
        a = 48
    if a == 99:
        a = 77
    if a > 100:
        a = a - moves
    print("You are now on square %s" %(a))
if a == 100:
    print("You Win!")