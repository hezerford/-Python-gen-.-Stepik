s = input()
similar = 0

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        similar += 1
        
print(similar)