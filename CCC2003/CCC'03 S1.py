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


#ccc waterloo 2003 s1 question:)
#(Snakes And Ladder But Codes :) )
End = False
i = -1
Position = 1
Up_Enter = [9,40,67]
Up_Exit = [34,64,86]
Down_Enter = [54,90,99]
Down_Exit = [19,48,77]
while End != True:
    i += 1
    moves = int(input())
    if moves == 0:
        print("You Quit!")
        break
    Position += moves
    if Position > 100 or Position < 0:
        Position -= moves
    if Position in Up_Enter:
        Position = Up_Exit[Up_Enter.index(Position)]
    if Position in Down_Enter:
        Position = Down_Exit[Down_Enter.index(Position)]
    if Position == 100:
        print("You are now on square", Position)
        print("You Win!")
        break
    print("You are now on square", Position)