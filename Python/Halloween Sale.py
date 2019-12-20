#   .-"-.
#  /|6 6|\
# {/(_0_)\}
#  _/ ^ \_
# (/ /^\ \)-'
#  ""' '""     하늘

# written by
# @author Wolverine 왕경민

# File Name : Halloween Sale.py
# Date Created : 13/12/2019

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    List = [p]

    while (True):
        p = p-d
        if (p>m):
            List.append(p)
        else:
            break

    if (sum(List) >= s):
        total = 0
        for i in range(len(List)):
            total += List[i]
            if (total >= s):
                return i
    else:
        s -= sum(List)
        count = s / m
        return math.floor(len(List) + count);
    # Return the number of games you can buy

if __name__ == '__main__':
    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    print (str(answer))