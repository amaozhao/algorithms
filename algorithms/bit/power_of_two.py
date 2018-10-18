"""
给定一个整数, 写一个函数判断是否这个数是否可以分解为2的n次方
"""
def is_power_of_two(n):
    """
    :type n: int
    :rtype: bool
    """
    return n > 0 and not n & (n-1)
