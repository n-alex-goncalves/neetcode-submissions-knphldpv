class WordDictionary:

    def __init__(self):
        self.children = {}
        self.endOfWord = False
        

    def addWord(self, word: str) -> None:
        if word:
            if word[0] not in self.children:
                self.children[word[0]] = WordDictionary()
            self.children[word[0]].addWord(word[1:])
            return
        self.endOfWord = True
        

    def search(self, word: str) -> bool:
        if word:
            if word[0] not in self.children:
                if word[0] == '.':
                    return any(x.search(word[1:]) for x in self.children.values())
                return False
            return self.children[word[0]].search(word[1:])
        return self.endOfWord
        
