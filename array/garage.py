# coding: utf-8

# 有一个停车场只有一个空位. 给予初始状态的停车场和最后的状态.
# 我们每个步骤都是允许移动一辆车离开它的位置, 并将其移动到空的地方.
# 目标是找出重新排列所需的最少动作停车场从初始状态到最终状态.


# 假设初始状态如下:

# [1,2,3,0,4],
# 这里 1,2,3,4 是不同的车子, 0 表示空车位.

# 最终的结果要求是:

# [0,3,2,1,4].
# 我们可以互换 0 和 1, 把它变成 [1, 3, 2, 0, 4].
# 每次只可以换 0.

def garage(beg, end):
    i = 0
    moves = 0
    while beg != end:
        if beg[i] != 0 and beg[i] != end[i]:
            car = beg[i]
            empty = beg.index(0)
            final_pos = end.index(beg[i])
            if empty != final_pos:
                beg[final_pos], beg[empty] = beg[empty], beg[final_pos]
                print(beg)
                empty = beg.index(0)
                beg[beg.index(car)], beg[empty] = beg[
                    empty], beg[beg.index(car)]
                print(beg)
                moves += 2
            else:
                beg[beg.index(car)], beg[empty] = beg[
                    empty], beg[beg.index(car)]
                print(beg)
                moves += 1
        i += 1
        if i == len(beg):
            i = 0
    return moves

if __name__ == "__main__":
    initial = [1, 2, 3, 0, 4]
    final = [0, 3, 2, 1, 4]
    print("initial:", initial)
    print("final:", final)
    print(garage(initial, final))
