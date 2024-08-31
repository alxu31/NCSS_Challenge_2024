class Board:
  def __init__(self, rows, cols) -> None:
    self.rows = rows
    self.cols = cols
    self.board = [['.' for _ in range(cols)] for _ in range(rows)]
  
  # Load a specific board state
  def load_board(self, rows) -> None:
    # rows is a 2D list of strings containing the board state
    self.board = [list(row) for row in rows]

  # Check if a move is valid by verifying if the top row of the selected column is empty
  
  def is_valid_move(self, col) -> bool:
    if self.board[0][col] == ".":
      return True
    return False

  # Get the next open row in a column for a piece to be dropped
  def get_next_open_row(self, col) -> int:
    i = 0
    try:
      while self.board[i][col] == ".":
        i += 1
      return i-1
    except(IndexError):
      return 5

  # Drop a piece into the board at the specified column
  def drop_piece(self, col, piece) -> None:
    self.board[self.get_next_open_row(col)][col] = piece

  # Check if the specified piece player has won the game
  def check_win(self, piece) -> bool:
    b = self.board
    for r in range(len(b)):
      for c in range(len(b[0])):
        # Horizontal
        if c <= len(b[0])-4:
          if all([val==piece for val in [b[r][c], b[r][c+1], b[r][c+2], b[r][c+3]]]):
            return True
        # Vertical
        if r <= len(b)-4:
          if all([val==piece for val in [b[r][c], b[r+1][c], b[r+2][c], b[r+3][c]]]):
            return True
        # Diagonal tl -> br
        if r <= len(b)-4 and c <= len(b[0])-4:
          if all([val==piece for val in [b[r][c], b[r+1][c+1], b[r+2][c+2], b[r+3][c+3]]]):
            return True
        # Diagonal bl -> tr
        if r >= 3 and c <= len(b[0])-4:
          if all([val==piece for val in [b[r][c], b[r-1][c+1], b[r-2][c+2], b[r-3][c+3]]]):
            return True
    return False
  
  # Check if the board is full
  def is_full(self) -> bool:
    if all("." not in li for li in self.board):
      return True
    return False
  
  # Print the current state of the board
  def print_board(self):
    print("| " + " ".join(str(i) for i in range(self.cols)) + " |")
    for row in self.board:
      print("| " + " ".join(row) + " |")
    print("| " + "-" * (self.cols * 2 - 1) + " |")