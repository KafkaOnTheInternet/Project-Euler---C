from itertools import permutations

li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

perm = permutations(li)

t = 1000000

print(str(list(perm)[t-1]))