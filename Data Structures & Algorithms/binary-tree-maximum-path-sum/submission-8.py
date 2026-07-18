# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        recursive
        global value
        
        self.maxPath = max(l, r, l + r + me)

        return max(l + me, r + me)
        '''
        self.maxPath = root.val

        def findMaxPath(root):
            if root:
                l = findMaxPath(root.left)
                r = findMaxPath(root.right)

                self.maxPath = max(
                    self.maxPath,
                    l + root.val,
                    r + root.val,
                    l + r + root.val,
                    root.val
                )

                return max(
                    l + root.val,
                    r + root.val,
                    root.val
                )

            return 0

        findMaxPath(root)
        return self.maxPath

        