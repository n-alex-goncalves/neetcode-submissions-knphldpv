# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = 0
        def test(root, depth):
            if root:
                self.maxDepth = max(self.maxDepth, depth)
                l, r = 0, 0
                if root.left:
                    l = test(root.left, depth + 1)
                if root.right:
                    r = test(root.right, depth + 1)
                return max(l, r)
            return 0
        test(root, 1)
        return self.maxDepth

        