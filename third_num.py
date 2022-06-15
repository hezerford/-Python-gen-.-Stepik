n = int(input())

while n > 1000:
    n //= 10
n = n % 10
print(n)