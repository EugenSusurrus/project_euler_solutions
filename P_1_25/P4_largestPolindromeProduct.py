"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import math

def findLargestPolindrome(startNum, endNum):
    polindromesList = list()
    for i in range(endNum, startNum-1, -1):
        if str(i) == str(i)[::-1]:
            polindromesList.append(i)

    return polindromesList

polindromeList = findLargestPolindrome(10000, 1000000)

print(polindromeList)

def largestProductPalindrome(palindromeList):

    largespolindrme = palindromeList[0]
    divider = -1
    digits = -1
    for polindrome in palindromeList:

        for i in range(999, 99, -1):
            digits = int(math.log10(polindrome / i))+1
            reminder = polindrome % i
            if reminder == 0 and digits == 3:
                largespolindrme = polindrome
                return largespolindrme, i

print(largestProductPalindrome(polindromeList))

