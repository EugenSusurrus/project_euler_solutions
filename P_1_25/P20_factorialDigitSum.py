"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def factorial(n):
    while n >= 0:
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return n * factorial(n-1)

large_number = factorial(100)

large_number_digit_sum = sum([int(digit) for digit in str(large_number)])

print(large_number_digit_sum)
