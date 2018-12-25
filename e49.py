from collections import Counter

def prime(n):
    i = 5
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    while(i*i <= n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perm(a, b):
    return len(str(a)) == len(str(b)) and Counter(str(a)) == Counter(str(b))

primes = []
nums = []
done = False

for i in range(1000, 10000):
    if prime(i):
        primes.append(i)


for i in range(len(primes) - 1):
    for j in range(i+1, len(primes)-1):
        if is_perm(primes[i], primes[j]):
            s = 2*primes[j] - primes[i]
            if s in primes and is_perm(primes[i], s):
                nums.append(primes[i])
                nums.append(primes[j])
                nums.append(s)
                if primes[i] != 1487:
                    done = True
                    break
    if done:
        print('done')
        break

for num in nums:
    print(num)
            
    