numbers = [1,2,3,4,5,6,7,8,9]

squares = [n * n for n in numbers]
print('Squares: {}'.format(','.join(str(n) for n in squares)))

under_twenty = [n for n in squares if n < 20]
print('< 20: ', under_twenty)

nested_for = [(x,y,z) for x in (0,1,2,3) for y in (0,1,2,3) for z in (0,1,2,3) if x < 2]
# [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 1, 3), (0, 2, 0), (0, 2, 1), (0, 2, 2), (0, 2, 3), (0, 3, 0), (0, 3, 1), (0, 3, 2), (0, 3, 3), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 0, 3), (1, 1, 0),
# (1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 0), (1, 2, 1), (1, 2, 2), (1, 2, 3), (1, 3, 0), (1, 3, 1), (1, 3, 2), (1, 3, 3)]
print(nested_for)