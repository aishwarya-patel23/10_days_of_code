#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the knightlOnAChessboard function below.
def knightlOnAChessboard(n):
    cost = [[-1 for _ in range(n - 1)] for _ in range(n - 1)]
    cost[n - 2][n - 2] = 1
    for i in range(n - 1):
        for j in range(i, n - 1):
            if i < n // 2 or j < n // 2:
                cost[i][j] = bfs(i + 1, j + 1, n)
                cost[j][i] = cost[i][j]
    return cost
def bfs(a, b, n):
    q = [(0, 0, 0)]
    visited = [[False] * n for _ in range(n)]
    while len(q):
        i, j, k = q.pop()
        if i == n - 1 and j == n - 1:
            return k
        moves = [(i + a, j + b), (i + b, j + a),(i - a, j - b), (i - b, j - a),
            (i - a, j + b), (i - b, j + a),(i + a, j - b), (i + b, j - a),]
            
        valid_moves = [(i_, j_) for i_, j_ in moves if 0 <= i_ < n and 0 <= j_ < n]
        for i_, j_ in valid_moves:
            if not visited[i_][j_]:
                q.insert(0, (i_, j_, k + 1))
                visited[i_][j_] = True
    return -1 


if __name__ == '__main__':

    n = int(input())

    result = knightlOnAChessboard(n)

    print(result)