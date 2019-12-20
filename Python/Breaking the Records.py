#   .-"-.
#  /|6 6|\
# {/(_0_)\}
#  _/ ^ \_
# (/ /^\ \)-'
#  ""' '""     하늘

# written by
# @author Wolverine 왕경민

# File Name : Breaking the Records
# Date Created : 20/9/2019

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    minimum = scores[0]
    maximum = scores[0]
    maxcount = 0
    mincount = 0

    for i in range(1, len(scores), 1):
        if (maximum < scores[i]):
            maximum = scores[i]
            maxcount += 1

        if (minimum > scores[i]):
            minimum = scores[i]
            mincount += 1
    return maxcount, mincount


if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print (' '.join(map(str, result)))
    print ('\n')