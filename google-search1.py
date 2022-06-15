n = int(input())
l = []  

for _ in range(n):
    s = input()
    l.append(s)

k = input()

for j in l:
    if k.lower() in j.lower():
        print(j)