# coding: utf-8
"""
展开带有嵌套的列表:
例如:
input = [2, 1, [3, [4, 5], 6], 7, [8]]
flatten(input)
输出: [2, 1, 3, 4, 5, 6, 7, 8]
"""
import collections


def flatten(inputArr, outputArr=None):
    if not outputArr:
        outputArr = []
    for ele in inputArr:
        if isinstance(ele, collections.Iterable):
            flatten(ele, outputArr)
        else:
            outputArr.append(ele)
    return outputArr
