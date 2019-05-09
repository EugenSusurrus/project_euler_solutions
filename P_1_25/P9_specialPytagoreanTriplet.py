"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def pythagorean_triplet(n):
    """
    Returns pythagorean triplets until the specified number n
    """

    for b in range(n):
        for a in range(1,b):
            c = (a * a + b * b) ** (1/2)
            if c % 1 == 0 and sum([a, b, int(c)]) == 1000:
                # return [a, b, int(c)]
                return [a, b, int(c)]

result = pythagorean_triplet(1000)
print(result[0] *
      result[1] *
      result[2] )
