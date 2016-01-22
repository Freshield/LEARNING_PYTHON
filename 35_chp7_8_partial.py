#35/123

print(int("12345"))

print(int('12345',16))

def int2(x, base=2):
    return int(x,base)

print(int2('100000'))

import functools

int2 = functools.partial(int, base=2)

print(int2('10101010'))

print(int2('100000',base=10))

kw = {'base':10}

print(int2('131234',**kw))

max2 = functools.partial(max,10)

print(max2(5,6,7))


