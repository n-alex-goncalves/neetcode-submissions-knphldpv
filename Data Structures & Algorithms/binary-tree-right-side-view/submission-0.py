# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        naive, could use depth
        O(n) space, where space is vertical?
        Should be fine
        '''
        dictionary = dict()
        def getDepth(root, depth):
            if root:
                dictionary[depth] = root.val
                getDepth(root.left, depth + 1)
                getDepth(root.right, depth + 1)
            return
        getDepth(root, 0)
        return list(dictionary.values())

        