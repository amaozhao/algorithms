"""
反转非负整形的32位bit的整数

例如, 给定输入 43261596
(相当于二进制数 00000010100101000001111010011100),
返回 964176192
(相当于二进制数 00111001011110000010100101000000).
"""
def reverse_bits(n):
    m = 0
    i = 0
    while i < 32:
        m = (m << 1) + (n & 1)
        n >>= 1
        i += 1
    return m