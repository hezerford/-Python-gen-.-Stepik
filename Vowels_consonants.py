s = input()
vowels = 0
consonants = 0

for i in range(len(s)):
    if s[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        vowels += 1
    if s[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        consonants += 1

print('Количество гласных букв равно', vowels)
print('Количество согласных букв равно', consonants)