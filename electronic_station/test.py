d1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

for k, v in d1.items():
    print(k, v)

d2 = {x: x * x for x in range(10, 15)}
print(d2)

tmp = {}
for d in (d1, d2):
    tmp.update(d)

print(tmp)
print(tmp.keys())
print(tmp.values())
print(tmp.items())

