def find_largest_factor(num):
    """Find the largest factor of num that != num"""
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return num // i
    return 1  # couldn't find any, just subtract 1 from the number


n = int(input())
cost = 0

while n != 1:
    a = find_largest_factor(n)
    b = n // a  # n = a * b
    cost += b - 1  # have to minus one for some reason (again, not sure why)
    n -= a

print(cost)