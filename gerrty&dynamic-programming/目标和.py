def findTargetSumWays(nums, S):
    """
    :type nums: List[int]
    :type S: int
    :rtype: int
    """
    if sum(nums) < S or (sum(nums) + S) % 2 == 1: return 0
    P = (sum(nums) + S) // 2
    dp = [1] + [0 for _ in range(P)]
    for num in nums:
        for j in range(P, num - 1, -1):
            dp[j] += dp[j - num]
    return dp[P]


if __name__ == '__main__':
    print(findTargetSumWays([1, 1, 1, 1, 1], 3))


