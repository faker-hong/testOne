import collections


class Solution(object):
    def trulyMostPopular(self, names, synonyms):
        """
        :type names: List[str]
        :type synonyms: List[str]
        :rtype: List[str]
        """
        p, d, q = {}, {}, collections.defaultdict(int)
        for s in synonyms:
            a, b = s[1: -1].split(',')
            pa, pb = p.setdefault(a, [a]), p.setdefault(b, [b])
            if pa is not pb:  # 并查集基操，对数组引用进行合并
                pa.extend(pb)
                for c in pb:
                    p[c] = pa
        for name in p:
            d.setdefault(id(p[name]), min(p[name]))  # 取字典序最小名
        # print(p)
        # print(d)
        for s in names:
            i = s.find('(')
            name, count = s[: i], int(s[i + 1: -1])
            q[name in p and d[id(p[name])] or name] += count  # 未合并过的name单独计数
        # print(q)
        return [f'{name}({count})'.format(name, count) for name, count in q.items()]


if __name__ == '__main__':
    names = ["John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"]
    synonyms = ["(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"]
    s = Solution()
    s.trulyMostPopular(names, synonyms)