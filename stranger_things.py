n = int(input())
total_eleven = 0

for i in range(n):
    s = input()
    if s.count('11') >= 3:
        total_eleven += 1
print(total_eleven)