import math

def check_abundant(n):
    li = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            if (n/i == i):
                li.append(i)
            else:
                li.append(int(n/i))
    return sum(li) > n

n = 28123
s = 0
abundant = []
can_write = [False]*(n+1)

for i in range(12, (n+1)):
    if check_abundant(i):
        abundant.append(i)

for x in range(len(abundant)):
    for y in range(len(abundant)):
        if abundant[x] + abundant[y] <= n:
            can_write[abundant[x] + abundant[y]] = True
        else:
            break

for i in range(len(can_write) + 1):
    if can_write[i] == False:
        s += i

print(s)