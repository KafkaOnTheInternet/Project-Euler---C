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

li = [x for x in range(2, 10**3) if is_prime(x)]

ms, mr = 0, -1

for i in range(len(li)):
    s = 0
    for j in range(i, len(li)):
        s += li[j]
        if s > 10**6:
            break
        if (is_prime(s) and s > ms and j - i > mr):
            mr = j - i
            ms = s
print(ms, mr)

