def PredictTheWinner(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    dp = [[0]*len(nums) for _ in range(len(nums))]
    print(dp)
    for i in range(len(nums)):
        dp[i][i] = nums[i]
    for i in range(len(nums)-1, -1, -1):
        for j in range(i+1, len(nums)):
            dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])

    return dp[0][-1]>0


if __name__ == '__main__':
    print(PredictTheWinner([1,5,2]))