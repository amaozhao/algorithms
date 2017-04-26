# coding: utf-8
"""
展开带有嵌套的列表:
例如:
input = [2, 1, [3, [4, 5], 6], 7, [8]]
flatten(input)
输出: [2, 1, 3, 4, 5, 6, 7, 8]
"""


def list_flatten(l, a=None):
    a = list(a) if isinstance(a, (list, tuple)) else []
    for i in l:
        if isinstance(i, (list, tuple)):
            # 这里判断是不是列表或元组, 然后采用嵌套函数执行(还有其他更高效的实现吗)
            a = list_flatten(i, a)
        else:
            a.append(i)
    return a
