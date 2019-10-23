class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generate( n, n, '', res)
        return res

    def generate(self, left, right, s, res):
        if left == 0 and right == 0:
            res.append(s)
            return
        if left > 0:
            self.generate(left-1, right, s + '(', res)
        if right > left:
            self.generate(left, right-1, s + ')', res)