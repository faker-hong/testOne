import numpy as np
class KMP:
    '''
        KMP算法匹配字符串：
            kmp(pat)方法： 先将pat进行处理，遇到什么字符，所转变的状态
            match(txt)方法： 如果txt中匹配上pat，返回匹配上的第一个字符的索引， 匹配不上返回-1
    '''
    def kmp(self, pat):
        self.pat = pat
        m = len(pat)

        # ASCII 码为256， 共有m个状态
        self.dp = [[0] * 256 for _ in range(m)]

        # base case
        self.dp[0][ord(pat[0])] = 1

        # 影子状态
        x = 0

        for i in range(1, m):
            for j in range(256):
                if ord(pat[i]) == j:
                    self.dp[i][j] = i + 1
                else:
                    self.dp[i][j] = self.dp[x][j]

            # 更新影子状态
            x = self.dp[x][ord(pat[i])]

    def match(self, txt):
        m = len(self.pat)
        n = len(txt)

        # pat的初始状态为0
        start = 0

        for i in range(n):
            start = self.dp[start][ord(txt[i])]
            if start == m:
                return i - m + 1

        return -1


if __name__ == '__main__':
    pat = 'abc'
    txt = 'abbc'
    kmp = KMP()
    kmp.kmp(pat)
    print(res)


