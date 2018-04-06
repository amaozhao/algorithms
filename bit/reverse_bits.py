"""
反转非负整形的32位bit的整数

例如, 给定输入 43261596
(相当于二进制数 00000010100101000001111010011100),
返回 964176192
(相当于二进制数 00111001011110000010100101000000).
"""
import unittest


def reverse_bits(n):
    m = 0
    i = 0
    while i < 32:
        m = (m << 1) + (n & 1)
        n >>= 1
        i += 1
    return m


class TestSuite(unittest.TestCase):

    def test_reverse_bits(self):

        self.assertEqual(43261596, reverse_bits(964176192))
        self.assertEqual(964176192, reverse_bits(43261596))
        self.assertEqual(1, reverse_bits(2147483648))

        # bin(0) => 00000000000000000000000000000000
        self.assertEqual(0, reverse_bits(0))

        # bin(2**32 - 1) => 11111111111111111111111111111111
        self.assertEqual(2**32 - 1, reverse_bits(2**32 - 1))


if __name__ == '__main__':

    unittest.main()