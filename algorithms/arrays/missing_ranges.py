# coding: utf-8

# 找到给定列表中从给定最小值和给定最大值的缺失值.
# 例子: [3, 5] lo=1 hi=10 => answer: [1->2, 4, 6->10]

import unittest

def missing_ranges(arr, lo, hi):

    res = []
    start = lo

    for n in arr:

        if n == start:
            start += 1
        elif n > start:
            res.append((start, n-1))
            start = n + 1

    if start <= hi:                 # after done iterating thru array,
        res.append((start, hi))     # append remainder to list

    return res
