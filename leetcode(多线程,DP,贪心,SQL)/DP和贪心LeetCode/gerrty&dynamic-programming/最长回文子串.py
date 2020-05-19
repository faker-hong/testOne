class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''超出时间限制
        if len(s) <= 1:
            return s
        res = []
        for end in range(1, len(s)+1):
            for start in range(end):
                if s[start:end] == s[start:end][::-1]:
                    res.append((start, end))
        res.sort(key=lambda x:x[1]-x[0])
        re = res[-1]
        return s[re[0]:re[1]]
        '''
        n = len(s)
        self.res = ''

        def find(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            if len(self.res) < j-i-1:
                # 这里的i，j已经做过加减，所以i要+1，j不变
                self.res = s[i+1:j]
        for i in range(n):
            # 区别奇偶性
            find(i, i)
            find(i, i+1)
        return self.res


if __name__ == '__main__':
    s = Solution()
    strs = 'babad'
    re = s.longestPalindrome(strs)
    print(re)