'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
'''


def jump(nums):
    n = len(nums)
    end = 0
    step = 0
    maxPosition = 0

    for i in range(n-1):
        if maxPosition >= i:
            # 下一步所能跳跃的最远位置
            maxPosition = max(maxPosition, nums[i] + i)
            if i == end:
                end = maxPosition
                step += 1

    return step


if __name__ == '__main__':
    nums = [2]
    res = jump(nums)
    print(res)