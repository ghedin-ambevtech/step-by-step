#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#





def compareTriplets(a, b):
    points = []
    alice = 0
    bob = 0
    for n in range(2):
        if a[n] > b[n]:
            alice += 1
        elif a[n] < b[n]:
            bob += 1
    points[0] = alice
    points[1] = bob
    return points

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))
    print(a)
    print(b)
    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
