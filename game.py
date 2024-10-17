class TicTacToeGame:
    def __init__(self):
        # Create a 3x3 board, initially empty
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # 'X' or 'O'
        self.winner = None
        self.moves_made = 0

    def reset(self):
        """Reset the game board and state"""
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.moves_made = 0

    def make_move(self, row, col):
        """Make a move if the cell is empty and return if it's valid"""
        if self.board[row][col] is None and not self.winner:
            self.board[row][col] = self.current_player
            self.moves_made += 1
            if self.check_winner():
                self.winner = self.current_player
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        """Check if the current player has won"""
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)) or \
               all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player:
            return True
        return False

    def is_draw(self):
        """Check if the game is a draw"""
        return self.moves_made == 9 and self.winner is None
