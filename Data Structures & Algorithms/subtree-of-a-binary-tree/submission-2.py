# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSametree(self, p, q):
        if p and q:
            if p.val == q.val:
                return self.isSametree(p.left, q.left) and self.isSametree(p.right, q.right)
            return False

        if p or q:
            return False

        return True
   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root:
            if self.isSametree(root, subRoot):
                return True
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False

        