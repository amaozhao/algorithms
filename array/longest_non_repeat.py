# coding: utf-8

# 给定一个字符串, 找到字符串中没有重复字符的最长子串

# 例子:

# 给定 "abcabcbb", 结果为 "abc", 长度为 3.

# 给定 "bbbbb", 结果位 "b", 长度为 1.

# 给定 "pwwkew", 结果 "wke", 长度 3.
# 注意结果必须为给定字符串的子串,
# "pwke" 不是一个子串.


def longest_non_repeat(s):
    start, maxlen = 0, 0
    used_char = {}
    for i, char in enumerate(s):
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1
        else:
            maxlen = max(maxlen, i - start + 1)
        used_char[char] = i
    return maxlen


a = "abcabcdefbb"
print(a)
print(longest_non_repeat(a))
