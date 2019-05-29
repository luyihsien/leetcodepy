class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
TreeNode(0)
print(TreeNode(0))
if None:
    print(1)
else:
    print(0)



class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False
            return check(node1.left, node2.right) and check(node1.right, node2.left)

        return check(root, root)
