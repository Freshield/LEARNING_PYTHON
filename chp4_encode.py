#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('包含中文的str')

print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

print('\u4e2d\u6587')

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
#print('中文'.encode('ascii'))

print(b'ABC'.decode('ascii'))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(len('ABC'),len('中文'))

print(len(b'ABC'),len(b'\xe4\xb8\xad\xe6\x96\x87'),len('中文'.encode('utf-8')))

print('Hello, %s' % 'world')

print('Hi, %s, you have $%d.' % ('Michael',100000))

print('%2d-%02d' % (3,1),'%.2f' % 3.1415926)

print('Age: %s. Gender: %s' % (25,True))

print('growth rate: %d %%' % 7)

print('growth rate: %.1f %%' % ((s2-s1)*100/s1))








