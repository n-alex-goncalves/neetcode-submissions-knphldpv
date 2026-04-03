# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.lst = []
        def preorder(root):
            if root:
                preorder(root.left)
                self.lst.append(root.val)
                preorder(root.right)
        preorder(root)
        return self.lst == sorted(set(self.lst))
