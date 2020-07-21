from collections import defaultdict


class Solution:
    def __init__(self):
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, other_visited):
        cur_word, level = queue.pop(0)

        for i in range(self.length):
            common_word = cur_word[:i] + '*' + cur_word[i+1:]

            for word in self.all_combo_dict[common_word]:
                if word in other_visited:
                    return level + other_visited[word]

                if word not in visited:
                    visited[word] = level + 1
                    queue.append((word, level + 1))

        return None

    def ladderLength(self, beginWord, endWord, wordList):
        # 判断参数是否为空， 最终结果是否存在wordList
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0

        # 所有单词的长度相同
        self.length = len(beginWord)

        # 定义通用单词字典
        for word in wordList:
            for i in range(self.length):
                self.all_combo_dict[word[:i] + '*' + word[i+1:]].append(word)

        # 以beginWord和endWord开始搜索的队列
        queue_begin = [(beginWord, 1)]
        queue_end = [(endWord, 1)]

        # 以beginWord和endWord开始的visit记录表
        visit_begin = {beginWord: True}
        visit_end = {endWord: True}
        ans = None

        while queue_begin and queue_end:
            ans = self.visitWordNode(queue_begin, visit_begin, visit_end)

            if ans:
                return ans

            ans = self.visitWordNode(queue_end, visit_end, visit_begin)

            if ans:
                return ans

        return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    s = Solution()
    res = s.ladderLength(beginWord, endWord, wordList)
    print(res)