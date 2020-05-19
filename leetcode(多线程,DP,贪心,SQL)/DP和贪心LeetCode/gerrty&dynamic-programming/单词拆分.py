def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    wordDict = set(wordDict)
    dp = [False]*(len(s)+1)
    dp[0] = True
    for i in range(1, len(s)+1):
        for j in range(0, i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    print(dp)
    return dp[len(s)]

if __name__ == '__main__':
    print(wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"]))