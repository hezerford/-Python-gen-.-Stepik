n = int(input())
l = []
sq = []

for _ in range(n):
    s = input()
    l.append(s)
    
k = int(input())

for _ in range(k):
    c = input()
    sq.append(c)

t = 0

for i in l:
    for j in sq:
        if j.lower() in i.lower():
            t += 1
            if t == 2:
                print(i)