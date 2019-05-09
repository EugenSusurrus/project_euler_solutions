"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def gen_primes(n):
    """
    Returns a list of primes below the number n.
    :return:
    List of primes primeList
    """

    primes = list()
    for possiblePrime in range(2, n):

        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(possiblePrime)

    return primes

print(gen_primes(10))
print(sum(gen_primes(10)))
print(sum(gen_primes(2000000)))
