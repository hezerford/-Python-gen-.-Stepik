s = input()
t = 0

for i in s:
    if i != i.upper():
        t += 1
print(t)