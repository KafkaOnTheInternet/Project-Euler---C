from math import factorial:

def ncr(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))

print(len([ncr(n, r) for n in range(1, 101) for r in range(n+1) if ncr(n, r) >= 10 ** 6]))
