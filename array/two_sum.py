"""
给定一个整型数组, 返回这样2个元素的索引: 这2个元素相加的结果为给定的值.

你可以假定这个结果只有一种情况, 但是每个元素只能使用一次.

例如:
    给定 nums = [2, 7, 11, 15], target = 9,

    因 nums[0] + nums[1] = 2 + 7 = 9,
    返回 [0, 1].
"""


def two_sum(nums: "List[int]", target: "int") -> "List[int]":
    dic = {}
    for i, num in enumerate(nums):
        if num in dic:
            return [dic[num], i]
        else:
            dic[target - num] = i


if __name__ == "__main__":
    arr = [3, 2, 4]
    target = 6
    res = two_sum(arr, target)
    print(res)
