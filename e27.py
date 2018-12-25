def is_prime(n) : 
  
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

def p(n, a, b):
    return (n*n) + a*n + b

primes = []
b_range = []


for i in range(100000):
    if(is_prime(i)):
        primes.append(i)
        
        
for pr in primes:
    if pr <= 1000:
        b_range.append(pr)

print(b_range)

m, mm, am, bm = 0, 0, 0, 0

for b in b_range:
    for a in range(-999, 1000, 2):
        n, m = 0, 0
        while(True):
            """
            if a < (1 - b):
                if m > mm:
                    mm = m
                break
            """
            if p(n, a, m) >= 0 and is_prime(p(n, a, m)):
                m += 1
                n += 1
            else:
                if m > mm:
                    mm = m
                    am, bm = a, b
                break

print(a, b, mm)          
