class Board:
    def __init__(self):
        # Initialize an 8x8 chessboard, where each square can hold a piece or be empty
        self.board = [['' for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        """Initializes the board with the standard piece layout"""
        # White pieces (Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)
        self.board[0] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        # Black pieces
        self.board[7] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']

        # Pawns
        self.board[1] = ['P'] * 8 # White pawns
        self.board[6] = ['p'] * 8 # Black pawns

        # Empty spaces
        for row in range(2, 6):
            self.board[row] = [''] * 8

    def print_board(self):
        """Prints the current board state"""
        for row in self.board:
            print(' '.join(row if row != '' else '.' for row in row))
        print()

    def get_piece(self, row, col):
        """Returns the piece at a specific location"""
        return self.board[row][col]

    def move_piece(self, start_pos, end_pos):
        """Moves a piece from one position to another"""
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        piece = self.board[start_row][start_col]

        if piece:
            self.board[end_row][end_col] = piece # Move piece to the new location
            self.board[start_row][start_col] = '' # Empty the starting square
        else:
            print("Invalid move: No piece at start position")

    def is_empty(self, row, col):
        """Check if a square is empty"""
        return self.board[row][col] == ''