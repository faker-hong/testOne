class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i = 0
        j = len(people)-1
        time = 0
        while True:
            time += 1
            if people[i] + people[j] <= limit:
                i -= 1
            if i == j:
                time += 1
                return time
            elif i > j:
                return time


if __name__ == '__main__':
    s = Solution()
    people = [3,5,3,4]
    limit = 5
    print(s.numRescueBoats(people, limit))