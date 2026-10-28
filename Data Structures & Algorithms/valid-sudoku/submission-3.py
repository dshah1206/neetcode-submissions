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
        
        # n = len(board)
        # m = len(board[0])

        # for row in range(n):
        #     seen = set()
        #     for col in range(m):
        #         if board[row][col] == ".":
        #             continue
        #         elif board[row][col] in seen:
        #             return False
        #         else:
        #             seen.add(board[row][col])

        # for col in range(m):
        #     seen = set()
        #     for row in range(n):
        #         if board[row][col] == ".":
        #             continue
        #         elif board[row][col] in seen:
        #             return False
        #         else:
        #             seen.add(board[row][col])
        
        # for square in range(9):
        #     seen = set()
        #     for i in range(3):
        #         for j in range(3):
        #             row = (square//3)*3 + i
        #             col = (square%3)*3 + j
        #             if board[row][col] == ".":
        #                 continue
        #             elif board[row][col] in seen:
        #                 return False
        #             else:
        #                 seen.add(board[row][col])
        # return True

        """
        T.C - O(N^2), S.C = O(N^2)
        """
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if ( board[row][col] in rows[row] or 
                    board[row][col] in cols[col] or
                    board[row][col] in square[(row//3, col//3)]):
                    return False
                
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                square[(row//3,col//3)].add(board[row][col])
        return True

        """
        T.C - O(N^2), S.C = O(N) -  Bitmask
        """

        # rows = [0] * 9
        # cols = [0] * 9
        # square = [0] * 9

        # for row in range(9):
        #     for col in range(9):
        #         if board[row][col] == ".":
        #             continue
        #         val = int(board[row][col]) - 1
        #         if (1 << val) & rows[row]:
        #             return False
        #         if (1 << val) & cols[col]:
        #             return False
        #         if (1 << val) & square[(row//3)*3 + (col//3)]:
        #             return False
        #         rows[row] = rows[row] | (1 << val)
        #         cols[col] = cols[col] | (1 << val)
        #         square[(row//3)*3 + (col//3)] = square[(row//3)*3 + (col//3)] | (1 << val)
        
        # return True




        

        