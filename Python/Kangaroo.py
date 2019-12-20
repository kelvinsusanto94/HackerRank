#   .-"-.
#  /|6 6|\
# {/(_0_)\}
#  _/ ^ \_
# (/ /^\ \)-'
#  ""' '""     하늘

# written by
# @author Wolverine 왕경민

# File Name : Kangaroo.py
# Date Created : 20/9/2019

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (v1 <= v2):
        return 'NO'
    else:
        while (x1 < x2):
            x1 += v1
            x2 += v2

    return 'YES' if x1 == x2 else 'NO'


if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print (result)