# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dictionary = collections.defaultdict(list)
        def getDepth(root, depth):
            if root:
                dictionary[depth].append(root.val)
                getDepth(root.left, depth + 1)
                getDepth(root.right, depth + 1)
            return 0
        getDepth(root, 0)
        return list(dictionary.values())
        