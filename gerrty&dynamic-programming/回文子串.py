"""
    从中间向两边扩张判断是否回文
"""


class Solution(object):
    def __init__(self):
        self.sum = 0

    def countSubstrings(self, s):
        for i in range(len(s)):
            self.count(s, i, i)  # s为奇数
            self.count(s, i, i + 1)  # s为偶数
        return self.sum

    def count(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            self.sum += 1
            start -= 1
            end += 1


if __name__ == '__main__':
    s = Solution()
    a = s.countSubstrings('aaa')
    print(a)
