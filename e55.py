"""
Never forms a number = Lychrel

n < 10 ** 4 will become Palindrome in < 50 iters

"""

nL = []

def palindrome(n):
    return n == int(str(n)[::-1])

def count_p(n):
    global nL
    t = n
    for _ in range(50):
        if palindrome(t + int(str(t)[::-1])):
            nL.append(t)
            break
        else:
            t = t + int(str(t)[::-1])

for i in range(1, 10 ** 4):
    count_p(i)


print(10 ** 4 - len(nL))

