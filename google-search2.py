n = int(input())
l = []  #список со строками
l1 = [] #список с запросами
t = 0

for _ in range(n): #строки
    s = input()
    l.append(s)

k = int(input())

for _ in range(k): #поисковые запросы
    s1 = input()
    l1.append(s1)

for i in range(k):
    for j in l1:
        for k in l:
            if j[i] in k:
                print()