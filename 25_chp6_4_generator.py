#25/123

L = [x*x for x in range(10)]

print(L)

g = (x*x for x in range(10))


for n in g:
    print(n)

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b, a+b
        n = n+1
    return 'done'

print(fib(6))    

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 5

o = odd()

print(next(o))
print(next(o))
print(next(o))

for n in fib(6):
    print(n)

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('return value:',e.value)
        
        break

        
r = abs(6)

print(r)

g = fib(6)

def triangles():
    L=[1]
    while True:
        yield L
        i = len(L)-1
        while(i):
            L[i] = L[i]+L[i-1]
            i = i-1
        L.append(1)
        
    
n = 0
for t in triangles():
    print(t)
    n = n+1
    if n == 10:
        break






