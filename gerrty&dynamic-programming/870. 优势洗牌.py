'''
给定两个大小相等的数组 A 和 B，A 相对于 B 的优势可以用满足 A[i] > B[i] 的索引 i 的数目来描述。
返回 A 的任意排列，使其相对于 B 的优势最大化。

题解：
先将A，B升序排序，然后遍历B中每个元素，如果A的最小值比当前值大，则放在这个元素对应的位置，否则，放到最后。
'''

class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A.sort()
        B = [(B[i], i) for i in range(len(B))]
        B.sort()
        i = 0
        j = len(B)-1
        a = 0
        ans = [0] * len(B)
        while i <= j:
            if A[a] > B[i][0]:
                ans[B[i][1]] = A[a]
                i += 1
            else:
                ans[B[j][1]] = A[a]
                j -= 1
            a += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    A = [2, 7, 11, 15]
    B = [1, 10, 4, 11]
    re = s.advantageCount(A, B)
    print(re)