def longestRalindrome(s):
    l = len(s)
    max_length = 0
    palindromic = ''
    if len(s) == 1:
        return s
    for i in range(l):
        for j in range(i + 1, l):
            is_palindromic = True
            for k in range(i, int((i + j) / 2) + 1):
                if s[k] != s[j - k + i]:
                    is_palindromic = False
                    break
            if is_palindromic and (j - i + 1) > max_length:
                max_length = j - i + 1
                palindromic = s[i:j + 1]
    if palindromic == '':
        palindromic = s[0]
    return palindromic


if __name__ == '__main__':
    # s = "bcaab"
    # print(s[1:4])
    # print(longestRalindrome(s))
    print(ord('z'))