"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
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


num = 10000
amicable_numbers_list = []

divisors_dict = dict(enumerate(range(1, num + 1), 1))
divisors_dict = {key:divisors(value) for (key, value) in divisors_dict.items()}

amicable_num_list = []
for k in divisors_dict.keys():

    actual_div_sum = sum(divisors_dict[k])

    if actual_div_sum <= num:
        if sum(divisors_dict[actual_div_sum]) == k and k != actual_div_sum:
            if not set([k, actual_div_sum]).issubset(set(amicable_num_list)):   # to avoid pair repetition such as [220, 284] with [284, 220]
                amicable_num_list.extend([k, actual_div_sum])
        #print(f'{k}\t:\t{actual_div_sum}')

print('\n')
print(amicable_num_list)
print(f'\nSum of all amicable numbers under {num} evaluates to:\t{sum(amicable_num_list)}')

