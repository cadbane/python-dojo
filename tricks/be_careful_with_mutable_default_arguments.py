def foo(x=[]):
    x.append(1)
    print(x)

print('foo(): ')
foo()
# [1]
foo()
# [1,1]
foo()
# [1,1,1]

def bar(x=None):
    x = x or []
    x.append(1)
    print(x)

print('bar():')
bar()
# [1]
bar()
# [1]
bar()
# [1]