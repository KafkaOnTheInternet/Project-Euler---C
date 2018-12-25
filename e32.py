T = [1, 2, 3, 4, 5, 6, 7, 8, 9]

P = []


for a in range(2000):
    for b in range(2000):
        li = [int(x) for x in str(a) + str(b) + str(a*b)]
        if sorted(li) == T and a*b not in P:
            P.append(a*b)

print(sum(P))
