class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def ishui(l):
            i = 0
            j = len(l) - 1
            while i <= j:
                if l[i] != l[j]:
                    return False
                i += 1
                j -= 1
            return True

        res = []

        def helper(l, left, s):
            if left == len(l):
                res.append(s)

            for i in range(left + 1, len(l) + 1):
                if ishui(l[left:i]):
                    helper(l, i, s + [l[left:i]])

        helper(s, 0, [])
        return res