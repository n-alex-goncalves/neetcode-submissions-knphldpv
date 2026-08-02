class TreeNode:

    def __init__(self, val='.'):
        self.val = val
        self.neighbours = dict()

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        '''
        while character exists: continue
        start adding character by character
        once word ends, add a .
        '''
        cur = self.root
        word = list(word)
        while word and word[0] in cur.neighbours:
            character = word.pop(0)
            cur = cur.neighbours[character]
        
        for character in word:
            newNode = TreeNode(character)
            cur.neighbours[character] = newNode
            cur = newNode
        
        cur.neighbours['.'] = '.'


    def search(self, word: str) -> bool:
        '''
        while character exists: continue
        if character does not exist and terminate exists: return true
        return false
        '''
        cur = self.root
        word = list(word)
        while word and word[0] in cur.neighbours:
            character = word.pop(0)
            cur = cur.neighbours[character]
        
        if not word and '.' in cur.neighbours:
            return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        '''
        while character exists: conintue
        if character does not exist: return True
        return fasle
        '''
        cur = self.root
        word = list(prefix)
        while word and word[0] in cur.neighbours:
            character = word.pop(0)
            cur = cur.neighbours[character]
        
        if not word:
            return True
        
        return False

        
        