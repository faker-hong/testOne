class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        n = len(S)
        m = len(T)

        stack1 = []
        stack2 = []

        for i in range(n):
            if S[i] == '#':
                if stack1:
                    stack1.pop()
                else:
                    continue
            else:
                stack1.append(S[i])

        for i in range(m):
            if T[i] == '#':
                if stack2:
                    stack2.pop()
                else:
                    continue
            else:
                stack2.append(T[i])

        return stack1 == stack2