#   .-"-.
#  /|6 6|\
# {/(_0_)\}
#  _/ ^ \_
# (/ /^\ \)-'
#  ""' '""     하늘

# written by
# @author Wolverine 왕경민

# File Name : Electronics Shop.py
# Date Created : 17/9/2019

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #Solusi 1
    # price = -1
    # for k in keyboards:
    #     for d in drives:
    #         price = k+d if price < k+d and k+d <= b else price
    # return price

    #Solusi 2
    hasil = [k+d for k in keyboards for d in drives]
    hasil.append(-1)
    return max([x for x in hasil if x <= b])

if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print (str(moneySpent))
