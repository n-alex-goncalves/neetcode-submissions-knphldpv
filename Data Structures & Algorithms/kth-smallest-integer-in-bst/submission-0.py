# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cur = float('-inf')
        self.k = k
        def preorder(root):
            if root:
                preorder(root.left)
                if self.k <= 0:
                    return self.cur
                self.cur = root.val
                self.k -= 1
                return preorder(root.right)
            return self.cur
        return preorder(root)
        