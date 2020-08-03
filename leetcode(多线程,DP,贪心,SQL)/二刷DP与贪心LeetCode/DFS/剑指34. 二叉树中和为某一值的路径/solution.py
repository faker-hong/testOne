class Solution(object):
    def pathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # 储存最终结果和能成功的路径
        res = []
        path = []

        def helper(root, tar):
            if not root:
                return
            
            path.append(root.val)

            tar -= root.val

            if tar == 0 and not root.left and not root.right:
                res.append(list(path))

            helper(root.left, tar)
            helper(root.right, tar)
            path.pop(0)

        helper(root, sum_)
        return res