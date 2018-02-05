# coding: utf-8
"""
轮换列表的最后 n 个元素(步长为 k).

例如, n = 7 and k = 3,
列表为 [1,2,3,4,5,6,7] 转换结果为 [5,6,7,1,2,3,4].

Note:
有很多其他的方案, 这里列出3种.
"""


#
# 轮换整个列表 'k' 次
# T(n)- O(nk)
#
def rotate_one_by_one(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    for i in range(k):
        temp = nums[n-1]
        for j in range(n-1, 0, -1):
            nums[j] = nums[j-1]
        nums[0] = temp


#
# 颠倒部分列表元素, 然后拼接整个列表
# T(n)- O(n)
#
def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    reverse(nums, 0, n - k - 1)
    reverse(nums, n - k, n - 1)
    reverse(nums, 0, n - 1)


def reverse(array, a, b):
    while a < b:
        array[a], array[b] = array[b], array[a]
        a += 1
        b -= 1

def rotate_array(array, k):
    if array is None:
        return None
    length = len(array)
    return array[length - k:] + array[:length - k]
