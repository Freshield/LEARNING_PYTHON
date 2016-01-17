#29/123

def f(x):
    return x*x

r = map(f,[1,2,3,4,5,6,7,8,9])

print(list(r))

for x in r:
    print(x)

L = []

for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
print(L)    

print(list(map(str,[1,2,3,4,5,6,7,8,9])))

def add(x,y):
    return x + y

from functools import reduce

print(reduce(add,[1,3,5,7,9]))

def fn(x,y):
    return x*10 + y

print(reduce(fn,[1,3,5,7,9]))


def char2num(s):
    return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

print(reduce(fn,map(char2num,'13579')))

def str2int(s):
    def fn(x,y):
        return x*10 + y
    def char2num(s):
        return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(fn,map(char2num,s))

print(str2int('13579'))

def char2num(s):
        return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

def str2int(s):
    return reduce(lambda x,y:x*10 +y,map(char2num,s))


print(str2int('13579'))

def normalize(name):
    return name[0].upper() + name[1:].lower()

L1 = ['adam','LISa','barT']
L2 = list(map(normalize,L1))

print(L2)

def prod(L):
    def mul(x,y):
        return x * y
    return reduce(mul,L)

print('3*5*7*9=',prod([3,5,7,9]))

def str2float(s):
    def char2num(s):
        return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    def fn(x,y):
        return x*10 + y
    s1,s2 = s.split('.')
    return(reduce(fn,map(char2num,s1))+reduce(fn,map(char2num,s2))*pow(10,-len(s2)))

print('str2float(\'123.456\')=',str2float('123.456'))



