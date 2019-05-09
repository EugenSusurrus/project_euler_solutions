"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def maxPrimeFactors(n):
    """Initialize the maximum prime factor variable
    with the lowest one"""

    maxPrime = -1

    # Print the number of 2s that divide n
    while n % 2 == 2:
        maxPrime = 2
        n = n / 2

    # n must be odd at this point,
    # thus skip the even numbers and
    # iterate only for odd integers
    for i in range(3, int(n ** (1/2)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i

    # this condition is to handle the
    # case when n is a prime number
    # greater than 2
    if n > 2:
        maxPrime = n

    return int(maxPrime)

num = 600851475143
print(maxPrimeFactors(num))