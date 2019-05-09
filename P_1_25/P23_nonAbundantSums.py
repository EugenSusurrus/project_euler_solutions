"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as
the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced
any further by analysis even though it is known that the greatest number that cannot be expressed as the
sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def divisors(n):
    divs = [1]
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            divs.extend([i, int(n/i)])
    #divs.extend([n])   #adds the actual number to the divisors list, this is true in math, but somethimes you
                        #dont ned this functionality
    divs = list(set(divs))

    return divs

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

bound = 28123
abundant_list = []
non_abundant_sum_integers = set([])
abundant_sum_list = []

for i in range(1, bound + 1):
    if sum(divisors(i)) > i:
        abundant_list.append(i)

for i in range(0, len(abundant_list)):
    for j in range(i, len(abundant_list)):
        if abundant_list[i] + abundant_list[j] <= bound:
            abundant_sum_list.append(abundant_list[i] + abundant_list[j])

non_abundant_sum_integers = set(list(range(1, bound + 1))).difference(set(abundant_sum_list))


print(sum(non_abundant_sum_integers))