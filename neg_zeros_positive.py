n = int(input())
neg = []
zeros = []
positive = []

for i in range(n):
    n1 = int(input())
    if n1 < 0:
        neg.append(n1)
    elif n1 == 0:
        zeros.append(n1)
    elif n1 > 0:
        positive.append(n1)
print(*neg, *zeros, *positive, sep='\n')