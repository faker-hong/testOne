class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(1, num+1):
            if i % 2 == 0:
                res.append(res[i//2])
            else:
                res.append(res[i-1] + 1)
        return res