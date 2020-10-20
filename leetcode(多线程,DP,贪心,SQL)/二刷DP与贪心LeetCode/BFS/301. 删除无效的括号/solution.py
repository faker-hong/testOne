class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 判断字符串是否有效
        def is_valid(s):
            cnt = 0

            for i in range(len(s)):
                if s[i] == '(':
                    cnt += 1
                elif s[i] == ')':
                    cnt -= 1

                if cnt < 0:
                    return False

            return cnt == 0

        check = {s}

        # 逐层往下检查，每次多删去一个char in '()'
        while True:
            res = list(filter(is_valid, check))
            if res:
                return res

            check = {c[:i] + c[i+1:] for c in check for i in range(len(c)) if c[i] in '()'}


if __name__ == '__main__':
    s = Solution()
    res = s.removeInvalidParentheses("(a)())()")
    print(res)