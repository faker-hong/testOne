class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 超出时间限制
        # if n <= 0:
        #     return 0
        # count = 10**n
        # for i in range(10, 10**n):
        #     if len(str(i)) != len(set(str(i))):
        #         count -= 1
        # return count

        # n = 1: res = 10
        # n = 2: res = 9 * 9 + 10 = 91  # 两位数第一位只能为1-9，第二位只能为非第一位的数，加上一位数的所有结果
        # n = 3: res = 9 * 9 * 8 + 91 = 739  # 三位数第一位只能为1-9，第二位只能为非第一位的数，第三位只能为非前两位的数，加上两位数的所有结果
        # n = 4: res = 9 * 9 * 8 * 7 + 739 = 5275  # 同上推法

        if n <= 0:
            return 1
        res, mule = 10, 9
        for i in range(1, min(n, 10)):
            mule *= 10 -i
            res += mule
        return res


if __name__ == '__main__':
    s =Solution()
    re = s.countNumbersWithUniqueDigits(3)
    print(re)