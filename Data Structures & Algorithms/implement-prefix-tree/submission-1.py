class PrefixTree:

    def __init__(self):
        self.children = {}
        

    def insert(self, word: str) -> None:
        if word:
            if word[0] not in self.children:
                self.children[word[0]] = PrefixTree()
            self.children[word[0]].insert(word[1:])
            return
        self.children['.'] = '.'


    def search(self, word: str) -> bool:
        if word:
            if word[0] not in self.children:
                return False
            return self.children[word[0]].search(word[1:])
        return '.' in self.children
        

    def startsWith(self, prefix: str) -> bool:
        if prefix:
            if prefix[0] not in self.children:
                return False
            return self.children[prefix[0]].startsWith(prefix[1:])
        return True
        
        