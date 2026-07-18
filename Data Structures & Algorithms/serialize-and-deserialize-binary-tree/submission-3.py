# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.code = []

        def preorderSerialize(root):
            if root:
                self.code.extend([str(root.val), '+', str(hash(root)), '|'])
                preorderSerialize(root.left)
                preorderSerialize(root.right)

        def inorderSerialize(root):
            if root:
                inorderSerialize(root.left)
                self.code.extend([str(root.val), '+', str(hash(root)), '|'])
                inorderSerialize(root.right)

        preorderSerialize(root)
        self.code.append('#')
        inorderSerialize(root)

        return ''.join(self.code)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder, inorder = data.split('#')
        preorder, inorder = preorder.split('|')[:-1], inorder.split('|')[:-1]

        preorder = [tuple(x.split('+')) for x in preorder]
        inorder = [tuple(x.split('+')) for x in inorder]

        print(preorder)
        print(inorder)

        def buildTree(preorder, inorder):
            if not preorder and not inorder:
                return None

            val, code = preorder.pop(0)
            index = inorder.index((val, code))

            leftI, leftP = inorder[:index], preorder[:index]
            rightI, rightP = inorder[index + 1:], preorder[index:]

            return TreeNode(
                val=val,
                left=buildTree(leftP, leftI),
                right=buildTree(rightP, rightI)
            )
        
        return buildTree(preorder, inorder)