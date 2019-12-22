#   .-"-.
#  /|6 6|\
# {/(_0_)\}
#  _/ ^ \_
# (/ /^\ \)-'
#  ""' '""     하늘

# written by
# @author Wolverine 왕경민

# File Name : Equalize the Array.py
# Date Created : 20/12/2019

# Complete the equalizeArray function below.
def equalizeArray(arr):
    #arr.count(x) menghitung jumlah element x didalam array
    #for x in arr mengambil tiap x di dalam array
    return len(arr) - max(arr.count(x) for x in arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(str(result))
