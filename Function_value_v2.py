n = int(input())
l = []

for i in range(n):
    i = (int(input()))
    print(i)
    l.append(i**2+2*i+1)

print()

print(*l, sep='\n')