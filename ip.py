s = input().split('.')
t = 0

for i in range(len(s)):
    s[i] = int(s[i])
    if 0 <= s[i] <= 255:
        t += 1
    else:
        print('НЕТ')
        break
if t == 4:
    print('ДА')