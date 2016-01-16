#24/123

print(list(range(1,11)))

L = []

for x in range(1,11):
    L.append(x * x)
    
print(L)

print([x * x for x in range(1,11)])

print([x * x for x in range(1,11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])

import os

print([d for d in os.listdir('.')])

d = {'x': 'A','y':'B','z':'C'}

for k,v in d.items():
    print(k,'=',v)

print([k + '=' + v for k,v in d.items()])

L = ['Hello','World','IBM','Apple']

print([s.lower() for s in L])

x = 'abc'

y = 123

print(isinstance(x,str))

print(isinstance(y,str))

L = ['Hello','World',18,'IBM','Apple',None]

print([s.lower() for s in L if isinstance(s,str)==True])




















