"""
给定一个整型数组, 返回这样2个元素的索引: 这2个元素相加的结果为给定的值.

你可以假定这个结果只有一种情况, 但是每个元素只能使用一次.

例如:
    给定 nums = [2, 7, 11, 15], target = 9,

    因 nums[0] + nums[1] = 2 + 7 = 9,
    返回 [0, 1].
"""


def two_sum(array, target):
    dic = {}
    for i, num in enumerate(array):
        if num in dic:
            return dic[num], i
        else:
            dic[target - num] = i
    return None
<<<<<<< HEAD


class TestSuite(unittest.TestCase):

    def test_two_sum(self):

        self.assertTupleEqual((0, 2), two_sum([2, 11, 7, 9], target=9))
        self.assertTupleEqual((0, 3), two_sum([-3, 5, 2, 3, 8, -9], target=0))

        self.assertIsNone(two_sum([-3, 5, 2, 3, 8, -9], target=6))


if __name__ == "__main__":
    unittest.main()
=======
>>>>>>> upstream/master
