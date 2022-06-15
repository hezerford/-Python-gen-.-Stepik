n = int(input())
third_num = 0
even_digits = 0
total_last_digits = 0
even_digit = 0
big_five = 0
multiply_big_seven = 1
zero_and_five = 0
last_digit_1 = n % 10

while n != 0:
    last_digit = n % 10
    if last_digit_1 == last_digit:
        total_last_digits += 1
    if last_digit == 3:
        third_num += 1
    if last_digit % 2 == 0:
        even_digits += 1
    if last_digit > 5:
        big_five += last_digit
    if last_digit > 7:
        multiply_big_seven *= last_digit 
    if last_digit == 0 or last_digit == 5:
        zero_and_five += 1
    n //= 10

print(third_num, total_last_digits, even_digits, big_five, multiply_big_seven, zero_and_five, sep='\n', end='')