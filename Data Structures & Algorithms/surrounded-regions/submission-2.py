class Solution:
    def solve(self, board: List[List[str]]) -> None:
        stack = []
        visited = set()

        for r in range(len(board)):
            if board[r][0] == 'O':
                stack.append((r, 0))

            if board[r][len(board[0]) - 1] == 'O':
                stack.append((r, len(board[0]) - 1))

        for c in range(len(board[0])):
            if board[0][c] == 'O':
                stack.append((0, c))

            if board[len(board) - 1][c] == 'O':
                stack.append((len(board) - 1, c))
        
        while stack:
            r, c = stack.pop()

            if (
                r < 0 or
                r >= len(board) or
                c < 0 or
                c >= len(board[0]) or
                (r, c) in visited or
                board[r][c] == 'X'
            ):
                continue
            
            visited.add((r, c))
            
            stack.extend([
                (r + 1, c),
                (r - 1, c),
                (r, c + 1),
                (r, c - 1)
            ])

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r, c) not in visited and board[r][c] == 'O':
                    board[r][c] = 'X'
        
            

