# coding: utf-8

# 有一个停车场只有一个空位. 给予初始状态的停车场和最后的状态.
# 我们每个步骤都是允许移动一辆车离开它的位置, 并将其移动到空的地方.
# 目标是找出重新排列所需的最少动作停车场从初始状态到最终状态.


# 假设初始状态如下:

# [1,2,3,0,4],
# 这里 1,2,3,4 是不同的车子, 0 表示空车位.

# 最终的结果要求是:

# [0,3,2,1,4].
# We can swap 1 with 0 in the initial array to get [0,2,3,1,4] and so on.
# Each step swap with 0 only.
# Edited by cyberking-saga
"""
Now also prints the sequence of changes in states.
Output of this example :-

initial: [1, 2, 3, 0, 4]
final:   [0, 3, 2, 1, 4]
Steps =  4
Sequence : 
0 2 3 1 4
2 0 3 1 4
2 3 0 1 4
0 3 2 1 4

"""


def garage(initial, final):
    initial = initial[::]     # create a copy to prevent changes in original 'initial'.
    steps = 0
    seq = []                  # list of each step in sequence
    while initial != final:
        zero = initial.index(0)
        if zero != final.index(0):
            car_to_move = final[zero]
            pos = initial.index(car_to_move)
            initial[zero], initial[pos] = initial[pos], initial[zero]
        else:
            for i in range(len(initial)):
                if initial[i] != final[i]:
                    initial[zero], initial[i] = initial[i], initial[zero]
                    break
        seq.append(initial[::])
        steps += 1
    seq = "\n".join(" ".join(map(str, s)) for s in seq)   # convert to string
    return steps, seq


if __name__ == "__main__":
    initial = [1, 2, 3, 0, 4]
    final = [0, 3, 2, 1, 4]
    print("initial:", initial)
    print("final:  ", final)
    steps, seq = garage(initial, final)
    print("No. of Steps = ", steps)
    print("Steps Sequence : ")
    print(seq)
