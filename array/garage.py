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


def garage(initial, final):
    i = 0
    steps = 0
    while initial != final:
        if initial[i] != 0 and initial[i] != final[i]:
            zero = initial.index(0)
            final_pos = final.index(initial[i])
            if zero != final_pos:
                # two swaps required
                initial[final_pos], initial[zero] = initial[
                    zero], initial[final_pos]
                zero = initial.index(0)
                initial[i], initial[zero] = initial[zero], initial[i]
                steps += 2
            else:
                # one swap is enough
                initial[i], initial[zero] = initial[zero], initial[i]
                steps += 1
        i = (i + 1) % len(initial)
    return steps


if __name__ == "__main__":
    initial = [1, 2, 3, 0, 4]
    final = [0, 3, 2, 1, 4]
    print("initial:", initial)
    print("final:", final)
    print(garage(initial, final))
