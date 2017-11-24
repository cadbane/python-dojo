# iterating over list index and value pairs
a = ['Lorem', 'ipsum', 'dorem', 'kolorem']
for i, x in enumerate(a):
    print(f'{i}: {x}')

# iterating over dictionary
b = {'apple': 3, 'banana': 7, 'orange': 0}
for f, q in b.items(): # iteritems() for python2
    print(f'{f}: {q}')