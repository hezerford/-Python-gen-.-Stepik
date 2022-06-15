s = input().lower().split()
a = s.count('a')
an = s.count('an')
the = s.count('the')

print('Общее количество артиклей:', a + an + the)
