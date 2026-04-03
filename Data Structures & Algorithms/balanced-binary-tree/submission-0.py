# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = True
        def getDepth(root, depth=0):
            if root:
                l = getDepth(root.left, depth) + 1
                r = getDepth(root.right, depth) + 1
                if abs(l - r) > 1:
                    self.balance = False
                return max(l, r)
            return 0
        getDepth(root)
        return self.balance
        
        