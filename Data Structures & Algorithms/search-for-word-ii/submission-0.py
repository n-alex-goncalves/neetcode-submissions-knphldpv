class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def add(self, word):
        if word:
            if word[0] not in self.children:
                self.children[word[0]] = Trie()
            self.children[word[0]].add(word[1:])
            return
        self.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.output = set()
        def checkWord(col, row, tree, cur):    
            if (
                col < 0
                or col >= len(board) 
                or row < 0
                or row >= len(board[0]) 
                or board[col][row] == '.'
                or board[col][row] not in tree.children
            ):
                return

            nxt = tree.children[board[col][row]]

            if nxt.endOfWord:
                self.output.add(cur + board[col][row])
            
            temp = board[col][row]
            board[col][row] = '.'

            output = (
                checkWord(col + 1, row, nxt, cur + temp) or
                checkWord(col, row + 1, nxt, cur + temp) or
                checkWord(col - 1, row, nxt, cur + temp) or
                checkWord(col, row - 1, nxt, cur + temp)
            )

            board[col][row] = temp
            return output 
        
        tree = Trie()
        for word in words:
            tree.add(word)

        for col in range(len(board)):
            for row in range(len(board[0])):
                checkWord(col, row, tree, '')
        
        return list(self.output)


        