class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        import heapq
        dp = [i for i in zip(Capital, Profits)]
        dp.sort()
        heap = []
        n = len(dp)
        i = 0
        while k:
            while i < n and dp[i][0] <= W:
                heapq.heappush(heap, -dp[i][1])
                i += 1
            if heap:
                W -= heapq.heappop(heap)
            k -= 1
        return W


if __name__ == '__main__':
    s = Solution()
    k = 2
    W = 0
    Profits = [1, 2, 3]
    Capital = [0, 1, 1]
    s.findMaximizedCapital(k, W, Profits, Capital)