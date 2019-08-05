"""
    当前数额是否大于前一个与后一个之和
"""


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cur = 0
    pre = 0
    for i in nums:
        temp = cur
        cur = max(pre + i, cur)
        pre = temp
    return cur


if __name__ == '__main__':
    # rob([2,1,3,4])
    q = list()
    print(q.append([5,0]),5)