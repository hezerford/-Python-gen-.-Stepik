n = int(input())
l = []

for i in range(n):
    n1 = int(input())
    l.append(n1)

l.remove(max(l))
l.remove(min(l))

print(*l, sep='\n')