def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    dp = [1]*n

    for i in range(0, n):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
    return max(dp)

if __name__ == '__main__':
    lengthOfLIS([1,3,6,7,9,4,10,5,6])