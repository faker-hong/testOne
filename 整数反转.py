class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        count = 0
        while x % 10 > 0:
            count = count*10+x%10
            x = x // 10
        return count
        while x % 10 < 0:
            count = count*10-x%10
            x=  x // 10
        return count
        if x>pow(2,31)-1 or x < pow(-2,31) or x == 0:
            return 0