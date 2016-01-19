#34/123

def now():
    print('2015-3-25')

f = now
print(f())

print(now.__name__)

print(f.__name__)

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

print(now())

print(now.__name__)

def log(*text, **kw):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s(): ' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('executre')
def now():
    print('2015-3-25')

now()

print(now.__name__)

def log(item):
    if callable(item):
        func = item
        def wrapper(*args, **kw):
            print("begin call\n %s(): " % (func.__name__))
            r = func(*args, **kw)
            print('end call')
            return r
        return wrapper
        
    else:
        text = item
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print("begin call\n%s %s(): " % (text, func.__name__))
                r = func(*args, **kw)
                print('end call')
                return r
            return wrapper
        return decorator
        
        
    

@log
def now():
    print('2016-1-19')

now()



























        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        