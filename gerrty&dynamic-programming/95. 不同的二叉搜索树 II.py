# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generateTrees_trees(start, end):
            if start > end:
                return [None,]

            all_trees = []

            for i in range(start, end+1):
                left_trees = generateTrees_trees(start, i-1)
                right_trees = generateTrees_trees(i+1, end)

                for j in left_trees:
                    for k in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = j
                        current_tree.right = k
                        all_trees.append(current_tree)
            return all_trees

        return generateTrees_trees(1, n) if n else []


if __name__ == '__main__':
    s = Solution()
    re = s.generateTrees(3)
    print(re)
