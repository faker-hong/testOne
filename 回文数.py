class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        a = list(str(x))
        while len(a) > 1:
            while a[0] == a[-1] and len(a) != 1:
                a.pop(0)
                a.pop(-1)
                if len(a) == 1 or len(a) == 0:
                    return True
            else:
                return False
        else:
            return True
                
        