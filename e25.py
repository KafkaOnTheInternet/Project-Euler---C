def fib(n):
    a, b = 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            a, b = b, a+b
        return b

def num_len(n):
    #return len([int(x) for x in str(n)])
    return len(str(n))

n = 1

while(True):
    if num_len(fib(n)) == 1000:
        print(n)
        break
    n += 1