"""
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

def spell_num(num):
    """
    Takes a number up to three digits as an input and returns the spelled number as per english dictionary
    :param num: int input number
    :return: spelled_num: str string of the spelled input number
    """
    str_num = str(num)

    hundreds_nums_dict = {1:'one',
                          2:'two',
                          3:'three',
                          4:'four',
                          5:'five',
                          6:'six',
                          7:'seven',
                          8:'eight',
                          9:'nine',
                          10:'ten',
                          11:'eleven',
                          12:'twelve',
                          13:'thirteen',
                          14:'fourteen',
                          15:'fifteen',
                          16:'sixteen',
                          17:'seventeen',
                          18:'eighteen',
                          19:'nineteen',
                          20:'twenty',
                          30:'thirty',
                          40:'forty',
                          50:'fifty',
                          60:'sixty',
                          70:'seventy',
                          80:'eighty',
                          90:'ninety'}

    tens_digit_list = {2:'twenty-',
                       3:'thirty-',
                       4:'forty-',
                       5:'fifty-',
                       6:'sixty-',
                       7:'seventy-',
                       8:'eighty-',
                       9:'ninety-'}
    if len(str_num) == 4 and str_num == '1000':
        spelled_num = 'one thousand'
    elif len(str_num) == 3:
        if str_num[-2:] == '00':
            spelled_num = hundreds_nums_dict[int(str_num[0])] + ' hundred'
        elif str_num[1] == '0':
            spelled_num = hundreds_nums_dict[int(str_num[0])] + ' hundred and ' + \
                          hundreds_nums_dict[int(str_num[2])]
        elif str_num[1] == '1' or str_num[-1] == '0':
            spelled_num = hundreds_nums_dict[int(str_num[0])] + ' hundred and ' + \
                          hundreds_nums_dict[int(str_num[1:3])]
        else:
            spelled_num = hundreds_nums_dict[int(str_num[0])] + ' hundred and ' + \
                          tens_digit_list[int(str_num[1])] + \
                          hundreds_nums_dict[int(str_num[2])]

    elif len(str_num) == 2:
        if str_num[0] == '1' or str_num[1] == '0':
            spelled_num = hundreds_nums_dict[int(str_num[0:2])]
        else:
            spelled_num = tens_digit_list[int(str_num[0])] + \
                          hundreds_nums_dict[int(str_num[1])]

    else: spelled_num = hundreds_nums_dict[int(str_num[0])]

    return spelled_num


spelled_num_list = [spell_num(i) for i in range(1, 1001)]
spelled_num_list = '\n'.join(spelled_num_list)

import re

stripped_spelled_num_list = re.sub(r'\W+', '', spelled_num_list)
print(len(stripped_spelled_num_list))

