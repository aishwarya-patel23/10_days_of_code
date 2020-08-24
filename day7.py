#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    counts=[[] for i in range(100)]

    for i in range(len(arr)//2):
        arr[i][1]='-'

    for i in arr:
        counts[int(i[0])].append(i[1])

    for a in counts:
        for b in a:
            print(b, end=" ")

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
