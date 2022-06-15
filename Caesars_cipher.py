n = int(input())
s = input()

for i in s:
    dec = ord(i) - n
    if dec < 97:
        dec += 26
    print(chr(dec), end='')