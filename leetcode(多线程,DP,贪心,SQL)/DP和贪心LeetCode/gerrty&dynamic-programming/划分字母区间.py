def partitionLabels(S):
    """
    :type S: str
    :rtype: List[int]
    解法：   1.先利用map将字符对应的最后出现位置储存下来
            2.遍历S,把字符出现最后的位置赋给cur，如果遍历到cur还是没有更新，那说明后面没有重复的字符了
    """
    mapIter = {}
    for i, s in enumerate(S):
        mapIter[s] = i

    cur = mapIter[S[0]]
    res = []
    for i, s in enumerate(S):
        if mapIter[s] > cur:
            cur = mapIter[s]
        if i == cur:
            res.append(i+1-sum(res))
    return res


if __name__ == '__main__':
    print(partitionLabels('abcabcdef'))