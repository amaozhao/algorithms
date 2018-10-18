"""
给定一个整形数组, 每个元素出现两次的除外, 找出这个数字.

NOTE: This also works for finding a number occurring odd
      number of times, where all the other numbers appear
      even number of times.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
"""
def single_number(nums):
    """
    Returns single number, if found.
    Else if all numbers appear twice, returns 0.
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    for num in nums:
        i ^= num
    return i
