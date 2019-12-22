#   .-"-.
#  /|6 6|\
# {/(_0_)\}
#  _/ ^ \_
# (/ /^\ \)-'
#  ""' '""     하늘

# written by
# @author Wolverine 왕경민

# File Name : Service Lane.py
# Date Created : 20/12/2019

# Complete the serviceLane function below.
def serviceLane(width, cases):
    #cara 1
    arr = []
    for i in range (len(cases)):
        arr.append(min(width[cases[i][0]:cases[i][1]+1]))
    return arr

    #cara 2
    # return [min(width[x:y+1]) for x, y in cases]

if __name__ == '__main__':
    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(width, cases)

    print('\n'.join(map(str, result)))
    print('\n')
