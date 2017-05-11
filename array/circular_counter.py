# coding: utf-8

"""人们围着圆桌坐了一圈, 每第三个成员打印它, 同时删除它, 下一个计数器在成员删除后立即开始.
打印，直到所有成员都用尽.

例子:
输入: 考虑 123456789 成员坐成一桌,
输出: 369485271
"""

a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def josepheus(int_list, skip):
    skip = skip - 1  # 列表计数从0开始
    idx = 0
    while len(int_list) > 0:
        # 改变计数以满足每3个成员选择一个
        idx = (skip + idx) % len(int_list)
        print (int_list.pop(idx))


josepheus(a, 3)

"""
the reason for hashing is that we have to find the index of the item which needs to be removed.
So for e.g. if you iterate with the initial list of folks with every 3rd item eliminated:

INPUT
int_list = 123456789
skip = 3

While Iteration:

int_list = 123456789
len(int_list) = 9
skip = 2 # as int_list starts from 0
idx = (0 + 2) % 9 #here previous index was 0
so 3rd element which is 3 in this case eliminated
int_list = 12456789
len(int_list) = 8
idx = (2 + 2) % 8 #here previous index was 2
so 3rd element starting from 4th person which is 6 would be deleted.
and so on
The reason why we have to do this way is I am not putting the people who escape at the back of list so ideally in 2 while iteration the list should have been
45678912 and then no hashing needed to be done, which means you can directly remove the third element
"""
