from collections import defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0

        n = len(wordList)
        all_combo_dict = defaultdict(list)

        for word in wordList:
            for i in range(n):
                all_combo_dict[word[:i] + '*' + word[i+1:]].append(word)

        queue = [(beginWord, 1)]

        visited = {beginWord: True}

        while queue:
            cur_word, times = queue.pop(0)

            for i in range(n):
                common_word = cur_word[:i] + '*' + cur_word[i+1:]

                for word in all_combo_dict[common_word]:
                    if word == endWord:
                        return times + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, times + 1))

                all_combo_dict[common_word] = []

        return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    s = Solution()
    res = s.ladderLength(beginWord, endWord, wordList)
    print(res)