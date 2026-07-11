# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        self.maxDepth = 0

        def depth(root):
            if root:
                self.depth += 1
                self.maxDepth = max(self.maxDepth, self.depth)

                depth(root.left)
                depth(root.right)
                
                self.depth -= 1
        
        depth(root)
        return self.maxDepth