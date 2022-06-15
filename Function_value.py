n = int(input())
l = []

for _ in range(n):
    n1 = int(input())
    l.append(n1)
    print(n1)

print()

for j in l:
    f = j ** 2 + 2 * j + 1
    print(f)