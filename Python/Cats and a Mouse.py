#   .-"-.
#  /|6 6|\
# {/(_0_)\}
#  _/ ^ \_
# (/ /^\ \)-'
#  ""' '""     하늘

# written by
# @author Wolverine 왕경민

# File Name : Cats and a Mouse.py
# Date Created : 17/9/2019

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    win = "Mouse C" if (abs(x-z) == abs(y-z)) else "Cat A" if (abs(x-z) < abs(y-z)) else "Cat B"
    return win

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)
