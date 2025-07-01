daytime =int(input())
evening = int(input())
weekend = int(input())
planA = 0
planB = 0
if daytime > 100:
    planA += (daytime-100)*25
planA += evening*15
planA += weekend*20
if daytime > 250:
    planB += (daytime-250)*45
planB += evening*35
planB += weekend*25
print("Plan A costs",f'{planA/100:.2f}')
print("Plan B costs",f'{planB/100:.2f}')
if planA < planB:
    print("Plan A is cheapest.")
elif planA > planB:
    print("Plan B is cheapest.")
else:
    print("Plan A and B are the same price.")
