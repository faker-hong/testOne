def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    """
    超出时间限制
    dp = [-1]*(len(s)+1)
    dp[0] = 0
    s = '0' + s
    for i in range(1,len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i] = dp[i-1] + j
                t = t[j:]
            else:
                continue
            break
    return dp == sorted(dp)
    """

    i = 0
    for char in s:
        j = t.find(char, i)
        if j == -1:
            return False
        i = j+1
    return True



if __name__ == '__main__':
    s = "acb"
    t = "ahbgdc"
    print(isSubsequence(s,t))