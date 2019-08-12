def minAddToMakeValid(S):
    """
    :type S: str
    :rtype: int
    """
    if not S:
        return 0
    if len(S) == 1:
        return 1
    stack = []
    for i in range(len(S)):
        if len(stack) == 0:
            stack.append(S[i])
            continue
        if stack[-1]+S[i] == '()':
            stack.pop()
        else:
            stack.append(S[i])
    return len(stack)

if __name__ == '__main__':
    print(minAddToMakeValid("((("))