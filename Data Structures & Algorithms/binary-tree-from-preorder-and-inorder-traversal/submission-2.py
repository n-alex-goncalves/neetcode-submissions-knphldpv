# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        preorder everything to the left, everything to the right
        pop inorder
        left till i ereach mine
        then right till i reach mine
        recursive
        '''
        if preorder:
            val = preorder.pop(0)

            i = inorder.index(val)

            l = self.buildTree(preorder[:i], inorder[:i])
            r = self.buildTree(preorder[i:], inorder[i+1:])

            return TreeNode(val, l, r)
        return None
        