class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)

        length = [1] * n    # length[i]以nums[i]结尾最长升序字符串长度
        count = [1] * n     # count[i]以nums[i]结尾最长升序字符串长度的个数

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[j] + 1 > length[i]:   # 第一次获得最大升序字符串
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

        res, tmp = 0, max(length)
        for i in range(n):
            if length[i] == tmp:
                res += count[i]

        return res


if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLIS([1,3,5,4,7])
    print(res)