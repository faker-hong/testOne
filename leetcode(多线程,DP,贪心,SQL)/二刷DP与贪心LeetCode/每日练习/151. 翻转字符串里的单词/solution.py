class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        word_list = s.split()
        word_list = word_list[::-1]
        res = ' '

        return res.join(word_list)


if __name__ == '__main__':
    s = Solution()
    s.reverseWords("a good   example")