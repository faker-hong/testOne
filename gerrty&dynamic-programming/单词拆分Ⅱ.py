class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if len(s) == 0 or len(wordDict) == 0:
            return []
        word_set = {word for word in wordDict}
        dp = [False for _ in range(len(s))]
        dp[0] = s[0] in word_set

        for i in range(1, len(s)):
            # 如果整个单词就直接在 word_set 中，直接返回就好了
            # 否则把单词做分割，挨个去判断
            if s[:i + 1] in word_set:
                dp[i] = True
                continue
            for j in range(i):
                if dp[j] and s[j + 1: i + 1] in word_set:
                    dp[i] = True
                    break

        split_s = []

        # 从尾往首遍历
        def dfs(end=len(s), sub_str_list=[]):
            # 如果最后切分的单词刚好就在字典中，那可以直接取出结果了
            if s[:end] in word_set:
                sub_str_list.append(s[:end])
                # 这儿注意，因为sub_str_list添加的子串都是从s的右边往左边添加的
                # 因为后面有个pop（）操作，所以这儿得先复制
                sub_str_copy = sub_str_list[:]
                sub_str_copy.reverse()
                new_str = " ".join(sub_str_copy)
                split_s.append(new_str)
                sub_str_list.pop()
            for start in range(end - 1, -1, -1):
                # 此处刚好对应状态转移方程2
                if dp[start] and (s[start + 1:end] in word_set):
                    dfs(start + 1, sub_str_list + [s[start + 1:end]])

        dfs()
        return split_s


if __name__ == '__main__':
    S = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    re = S.wordBreak(s, wordDict)
    print(re)