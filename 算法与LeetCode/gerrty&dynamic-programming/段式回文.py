class Solution:
    def longestDecomposition(self, text: str) -> int:
        length = len(text)
        str1 = ""
        str2 = ""
        re = 0
        i = 0
        j = length-1
        while i < j:
            str1 = str1 + text[i]
            str2 = text[j] + str2
            if str1 == str2:
                re += 2
                str1 = ""
                str2 = ""
            i += 1
            j -= 1
        if length % 2 == 1 or str1 != "":
            re += 1
        return re


if __name__ == '__main__':
    print(Solution().longestDecomposition("antaprezatepzapreanta"))