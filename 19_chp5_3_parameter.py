#19/123

def power(x):
    return x * x

print(power(5))

print(power(25))

def power(x=1, n=2):
    s = 1
    while n>0:
        n = n - 1
        s = s * x
    return s

print(power(5, 3))

print(power(5))

print(power(5, 2))

print(power(5, 1))


def enroll(name, gender):
    print('name',name)
    print('gender',gender)
  
enroll('sarah','F')

def enroll(name, gender, age=6, city='beijing'):
    print('name',name,'\ngender',gender,'\nage',age,'\ncity',city)
    
enroll('sarah','f')

enroll('bob','m', city='montreal')

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end([1,2,3]))

print(add_end(['x','y','z']))

print(add_end())
print(add_end())
print(add_end())

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3))
print(calc(1,3,5,7))
print(calc())

nums = [1,2,3]

print(calc(nums[0],nums[1],nums[2]))

print(calc(*nums))

print(nums)
print(*nums)

def person(name, age, **kw):
    print('name',name,'age',age,'other',kw)
    
person('michael',30)

person('bob',35,city='beijing')

person('adam',45,gender='m',job='engineering')

extra = {'city':'beijing','job':'engineering'}

person('jack',24,**extra)

def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name',name,'age',age,'other',kw)
    
person('jack',24,city='beijing',addr='chaoyang',zipcode=123456)

def person(name,age,*,city,job):
    print(name,age,city,job)


person('jack',24,job='engineering',city='beijing')


def person(name,age,*,city='beijing',job):
    print(name,age,city,job)

person('jack',24,job='engineering')


def f1(a,b,c=0,*args,**kw):
    print('a',a,'b',b,'c',c,'args',args,'kw',kw)
    
def f2(a,b,c=0,*,d,**kw):
    print('a',a,'b',b,'c',c,'d',d,'kw',kw)

f1(1,2)
f1(1,2,c=3)
f1(1,2,x=99)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)

f2(1,2,d=99,ext=None)

args = (1,2,3,4)
kw = {'d':99,'x':'#'}

f1(*args,**kw)

args = (1,2,3)
kw = {'d':88,'x':'#'}

f2(*args,**kw)





















