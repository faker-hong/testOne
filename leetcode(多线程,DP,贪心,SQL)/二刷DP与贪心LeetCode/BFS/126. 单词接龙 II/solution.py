from collections import defaultdict


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # beginWord 和endWord 非空
        if endWord not in wordList or not wordList:
            return []

        n = len(beginWord)
        match = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                match[word[:i] + '*' + word[i+1:]].append(word)

        queue = [(beginWord, [beginWord])]
        visit = {beginWord: True}
        res = []

        while queue:
            next_layer = []
            for i in range(len(queue)):
                word, path = queue.pop(0)
                if word == endWord:
                    res.append(path)
                visit[word] = True
                for i in range(n):
                    for next_word in match[word[:i] + '*' + word[i+1:]]:
                        if next_word not in visit:
                            next_layer.append((next_word, path + [next_word]))
            queue = next_layer
            if res:
                return res

        return res


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    s = Solution()
    res = s.findLadders(beginWord, endWord, wordList)
    print(res)