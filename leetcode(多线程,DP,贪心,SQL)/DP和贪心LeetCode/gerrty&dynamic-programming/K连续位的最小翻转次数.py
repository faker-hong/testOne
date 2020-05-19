class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        '''
        此方法超出时间限制
        n = len(A)
        count = 0
        for i in range(n):
            # 如果出现0就翻转
            if A[i] == 0:
                # 如果出现0的位置，子数组长度小于K，说明无法翻转成功
                if i + K > n:
                    return -1
                for i in range(i, i+K):
                    A[i] ^= 1
                count += 1
        return count
        '''
        q, res, n = list(), 0, len(A)
        for i, a in enumerate(A):
            if q and q[0] + K == i:
                q.pop(0)

            # 判断len(q) + a的奇偶性
            if (len(q) + a) & 1 == 0:
                if i > n - K:
                    return -1
                q.append(i)
                res += 1

        return res


if __name__ == '__main__':
    s = Solution()
    A = [0, 0, 0, 1, 0, 1, 1, 0]
    K = 3
    re = s.minKBitFlips(A, K)
    print(re)