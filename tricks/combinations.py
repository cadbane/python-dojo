from itertools import combinations

players = ['A','B','C','D','E']

for game in combinations(players, 2):
    print(game)