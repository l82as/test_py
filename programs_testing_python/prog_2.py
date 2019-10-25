import math as m
a, b = map(int, input().split())
x = int(round((a + m.sqrt(a**2-4*b))/2, 10))
y = a - x
print(min(x, y), end = " ")
print(max(x, y))