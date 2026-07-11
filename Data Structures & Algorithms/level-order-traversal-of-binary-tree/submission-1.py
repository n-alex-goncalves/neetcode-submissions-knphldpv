# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dictionary = collections.defaultdict(list)
        self.depth = 0
        def findDepth(root):
            if root:
                self.depth += 1
                dictionary[self.depth].append(root.val)
                findDepth(root.left)
                findDepth(root.right)
                self.depth -= 1
        findDepth(root)
        return list(dictionary.values())