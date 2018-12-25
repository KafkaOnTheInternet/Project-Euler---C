
print(sum([i for i in range(2, 1000000) if sum([int(x)**5 for x in str(i)]) == i]))

