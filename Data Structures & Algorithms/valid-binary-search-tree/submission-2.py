# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.cur = float('-inf')
        def preorder(root):
            if root:
                l = preorder(root.left)
                if root.val <= self.cur:
                    return False
                self.cur = root.val
                r = preorder(root.right)
                return l and r
            return True
        return preorder(root)
