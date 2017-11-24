f = ['apple', 'banana', 'orange']
q = [7, 0, 12]

fruits = zip(f,q)
print('list(fruits): {}'.format(list(fruits)))
# [('apple', 7), ('banana', 0), ('orange', 12)]

# zip() in conjunction with the * operator can be used to unzip a list:
a, b = zip(*zip(f,q))
# a: ('apple', 'banana', 'orange')
# b: (7, 0, 12)

print('a == f: {}'.format(f == list(a))) # True
print('b == q: {}'.format(q == list(b))) # True


p = ['a','b','c','d','e']
o = [1,2,3]

z1 = zip(p,o)
print('zip(p,o): {}'.format(list(z1)))
# zip(p,o): [('a', 1), ('b', 2), ('c', 3)]

z2 = zip(o,p)
print('zip(o,p): {}'.format(list(z2)))
# zip(o,p): [(1, 'a'), (2, 'b'), (3, 'c')]