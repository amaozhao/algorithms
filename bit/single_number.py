"""
给定一个整形数组, 每个元素出现两次的除外, 找出这个数字.

注意:
你的算法需要线性的时间复杂度.
并不要使用额外的内存?
"""


def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    for num in nums:
        i ^= num
    return i

if __name__ == '__main__':
    li = [2, 2, 3, 3, 3, 4, 5]
    print(single_number(li))
