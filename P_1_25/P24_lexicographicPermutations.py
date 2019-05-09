"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of
the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

"""
def perms(elements):
    if len(elements) <=1:
    
        yield elements
    else:
        for perm in perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

permutations_list = []
permutation = perms([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

while len(permutations_list) < 1000000:
    permutations_list.append(''.join(map(str, next(permutation))))

permutations_list.sort()

print(permutations_list[-1])

"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
from itertools import permutations
all_permutations = list(permutations(numbers))
all_permutations.sort()
print(''.join(map(str, all_permutations[999999])))
