li = []

for a in range(1, 100):
    for b in range(1, 100):
        li.append(a ** b)

o = []

for l in li:
    o.append(sum([int(x) for x in str(l)]))

print(max(o))


