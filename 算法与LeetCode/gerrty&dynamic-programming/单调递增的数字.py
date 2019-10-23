class Solution:
    def monotoneIncreasingDigits(self, N):
        num = str(N)
        num = self.min_list(num)
        if num[0] == '0':
            num = num[1:]
        return num

    def min_list(self, l):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                return self.min_list(str(int(''.join(l[:i+1]))-1)) + (len(l)-i-1)*'9'
        return l


if __name__ == '__main__':
    s = Solution()
    print(s.monotoneIncreasingDigits(10))