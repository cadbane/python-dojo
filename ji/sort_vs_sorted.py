# list.sort()
# mutates the list in-place & returns None

a = [6,4,7,8,3,1]
print(a)
print(a.sort())
print(a)

# list.sort(0 is faster than sorted() because it doesn't have to create a copy

# sorted() return a new sorted list, leaving the original list unaffected
b = [6,7,3,1,3,5]
print(b)
print(sorted(b))
print(b)

# sorted() works on any iterable, not just lists

# strings
c = 'ala ma kota'
print(c)
print(sorted(c))

# tuples
d = (8,6,4,1,2,0)
print(d)
print(sorted(d))

# dicts
e = {'c': 3, 'a': 1, 'b': 2, 'd': 4}
print(e)
print(sorted(e))