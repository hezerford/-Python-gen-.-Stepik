s = input()
Sum = 0
Mult = 0

for i in range(len(s)):
    if s[i] in '+':
        Sum += 1
    if s[i] in '*':
        Mult += 1

print('Символ', '+', 'встречается', Sum, 'раз')
print('Символ', '*', 'встречается', Mult, 'раз')