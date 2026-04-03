# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.cur = float('-inf')
        
        def dfs(root):
            if root:

                l = max(0, dfs(root.left))
                r = max(0, dfs(root.right))

                self.cur = max(self.cur, root.val + l + r)

                return root.val + max(l, r)
            return float('-inf')
        
        dfs(root)
        return self.cur

        