# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
a = 1
v = 0


class Solution:
    global a
    global v

    def maximumAverageSubtree(self, root) -> float:
        if not root.left and not root.right:
            return root.val
        elif root.left and not root.right:
            v += root.val
            a += 1
            v += self.maximumAverageSubtree(root.left)

        elif not root.left and root.right:
            v += root.val
            a += 1
            v += self.maximumAverageSubtree(root.right)
        elif root.left and root.right:
            v += root.val
            a += 2
            v += self.maximumAverageSubtree(root.right) + self.maximumAverageSubtree(root.left)