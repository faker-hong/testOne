def maxSubArrat(nums):

    sum = nums[0]
    n = nums[0]
    for i in range(1, len(nums)):
        if n>0:
            n += nums[i]
        else:
            n = nums[i]
        if sum<n:
            sum = n
    return sum


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = maxSubArrat(nums)
    print(result)