def canPartitionKSubsets(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    # 是否存在k个值相等的非空子集
    # 先做判断sum（nums）能否被k整除，不能整除说明不存在
    if sum(nums) % k != 0:
        return False

    value = sum(nums) // k
    nums.sort(reverse=True)
    n = len(nums)
    if n<k:
        return False
    visit = set()

    def dfs(k, tmp_sum, loc):
        if tmp_sum == value:
            return dfs(k-1, 0, 0)
        if k==1:
            return True
        for i in range(loc,n):
            if i not in visit and nums[i] + tmp_sum <= value:
                visit.add(i)
                if dfs(k, tmp_sum + nums[i], i+1):
                    return True
                visit.remove(i)
        return False
    return dfs(k, 0, 0)