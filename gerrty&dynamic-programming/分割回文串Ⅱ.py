class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0
        # 维护一个record，最多需要分割len(s)-1次
        record = [i for i in range(-1, len(s))]
        for end in range(1, len(s)+1):
            for start in range(end):
                # 是否是回文
                if s[start:end] == s[start:end][::-1]:
                    # 更新record，并于当前的值与record[start]+1取较小值
                    record[end] = min(record[end], record[start] + 1)
        return record[-1]


if __name__ == '__main__':
    s = Solution()
    S = 'aabcb'
    re = s.minCut(S)
    print(re)