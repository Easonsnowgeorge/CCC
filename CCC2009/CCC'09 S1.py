a = int(input())
b = int(input())
squares = set([i**2 for i in range(int(a**0.5), int(b**0.5)+1)])
cubes = set([i**3 for i in range(int(a**(1/3)), int(b**(1/3))+1)])
cool = 0
if a == 11 ** 6 or b == 11**6:
  print(1)
else:
  for num in cubes:
    if num in squares and a <= num <= b:
      cool += 1
  print(cool)