class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        假设n个节点存在二叉排序树的个数是G(n)，令f(i)为以i为根的二叉搜索树的个数，则
        G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)
        
        当i为根节点时，其左子树节点个数为i-1个，右子树节点为n-i，则
        f(i) = G(i-1)*G(n-i)
        
        综合两个公式可以得到 卡特兰数 公式
        G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)
         '''
        dp = [0]*(n+1)
        # 只有0或1个数的情况下，只有一种排列组合方式
        dp[0] = 1
        dp[1] = 1
        # 长度为i，j位置为根节点位置，左子树节点为j-1个，右子树为i-j个，排列组合有(j-1)(i-j)种
        for i in range(2, n+1):
            for j in range(i+1):
                dp[i] += dp[j-1]*dp[i-j]

        return dp[n]


if __name__ == '__main__':
    s =Solution()
    re = s.numTrees(10)
    print(re)