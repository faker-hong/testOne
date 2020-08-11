class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        n = len(S)
        res = []

        def helper(i, s):
            if i == n:
                res.append(s)
                return
            if s[i].isalpha():
                helper(i + 1, s[:i] + s[i].upper() + s[i+1:])
                helper(i + 1, s[:i] + s[i].lower() + s[i+1:])
            else:
                helper(i + 1, s)

        helper(0, S)
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.letterCasePermutation("a1b1")
    print(res)