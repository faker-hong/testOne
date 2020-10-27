class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 滑动窗口
        if not s:
            return 0

        left = 0
        lookup = set()
        n = len(s)
        max_len, cur_len = 0, 0

        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])

        return max_len


if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLongestSubstring("abcabcbb")
    print(res)