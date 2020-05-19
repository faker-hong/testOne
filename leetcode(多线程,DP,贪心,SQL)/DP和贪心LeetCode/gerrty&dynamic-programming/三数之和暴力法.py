class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        answer2 = []
        for x in range(0, len(nums)):
            for y in range(0, len(nums)):
                for z in range(0, len(nums)):
                    if x != y and x != z and y != z and nums[x] + nums[y] + nums[z] == 0:
                        list = [nums[x], nums[y], nums[z]]
                        list.sort()
                        # print("етЪЧ", list)
                        answer.append(list)
                        # print(answer)
        for i in answer:
            if not i in answer2:
                answer2.append(i)
        print(answer2)


p = Solution()
nums = [-1, 0, 1, 2, -1, -4]
p.threeSum(nums)