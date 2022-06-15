abc = 'abcdefghijklmnopqrstuvwxyz'
l = []

for i in range(0, 26):
    l.append(abc[i] * (i+1))
print(l)