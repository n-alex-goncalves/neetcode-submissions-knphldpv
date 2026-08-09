class TreeNode:

    def __init__(self, val=None):
        self.val = val
        self.neighbours = dict()


class WordDictionary:

    def __init__(self):
        self.root = TreeNode('/')
        
    def addWord(self, word: str) -> None:
        node = self.root
        i = 0
        while i < len(word) and word[i] in node.neighbours:
            node = node.neighbours[word[i]]
            i += 1
        
        while i < len(word):
            newNode = TreeNode(word[i])
            node.neighbours[word[i]] = newNode
            node = newNode
            i += 1
        
        node.neighbours['/'] = TreeNode()
        return
        

    def search(self, word: str, head=None) -> bool:
        node = head if head else self.root
        for i in range(len(word)):
            character = word[i]
            if character in node.neighbours:
                node = node.neighbours[character]
            elif character == '.':
                return any([self.search(word[i + 1:], n) for n in node.neighbours.values()])
            else:
                return False
        
        return '/' in node.neighbours
        
