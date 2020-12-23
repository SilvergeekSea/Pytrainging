"""
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Example:
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

"""

def digitrootInternal(n):
    strNumbers = str(n)
    intSum = 0
    i = 0
    while i<len(strNumbers):
        intSum += int(strNumbers[i])
        i += 1
    return str(intSum)


def digital_root(n):
    strNumbers1 = str(n)
    while len(strNumbers1) > 1:
        strNumbers1 = digitrootInternal(strNumbers1)
    print (f'sum is {strNumbers1}')
    return int(strNumbers1)



digital_root(16)
digital_root(942)
digital_root(132189)
digital_root(493193)