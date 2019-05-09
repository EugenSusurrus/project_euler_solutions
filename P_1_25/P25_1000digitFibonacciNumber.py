"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def fibonacci(n):
    """Returns the nth element in the 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    fashion fibonacci series"""
    if n == 0: return 0
    elif n == 1: return 1
    elif n == 2: return 1
    else: return fibonacci(n - 1) + fibonacci(n - 2)

def fib_generator():
    a, b = 1, 0
    while True:
        yield a
        b = a + b
        yield b
        a = a + b

from itertools import islice


num_digits = 1000
fibonacci_index = 1
fibonacci_element = fib_generator()
fib_num = next(fibonacci_element)

while len(str(fib_num)) < num_digits:
    fibonacci_index += 1
    fib_num = next(fibonacci_element)

print(next(islice(fibonacci_element, fibonacci_index, fibonacci_index + 1)))
print('*********************************************************************')
print(fibonacci_index)