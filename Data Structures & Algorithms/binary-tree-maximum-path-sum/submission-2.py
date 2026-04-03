# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        self.cur = 0
        '''
        self.cur = float('-inf')
        def pathSum(root):
            if root:
                l = pathSum(root.left)
                r = pathSum(root.right)
                self.cur = max([
                    self.cur,
                    l,
                    r,
                    l + r + root.val, 
                    root.val,
                    l + root.val,
                    r + root.val
                ])
                return max([root.val + l, root.val + r, root.val])
            return float('-inf')
        pathSum(root)
        return self.cur
        