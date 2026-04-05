# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        global variable output
        recrusive, carry largest int,
        if largest int smaller, replace, += 1 to output
        '''
        self.output = 0
        def findGood(root, largestValue):
            if root:
                if root.val >= largestValue:
                    self.output += 1
                findGood(root.left, max(largestValue, root.val))
                findGood(root.right, max(largestValue, root.val))
            return
        findGood(root, float('-inf'))
        return self.output
