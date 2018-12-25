import numpy as np

def get_prod(index):
    prod = 1
    for i in range(index, index + 4):
        prod *= 

grid = np.zeros((20, 20), dtype = int)

f = open('e11.txt')

i, j = 0, 0


for line in f.readlines():
    li = [int(x) for x in list(map(int, line.strip('\n').split()))]
    j = 0
    for l in li:
        grid[i, j] = l
        j += 1
    i += 1

m = 0

for u in range(20):
    prod = 1
    for v in range(20):
        
        