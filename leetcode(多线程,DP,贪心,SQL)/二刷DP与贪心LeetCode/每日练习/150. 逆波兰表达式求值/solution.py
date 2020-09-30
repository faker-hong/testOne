class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        n = len(tokens)
        i = 0
        queue = []

        while i < n:
            if tokens[i] not in ['+', '-', '*', '/']:
                queue.append(int(tokens[i]))
            else:
                right = queue.pop()
                left = queue.pop()
                if tokens[i] == '+':
                    queue.append((left + right))
                elif tokens[i] == '-':
                    queue.append((left - right))
                elif tokens[i] == '*':
                    queue.append((left * right))
                elif tokens[i] == '/':
                    queue.append(int(left / right))

            i += 1
        return queue[0]


if __name__ == '__main__':
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    s = Solution()
    s.evalRPN(tokens)