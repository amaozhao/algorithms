"""
给定一个整数, 写一个函数判断是否这个数是否可以分解为2的n次方
"""
import unittest


def is_power_of_two(n):
    """
    :type n: int
    :rtype: bool
    """
    return n > 0 and not n & (n-1)


class TestSuite(unittest.TestCase):

    def test_is_power_of_two(self):

        self.assertTrue(is_power_of_two(64))
        self.assertFalse(is_power_of_two(91))
        self.assertTrue(is_power_of_two(2**1001))
        self.assertTrue(is_power_of_two(1))
        self.assertFalse(is_power_of_two(0))


if __name__ == '__main__':

    unittest.main()
