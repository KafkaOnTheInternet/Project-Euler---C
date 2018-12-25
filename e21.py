from math import sqrt
from collections import Counter

def d(n):
    li = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            li.append(i)
            li.append(n // i)
    return sum(li) - n

found = []
amicable = []

"""
for i in range(0, 10000, 2):
    j = d(i)
    if j > 10000:
        continue
    if i not in found and j not in found:
        found.append(i)
        found.append(j)
    elif i in found and j in found:
        amicable.append(i)
        amicable.append(j)
    i += 1        
"""

"""
for i in range(10000):
    j = d(i)
    if j > 10000:
        continue
    found.append(i)
    if j in found:
        amicable.append(i)
        amicable.append(j)
"""

divisors = [d(x) for x in range(10000)]

"""
for i in range(10001):
    j = d(i)
    if i in amicable:
        continue
    if d(j) in amicable:
        if j > 10000 and i < 10000:    
            amicable.append(i)
        else:
            amicable.append(i)
            amicable.append(j)
d = Counter(amicable)
"""
for i in range(10000):
    


d = Counter(amicable)
print(sum(d.keys()))