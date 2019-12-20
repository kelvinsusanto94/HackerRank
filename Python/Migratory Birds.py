#   .-"-.
#  /|6 6|\
# {/(_0_)\}
#  _/ ^ \_
# (/ /^\ \)-'
#  ""' '""     하늘

# written by
# @author Wolverine 왕경민

# File Name : Migratory Birds.py
# Date Created : 20/9/2019

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    mcounter=0
    birdtype=0
    for i in range (1,6):
        curcounter=0
        for j in range (0,arr_count):
            if (i == arr[j]):
                curcounter+=1
        if (curcounter > mcounter):
            mcounter = curcounter
            birdtype = i
    return birdtype


if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print (str(result))
