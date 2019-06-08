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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sym(self, left_node, right_node):
        if not left_node and not right_node:
            return True
        if not left_node or not right_node:
            return False
        if left_node.val != right_node.val:
            return False
        return self.sym(left_node.left, right_node.right) and self.sym(left_node.right, right_node.left)

    def isSymmetric(self, root):
        return self.sym(root, root)
'''
成功
显示详情 
执行用时 : 52 ms, 在Symmetric Tree的Python3提交中击败了92.83% 的用户
内存消耗 : 13 MB, 在Symmetric Tree的Python3提交中击败了95.52% 的用户

'''