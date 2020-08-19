class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        f = [0 for _ in range(N + 1)]
        f[0] = 1
        P = 10 ** 9 + 7
        for i in range(N + 1):
            cnt = self.getCnt(s[i - 1])
            f[i] += cnt * f[i - 1]
            if i > 1:
                cnt = self.getCnt2(s[i - 2], s[i - 1])
                f[i] += cnt * f[i - 2]

        return f[N] % P

    def getCnt(self, c):
        if c == '0':
            return 0
        elif c == '*':
            return 9
        else:
            return 1

    def getCnt2(self, c1, c2):
        if c1 == '0' or '3' <= c1 <= '9':
            return 0
        elif c1 == '1':
            if c2 == '*':
                return 9
            else:
                return 1
        elif c1 == '2':
            if c2 == '*':
                return 6
            elif '0' <= c2 <= '6':
                return 1
            else:
                return 0
        elif c1 == '*':
            if c2 == '*':
                return 15
            elif '0' <= c2 <= '6':
                return 2
            else:
                return 1

        return 0