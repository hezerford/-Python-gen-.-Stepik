s = input().split()
t = 0

for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            t += 1
print(t)