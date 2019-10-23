class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        '''利用Counter计算出各个字符的数量，如果数量最多的有两个字符，数量各-1然后再进行排序计算'''
        from collections import Counter
        c = Counter(S)
        if max(c.values()) <= (len(S) + 1) / 2:
            res = ""
            while c:
                out = c.most_common(2)
                if len(out):
                    res += out[0][0]
                    c[out[0][0]] -= 1
                if len(out) > 1:
                    res += out[1][0]
                    c[out[1][0]] -= 1
                c += Counter()      # 重新计数排序
            return res
        return ""


if __name__ == '__main__':
    s = Solution()
    S = "nowpwibfd"
    re = s.reorganizeString(S)
    print(re)