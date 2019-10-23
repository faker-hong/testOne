class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        re = ["0"]
        for index, c in enumerate(s):
            if c not in re:
                while c < re[-1] and s[index:].count(re[-1]) > 0:
                    re.pop()
                re.append(c)
        return ''.join(re[1:])


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicateLetters("bcabc"))