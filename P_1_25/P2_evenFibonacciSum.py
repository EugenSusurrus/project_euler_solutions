"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""

targetVal = 4000000

def F(n):
    """Returns the nth element in the 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    fashion fibonacci series"""

    if n == 0: return 0
    elif n == 1: return 1
    elif n == 2: return 2
    else: return F(n - 1) + F(n - 2)

fibonacciElement = 1
sumEvenFibonacci = 0

while F(fibonacciElement) <= targetVal:

    if F(fibonacciElement) % 2 == 0:
        sumEvenFibonacci = sumEvenFibonacci + F(fibonacciElement)

    fibonacciElement = fibonacciElement + 1

print(f'The sum of the Fibonacci even elements whos values do not exceed {targetVal} is equal to {sumEvenFibonacci}\n')