class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_store = defaultdict(set)
        cols_store = defaultdict(set)
        squares_store = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rows_store[row] or board[row][col] in cols_store[col] or board[row][col] in squares_store[(row // 3, col // 3)]:
                    return False
                
                rows_store[row].add(board[row][col])
                cols_store[col].add(board[row][col])
                squares_store[(row // 3, col // 3)].add(board[row][col])
        
        return True


                
        