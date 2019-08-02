def findContentChildren(g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    if len(s) == 0:
        return 0
    g = sorted(g)
    s = sorted(s)
    sum_s = s[0]
    g_point = 0
    s_point = 0
    happy = 0
    while True:
        if g[g_point] <= s[s_point]:
            happy += 1
            g_point += 1
            s_point += 1
            if g_point == len(g) or s_point == len(s):
                return happy
            # sum_s = s[s_point]

        else:
            # sum_s = s[s_point]
            s_point += 1
            if g_point == len(g) or s_point == len(s):
                return happy
            # sum_s += s[s_point]

    return happy


if __name__ == '__main__':
    g=[3]
    s=[1, 2]
    print(findContentChildren(g, s))        # 这种情况下，应该是有一个小朋友满足。但结果为0