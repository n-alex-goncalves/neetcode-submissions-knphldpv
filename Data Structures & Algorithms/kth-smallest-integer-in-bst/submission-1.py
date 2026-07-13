# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i = 0
        self.ouptut = 0
        def inorderTraversal(root):
            if root and self.i < k:
                inorderTraversal(root.left)
                self.i += 1
                if self.i == k:
                    self.output = root.val
                inorderTraversal(root.right)
        inorderTraversal(root)
        return self.output