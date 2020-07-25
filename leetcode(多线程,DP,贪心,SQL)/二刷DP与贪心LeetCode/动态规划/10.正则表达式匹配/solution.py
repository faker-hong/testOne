class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = dict()   # 备忘录

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            # 第一次匹配
            first_match = i < len(s) and p[j] in (s[i], '.')

            if j <= len(p) - 2 and p[j + 1] == '*':
                # 出现*号，前者为匹配0次，后者为匹配1次
                ans = dp(i, j + 2) or first_match and dp(i + 1, j)
            else:
                ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans

            return ans

        return dp(0, 0)