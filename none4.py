def quick_merge(n):
    l = []
    for i in range(n):
        n = [int(i) for i in input().split()]
        l += n
    l.sort()
    return l

n = int(input())

print(*quick_merge(n))