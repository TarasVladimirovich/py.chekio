from itertools import zip_longest

q = "xac\nxbc\nxc\nx".strip().replace(' ', '').split('\n')
print(q)

for i in zip_longest(*q):
    print(i)