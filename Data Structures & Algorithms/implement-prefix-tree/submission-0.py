class PrefixTree:

    def __init__(self):
        self.child = {}
        

    def insert(self, word: str) -> None:
        if word:
            if word[0] not in self.child:
                self.child[word[0]] = PrefixTree()
            self.child[word[0]].insert(word[1:])
            return
        self.child['.'] = '.'


    def search(self, word: str) -> bool:
        if word:
            if word[0] in self.child:
                return self.child[word[0]].search(word[1:])
            return False
        return '.' in self.child


    def startsWith(self, prefix: str) -> bool:
        if prefix:
            if prefix[0] in self.child:
                return self.child[prefix[0]].startsWith(prefix[1:])
            return False
        return True

        