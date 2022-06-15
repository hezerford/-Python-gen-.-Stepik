n = int(input())
l = []

for i in range(n):
    n1 = int(input())
    l.append(n1)

del l[1::2]
print(l)