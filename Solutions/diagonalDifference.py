#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left = 0
    right = 0
    length = len(arr) - 1;

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j and arr[i][j]:
                left += int(arr[i][j])

    for k in range(len(arr)):
        subArr = arr[k]
        for x in range(len(subArr) - 1, -1, -1):
            if x == length and subArr[x]:
                right += subArr[x]
        length -= 1

    return abs(left - right)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
