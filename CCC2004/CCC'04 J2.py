a = int(input())
b = int(input())
print("All positions change in year %s"%(a))
for i in range(1, 1000):
    if b >= a + i * 60:
        print("All positions change in year %s"%(a + i * 60))
    if b < a + i * 60:
        break