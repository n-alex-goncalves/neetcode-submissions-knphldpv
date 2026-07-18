# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.lst = []
        def preorderTraversal(root):
            if root:
                self.lst.extend([str(root.val), '|'])
                preorderTraversal(root.left)
                preorderTraversal(root.right)
            else:
                self.lst.append('N|')
        preorderTraversal(root)
        return ''.join(self.lst)
 
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.lst = data.split('|')[:-1]
        # ['1', '2', 'N', 'N', '3', '4', 'N', 'N', '5', 'N', 'N']
        # recurisve

        def dfs():
            if self.lst:
                val = self.lst.pop(0)
                if val == 'N':
                    return None
                root = TreeNode(val=val)
                root.left = dfs()
                root.right = dfs()
                return root
            return None

        return dfs()
            # build tree
            # left dfs
            # if it stops return
            # right dfs
            # if it stops return

            # if it stops return

            

