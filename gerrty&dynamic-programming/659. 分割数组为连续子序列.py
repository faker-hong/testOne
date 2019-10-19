import collections


class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = collections.Counter(nums)
        tails = collections.Counter()
        for x in nums:
            if count[x] == 0:
                continue
            elif tails[x] > 0:
                tails[x] -= 1
                tails[x + 1] += 1
            elif count[x + 1] > 0 and count[x + 2] > 0:
                count[x + 1] -= 1
                count[x + 2] -= 1
                tails[x + 3] += 1
            else:
                return False
            count[x] -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2,2,3,3]
    re = s.isPossible(nums)
    print(re)