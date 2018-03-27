"""
# 给定一个字符串, 找到字符串中没有重复字符的最长子串

# 例子:

# 给定 "abcabcbb", 结果为 "abc", 长度为 3.

# 给定 "bbbbb", 结果位 "b", 长度为 1.

# 给定 "pwwkew", 结果 "wke", 长度 3.
# 注意结果必须为给定字符串的子串,
# "pwke" 不是一个子串.
"""


def longest_non_repeat(string):
    """
    Finds the length of the longest substring
    without repeating characters.
    """
    if string is None:
        return 0
    temp = []
    max_len = 0
    for i in string:
        if i in temp:
            temp = []
        temp.append(i)
        max_len = max(max_len, len(temp))
    return max_len


def longest_non_repeat_two(string):
    """
    Finds the length of the longest substring
    without repeating characters.
    Uses alternative algorithm.
    """
    if string is None:
        return 0
    start, max_len = 0, 0
    used_char = {}
    for index, char in enumerate(string):
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1
        else:
            max_len = max(max_len, index - start + 1)
        used_char[char] = index
    return max_len

import unittest

class TestLongestNonRepeat(unittest.TestCase):

    def test_longest_non_repeat(self):

        string = "abcabcbb"
        self.assertEqual(longest_non_repeat(string), 3)

        string = "bbbbb"
        self.assertEqual(longest_non_repeat(string), 1)
        
        string = "pwwkew"
        self.assertEqual(longest_non_repeat(string), 3)

    def test_longest_non_repeat_two(self):
        
        string = "abcabcbb"
        self.assertEqual(longest_non_repeat_two(string), 3)

        string = "bbbbb"
        self.assertEqual(longest_non_repeat_two(string), 1)
        
        string = "pwwkew"
        self.assertEqual(longest_non_repeat_two(string), 3)
        
if __name__ == "__main__":
    
    unittest.main()
