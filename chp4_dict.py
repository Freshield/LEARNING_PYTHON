d = {'michael':95,'bob':75,'tracy':85}
print(d['michael'])

d['adam'] = 67
print(d['adam'])

d['adam'] = 99
print(d['adam'])

print('thomas' in d)

print(d.get('thomas'))
print(d.get('thomas',233))

print(d)

print(d.pop('bob'))
print(d)

key = (1,2,3)

d[key] = 'a list'

print(d)

key = ()

print(d)

print(d[(1,2,3)])

s = set([1,2,3])

print(s)

s = set([1,1,2,2,3,3])
print(s)

s.add(4)
print(s)

s.add(4)
print(s)

s.remove(4)
print(s)

s1 = set([1,2,3])
s2 = set([2,3,4])

print(s1 & s2)
print(s1 | s2)

a = ['c','b','a']
a.sort()
print(a)

a = 'abc'
b = a.replace('a','A')
print(a)
print(b)

s = set([1,2,3])
a=s
a.add(4)
print(a) #输出结果1,2,3,4
print(s)
b=s
b.add(5)
print(a)
print(b) #输出结果1,2,3,4,5
print(s)
u = a & b
print(u) #输出结果1,2,3,4,5
u = a|b
print(u) #输出结果1,2,3,4,5




































