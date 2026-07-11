# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.lst = []
        def preorderTraversal(root):
            if root:
                preorderTraversal(root.left)
                self.lst.append(root.val)
                preorderTraversal(root.right)
        preorderTraversal(root)
        return sorted(self.lst) == self.lst and len(set(self.lst)) == len(self.lst)
        