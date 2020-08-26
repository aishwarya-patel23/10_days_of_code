#!/bin/python3
from __future__ import division
import os
import sys

# Complete the solve function below.

def exgcd(a, b):
   
    if b is 0:
        return (a, 1, 0)
    else:
        g, x, y = exgcd(b, a % b)
        return (g, y, x - (a // b) * y)


def modinv(a, m):
    
    _, x, y = exgcd(a, m)
    return (m + x % m) % m


def solve(a, b, x):
    if b > 0:
        return pow(a, b, x)
    else:
        return pow(modinv(a, x), -b, x)
if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        abx = input().split()

        a = int(abx[0])

        b = int(abx[1])

        x = int(abx[2])

        result = solve(a, b, x)

        print(result)

