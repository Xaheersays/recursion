n = 3745374
curr_sum = 0
def Reverse(n):
    global curr_sum
    curr_sum = curr_sum * 10 + (n % 10)
    if n % 10 == n:
        return
    return Reverse(n // 10)

Reverse(n)
print(curr_sum)

# another method without using global

import math


def calNumOfDigits(n):
    return int(math.log10(n))


def reverseDigitsForMe(n, dig):
    if n % 10 == n:
        return n
    rem = n % 10
    return rem * (10 ** dig) + reverseDigitsForMe(n // 10, dig - 1)


# n = 123456
print(reverseDigitsForMe(n, calNumOfDigits(n)))
