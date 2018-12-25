coins= [1, 2, 5, 10, 20, 50, 100, 200]

a = 200

def ways(target, avc):
    if avc <= 0:
        return 1
    res = 0
    while target >= 0:
        res = res + ways(target, avc-1)
        target = target - coins[avc]
    return res
print(ways(a, 7))