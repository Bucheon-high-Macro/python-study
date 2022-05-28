a = []
n = 0
for n in range(1, 101):
    b = str(n)
    a.append(b)
print(a)
del a[:]
for n in range(1, 101):
    a.append(n)
print(a)
