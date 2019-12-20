#   .-"-.
#  /|6 6|\
# {/(_0_)\}
#  _/ ^ \_
# (/ /^\ \)-'
#  ""' '""     하늘

# written by
# @author Wolverine 왕경민

# File Name : Repeated String.py
# Date Created : 17/10/2019

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    counter, counter2 = 0, 0
    for i in range (len(s)):
        counter += (1 if s[i] == "a" else 0)
    repeat = n // len(s)

    for i in range (n % len(s)):
        counter2 += (1 if s[i] == "a" else 0)

    return (counter * repeat) + counter2

if __name__ == '__main__':
    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(str(result))