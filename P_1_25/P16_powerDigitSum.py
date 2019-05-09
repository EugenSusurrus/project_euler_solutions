"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

large_num = int(2 ** 1000)
large_num_digits = [int(digit) for digit in str(large_num)]

power_digit_sum = sum(large_num_digits)

print(power_digit_sum)