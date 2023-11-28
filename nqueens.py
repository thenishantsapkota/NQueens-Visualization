class NQueenProblem:
    def __init__(self, num_queens):
        self.num_queens = num_queens
        # Here I'm initializing the board for playing[4x4 for 4 queen]
        # [8x8 for 8 queen]
        self.board = [
            [0 for _ in range(self.num_queens)] for _ in range(self.num_queens)
        ]

    def is_safe(self, row, col):
        # Checking the row and columns
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        # Checking the upper diagonal on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Checking the lower diagonal on the left side
        for i, j in zip(range(row, self.num_queens, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        return True