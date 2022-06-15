n = int(input())
fact = 1
sum_f = 0

for i in range(1, n+1):
    fact *= i
    sum_f += fact
print(sum_f)

