import functools


class Solution(object):
    # dfs解法
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        target = stones[-1]

        @functools.lru_cache(None)
        def dfs(pos, jump):
            if pos == target:
                return True

            for j in [jump-1, jump, jump+1]:
                if j and pos + j in stones and dfs(pos+j, j):
                    return True

            return False

        return dfs(0, 0)

    # DP解法
    def _canCross(self, stones):
        n, s = len(stones), set(stones)
        dp = [set() for _ in range(n)]
        dp[0].add(0)

        # dp[i]是否可以通过dp[j]位置跳need步到达，如果可以则添加步数进去，最后判断最后一个石头的set中是否有数字即可
        for i in range(n):
            cur = stones[i]
            for j in range(i):
                need = cur - stones[j]
                if need - 1 in dp[j] or need + 1 in dp[j] or need in dp[j]:
                    dp[i].add(need)

        return len(dp[-1]) > 0


if __name__ == '__main__':
    s = Solution()
    s.canCross()