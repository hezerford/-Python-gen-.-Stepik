s = input()
t = 0

for i in range(len(s)):
    if s[i] in '0123456789':
        t += 1

if t > 0:
    print('Цифра')
else:
    print('Цифр нет')