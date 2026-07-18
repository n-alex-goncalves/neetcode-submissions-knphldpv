# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = [1,2,3,4], inorder = [2,1,3,4]
        '''
        pop preorder
        find in inorder
        split into two functions (recursive buildTree)
        then return answer
        '''
        if not preorder and not inorder:
            return None

        val = preorder.pop(0)
        index = inorder.index(val)

        leftInorder = inorder[:index]
        rightInorder = inorder[index + 1:]

        leftPreorder = preorder[:index]
        rightPreorder = preorder[index:]

        return TreeNode(
            val=val,
            left=self.buildTree(leftPreorder, leftInorder),
            right=self.buildTree(rightPreorder, rightInorder)
        )