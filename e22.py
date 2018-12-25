import json

names = sorted(json.loads(open('e22.json').read()))

s = 0

for index, name in enumerate(names):
    s += sum(ord(c) - 64 for c in name) * (index + 1)

print(s)
