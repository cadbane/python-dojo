L = list(range(20))

print(L[:3])
# [0, 1, 2]

print(L[::2])
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

print(L[::4])
# [0, 4, 8, 12, 16]

print(L[::-1])
# [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(L[1:10:2])
# [1, 3, 5, 7, 9]

print(L[10:1:-1])
# [10, 9, 8, 7, 6, 5, 4, 3, 2]

L[3:7] = [5, 4, 3, 2]
print(L)
# [0, 1, 2, 5, 4, 3, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]