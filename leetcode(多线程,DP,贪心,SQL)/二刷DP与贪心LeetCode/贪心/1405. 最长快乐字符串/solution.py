class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        # 获得a,b,c的最小次数
        m = {'a': min(a, 2*(b+c+1)), 'b': min(b, 2*(a+c+1)), 'c': min(c, 2*(a+b+1))}

        # 得到最终字符串的长度
        n = sum(m.values())

        # 结果列表
        res = []

        # 每次插入一个字符
        for i in range(n):
            # 候选的字符
            cand = ['a', 'b', 'c']
            # 如果列表的最后两个字符相同，则将该字符移除候选列表
            if len(res) > 1 and res[-1] == res[-2]:
                cand.remove(res[-1])

            # 贪心，在候选中选择数量最大的
            tmp = max(cand, key=lambda x: m[x])
            res.append(tmp)
            m[tmp] -= 1

        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    res = s.longestDiverseString(1, 1, 7)
    print(res)