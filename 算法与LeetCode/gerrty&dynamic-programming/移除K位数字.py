def removeKdigits(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    if len(num) <= k:
        return '0'
    if k == 0:
        return num
    stack, count = [], 0
    # 对于字符串里的每一个元素
    for i, x in enumerate(num):
        # 如果栈顶元素比待入栈元素要大，则删除栈顶元素，同时将待入栈元素push, count加1
        while len(stack) > 0 and x < stack[-1]:
            stack.pop()
            count += 1
            # 若入栈的元素已经为k
            if count == k:
                # 一般情况下，经过贪心算法的已经入栈的元素+num中未处理的元素
                # 当有前导0时，由于先转为int,前导0消失，然后转为str类型，这就解决了前导0的问题
                return str(int(''.join(stack) + num[i:]))
        stack.append(x)
    # 特殊情况下一直是升序，如123456，则只返回前len(num)-k个数
    return str(int(''.join(stack[:len(num) - k])))


if __name__ == '__main__':
    print(removeKdigits('5337', 2))