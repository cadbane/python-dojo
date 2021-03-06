a, b, c = 1, 2, 3
# a,b == (1,2)

a, b, c = [1, 2, 3]
# a,c == (1,3)

a,c == (1,3)
# (1, False)

a, b, c = (7 * j for j in range(3))
# (0, 7, 14)

a, b = 1, 2
a, b = b, a
# a == 2, b == 1

a, *b, c = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
# a == 1, c == 1
# b == [2,3,4,5,6,7,8,9,8,7,6,5,4,3,2]