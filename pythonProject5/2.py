import math

x = 1.825
y = 18.225
x1 = x ** (y / x)

cube_root = y/x ** (1./3.)

b = x1 - cube_root

d= abs(b)
print(d)
