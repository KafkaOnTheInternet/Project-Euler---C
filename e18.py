import numpy as np

g = np.zeros((15, 15), dtype = int)

f = open('e18.txt')

lines = f.readlines()
li = []

for l in lines:
    li.append(list(map(int, l.split())))
    
for l in li:
    print(l)


"""
x, y = 14, 14

for line, cnt in zip(li, range(15)):
    for l in range(len(line)):
        g[cnt, l] = line[l]
        
while(x >= 1):
    for i in range(y):
        g[x-1][i] += max(g[x][i], g[x][i+1])
    x -= 1

#print(g)
"""       

t = 13

while(t >= 0):
    for i in range(len(li[t])):
        li[t][i] += max(li[t+1][i], li[t+1][i+1])
    t -= 1

for l in li:
    print(l)