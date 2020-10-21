class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        n = len(name)
        m = len(typed)

        i, j = 0, 0

        if name[i] != typed[j]:
            return False

        while i < n and j < m:
            # 字符相等
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                # 字符不相等  与name前一个字符比较
                if typed[j] == name[i-1]:
                    j += 1
                else:
                    return False

        if i == n and j == m:
            return True

        # 如果i还未到n，说明name后面还有字符，返回False
        if i < n:
            return False

        # 如果j还未到m，判断typed后面的字符是否等于name最后一个字符
        if j < m:
            if ''.join(set(typed[j:])) == typed[j]:
                return True
            return False