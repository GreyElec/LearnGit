# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 13:42:48 2018

@author: black
"""
import math
M = [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]


def solution():
    res = [[0] * len(M[0]) for i in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            line_lower, line_upper = i - 1 if i - \
                1 >= 0 else 0, i + 1 if i + 1 < len(M) else i
            col_lower, col_upper = j - 1 if j - \
                1 >= 0 else 0, j + 1 if j + 1 < len(M[0]) else j
            Sum, tic = 0, 0
            for ind in range(line_lower, line_upper + 1, 1):
                for col in range(col_lower, col_upper + 1, 1):
                    Sum += M[ind][col]
                    tic += 1
            res[i][j] = math.floor(Sum / tic)
    return res


print(solution())
