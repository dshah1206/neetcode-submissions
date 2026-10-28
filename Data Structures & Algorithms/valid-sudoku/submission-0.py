class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        T.C - O(N^2), S.C = O(N)
        Condition: 1
        Check for duplicates in each row

        Condition: 2
        Check for duplicates in each col

        Condition: 3
        [ Squares: Consider 9x9 made up of 9 sub boxes
            [[0],[1],[2]]
            [[3],[4],[5]]
            [[6],[7],[8]]

            row = (square//3)*3 + i
            • Squares 0, 1, 2 start at row 0.
            • Squares 3, 4, 5 start at row 3.
            • Squares 6, 7, 8 start at row 6.

            col = (square%3)*3 + j
            • Squares 0, 3, 6 start at column 0.
            • Squares 1, 4, 7 start at column 3.
            • Squares 2, 5, 8 start at column 6.
        ]
        """
        
        n = len(board)
        m = len(board[0])

        for row in range(n):
            seen = set()
            for col in range(m):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])

        for col in range(m):
            seen = set()
            for row in range(n):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])
        
        for square in range((n//3*m//3)):
            seen = set()
            for i in range(n//3):
                for j in range(m//3):
                    row = (square//3)*3 + i
                    col = (square%3)*3 + j
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])
        return True
        

        