# Given an arbitrary integer, print its' separate digits.

def int_input (message):
    i = None
    while True:
        try:
            i = int(input(message))
        except ValueError:
            print('Input should be a valid integer')
            continue
        else:
            return i
        
def to_digits (number):
    digits = []
    while number > 0:
        digits.insert(0, number % 10)
        number //= 10
    return digits

number = int_input('Enter an integer: ')
isNegative = number < 0
digits = to_digits(abs(number))

if isNegative:
    print('-')
print ('\n'.join(map(str, digits)))

# Print the minimum digit in the integer (without using the library function).

min = digits[0]
for digit in digits[1:]:
    if digit < min:
        min = digit
print('Minimum digit: {}'.format(min))

# Reverse the input integer (without using a separate list to store the digits) and print it.

reversed = 0
p = 1
for digit in digits:
    reversed += p * digit
    p *= 10
if isNegative:
    reversed *= -1
print ('Reversed integer: {}'.format(reversed))

# FOLLOWUP: Given two integers, return a third one created from their even digits.

first = to_digits(int_input('Enter the first integer: '))
second = to_digits(int_input('Enter the second integer: '))

merged = 0
for digit in map(int, first + second):
    if digit % 2 == 0:
        merged *= 10
        merged += digit
print ('Merged integer: {}'.format(merged))
