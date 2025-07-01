ca = 0
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 1:
   ca += 461
if a == 2:
   ca += 431
if a == 3:
   ca+=420
if a == 4:
   ca += 0
if b == 1:
   ca+= 100
if b == 2:
   ca+=57
if b == 3:
   ca+=70
if b == 4:
   ca+=0
if c == 1:
   ca+=130
if c == 2:
   ca+=160
if c == 3:
   ca+=118
if c == 4:
   ca+=0
if d == 1:
   ca+=167
if d == 2:
   ca+=266
if d == 3:
   ca+=75
if d == 4:
   ca+=0
print("Your total Calorie count is %s." %(ca))