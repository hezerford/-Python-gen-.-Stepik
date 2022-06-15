s = input()

if s.count('f') == 1:
    print('-1')
elif s.count('f') == 0:
    print('-2')
else:
    print(s.replace('f', '_', 1).find('f'))
