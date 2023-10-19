
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    maximum = -math.inf
    minimum = math.inf

    for i in range(len(arr)):
        current = arr[i]
        currentMax = 0
        currentMin = 0
        for j in range(len(arr)):
            currentMax = arr[j] + currentMax
            currentMin = arr[j] + currentMin

        currentMax = currentMax - current
        currentMin = currentMin - current

        if currentMin < minimum:
            minimum = currentMin

        if currentMax > maximum:
            maximum = currentMax

    print(f"{minimum} {maximum}")

#time is O(n^2)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
