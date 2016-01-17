#30/123

def is_odd(n):
    return n%2 == 1

print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10])))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['a','','b',None,'c',''])))

def _odd_iter():
    n = 1
    while True:
        n = n+ 1
        yield n

def _not_divisible(n):
    return  lambda x:x % n >0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)


for e in primes():
        if e < 100:
            print(e)
        else:
            break    


def is_palindrome(n):
    return str(n)==str(n)[::-1]

output=filter(is_palindrome,range(1,1000))
print(list(output))












