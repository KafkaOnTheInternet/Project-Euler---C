f = open('e8.txt')

def get_prod(index):
    prod = 1
    for i in range(index+1, index + 13):
        prod *= li[i]
    return prod

li = []


for line in f.readlines():
    for l in line.strip('\n'):
        li.append(int(l))

m = 0
n = 999
    
for i in range(999 - 13):
    if (li[i] * get_prod(i)) > m:
        m = li[i] * get_prod(i)
        print(m)

print(m)
