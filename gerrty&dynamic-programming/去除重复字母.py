"""
    可以排序的情况下
"""
def removeDuplicateLetters(s):
    """
    :type s: str
    :rtype: str
    """
    letters = sorted(list(s))
    result = []
    compare = ''
    for i in range(len(letters)):
        if letters[i] == compare:
            continue
        else:
            compare = letters[i]
            result.append(compare)
    return ''.join(result)



"""
    不能排序的情况下
"""
def removeDuplicateLetters_two(s):
    if not s:
        return ""
    dict = []
    for i in range(len(s)):
        if s[i] in dict:
            continue
        else:
            compare = s[i]
            dict.append(compare)

    a = dict[0]
    index = 0
    for i in range(len(dict)):
        if dict[i] < a:
            a = dict[i]
            index = i

    dict1 = dict[index:]
    dict2 = dict[:index]
    dict3 = dict1+dict2
    return ''.join(dict3)



if __name__ == '__main__':
    a = "bcabc"
    # print(removeDuplicateLetters(a))
    print(removeDuplicateLetters_two(a))