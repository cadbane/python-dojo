numbers = [1,2,3,4,5,6,7,8,9]

squares = [n * n for n in numbers]
print('Squares: {}'.format(','.join(str(n) for n in squares)))

under_twenty = [n for n in squares if n < 20]
print('< 20: ', under_twenty)