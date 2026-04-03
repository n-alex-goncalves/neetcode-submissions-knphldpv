# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self, i, j):
        if i and j:
            if i.val == j.val:
                return self.sameTree(i.left, j.left) and self.sameTree(i.right, j.right)
            return False
        if i or j:
            return False    
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:        
        if root:
            if self.sameTree(root, subRoot):
                return True
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False

        
        