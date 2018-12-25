f = open('e67.txt')

lines = f.readlines()
li = []

for l in lines:
    li.append(list(map(int, l.split())))
      

t = 98

while(t >= 0):
    for i in range(len(li[t])):
        li[t][i] += max(li[t+1][i], li[t+1][i+1])
    t -= 1

print(li[0])