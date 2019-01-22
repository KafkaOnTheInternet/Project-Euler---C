def check(n):
    for i in range(2, 7):
        if sorted(str(n*i)) != sorted(str(n)):
            return False
    return True

for i in range(1, 10**6):
    if check(i):
        break

print(i)


