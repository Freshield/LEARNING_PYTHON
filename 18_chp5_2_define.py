#18/123

def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-20))

def nop():
    pass
    
print(nop())

#my_abs('a')

import math

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

x,y = move(100, 100, 60, math.pi / 6)

print(x, y)

r = move(100, 100, 60, math.pi / 6)

print(r)

def quadratic(a, b, c):
#can add the detect if there have solution first
    ans1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    ans2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return ans1,ans2

print(quadratic(2,3,1))
print(quadratic(1,3,-4))













