from collections import Counter

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5

    while i * i <= n:
        if n % i == 0:
            return False
        i += 6
    
    return True

    
cnt, n = 0, 0

for i in range(2, 10**4):
    if cnt == 2:
        n = i
        break
    li = [x for x in range(2, i+1) if is_prime(x) and i % x == 0]

    if sum(li) == 2:
        cnt += 1
    else:
        cnt = 0

print(n)    

