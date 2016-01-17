#31/123

print(sorted([36,5,-12,9,-21]))

print(sorted([36,5,-12,9,-21], key=abs))

print(sorted(['bob','about','Zoo','Credit']))

print(sorted(['bob','about','Zoo','Credit'],key=str.lower))

print(sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True))


L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

def by_name(t):
    a = t[0]
    return a

def by_score(t):
    return t[1]

print(sorted(L,key=by_name))
print(sorted(L,key=by_score,reverse=True))
















