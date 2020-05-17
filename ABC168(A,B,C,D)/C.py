from math import radians, cos
a, b, h, m = map(int, input().split())
s = 30 * h + (1 / 2) * m
l = 6 * m
theta = radians(abs(s - l))
ans = (a ** 2 + b ** 2 - (2 * a * b * cos(theta))) ** (1 / 2)
print(ans)