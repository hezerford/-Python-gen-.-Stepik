n = int(input())
c = 0
l = []

for i in range(n):
    n1 = int(input())
    c += n1
    l.append(c)
    c = n1
print(l[1:])