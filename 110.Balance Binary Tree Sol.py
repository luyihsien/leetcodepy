class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        _, isB = self.getHeight(root)
        return isB

    def getHeight(self, root):
        if not root:
            return 0, True
        lH, lB = self.getHeight(root.left)
        rH, rB = self.getHeight(root.right)
        return max(lH, rH) + 1, abs(lH - rH) <= 1 and lB and rB


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def backtracking(root):
            if not root:
                return 1
            left = backtracking(root.left)
            if not left:
                return 0
            right = backtracking(root.right)
            if not right:
                return 0
            return max(left, right) + 1 if abs(left - right) <= 1 else 0

        if not root:
            return True
        return True if backtracking(root) else False
