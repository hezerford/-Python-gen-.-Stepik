s = input()
a = len(s) // 2 + len(s) % 2

print(s[a:] + s[:a])