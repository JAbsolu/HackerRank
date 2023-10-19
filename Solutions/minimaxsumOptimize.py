  #!/bin/python3

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
      total = 0

      min_val = float('inf')
      max_val = float('-inf')

      for num in arr:
          total = total + num
          if num > max_val:
              max_val = num

          if num < min_val:
              min_val = num

      min_sum = total - max_val
      max_sum = total - min_val

      print(f"{min_sum } {max_sum}")

  #Time is O(n)

  if __name__ == '__main__':

      arr = list(map(int, input().rstrip().split()))

      miniMaxSum(arr)
