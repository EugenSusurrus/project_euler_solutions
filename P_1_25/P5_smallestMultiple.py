"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def smallestMultiple(limit):
    """Returns the smallest number that is a even multiple of all the numbers from 0
    up to the limit"""

    smallestMultiple = 1
    dividers = list(range(1, limit + 1))
    while smallestMultiple:
        reminders = [smallestMultiple % divider for divider in dividers]
        if len(reminders) == limit and sum(reminders) == 0:
            return smallestMultiple

        smallestMultiple = smallestMultiple + 1


print(smallestMultiple(20))