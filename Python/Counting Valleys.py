#   .-"-.
#  /|6 6|\
# {/(_0_)\}
#  _/ ^ \_
# (/ /^\ \)-'
#  ""' '""     하늘

# written by
# @author Wolverine 왕경민

# File Name : Counting Valleys.py
# Date Created : 17/9/2019

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sea = 0
    counter = 0
    for i in s:
        counter= counter+1 if i == "U" and sea == -1 else counter;
        sea= sea+1 if i == "U" else sea-1;
    return counter

if __name__ == '__main__':
    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(str(result))