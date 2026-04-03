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
        def preorder(root):
            if root:
                self.lst.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
                return
            self.lst.append('#')
        preorder(root)
        return '|'.join(self.lst)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.lst = data.split('|')
        def dfs():
            if self.lst:
                cur = self.lst.pop(0)

                if cur == '#':
                    return None

                l = dfs()
                r = dfs()
                return TreeNode(int(cur), l, r)
            return None
        return dfs()
