def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if sum(nums) % 2 != 0:
        return False

    avg = sum(nums) // 2

    dp = [[0]*(avg+1) for _ in range(len(nums)+1)]
    for i in range(1, len(nums)+1):
        for j in range(1, avg+1):
            if j < nums[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i-1]] + nums[i-1])
        if dp[i][-1] == avg:
            return True


if __name__ == '__main__':
    nums = [1, 2, 4, 5]
    print(canPartition(nums))