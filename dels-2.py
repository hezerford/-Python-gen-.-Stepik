n = int(input())

for i in range(1, n+1):
    print(i, sep='', end='')
    for j in range(1, n+1):
        if i % j == 0:
            print('+', end='', sep='')
    print()