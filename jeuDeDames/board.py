"""Define a class for representing a board for the game of draughts.

A board has a given, parameterizable width, and contains pieces and their
positions. It provides methods for executing moves (including captures and
promotion of men to kings), handling the list of pieces, the forward and backward
directions for each color, and providing a text representation of itself."""


from pieces import *


class Board:
    """Represent an n x n board and pieces."""

    # Width of the text representation of a square, in number of characters
    square_width = 3

    # Height of the text representation of a square, in number of characters
    square_height = 2

    def __init__ (self, width):
        """Build a board of a given width, with pieces at their initial position.

        width -- an even, positive integer (at least 4)
        Raises an exception in case width is odd or less than 4
        (4 is the minimum width such that men can be separated by
        two rows in the initial position).
        """
        if width % 2 == 1 or width < 4:
            raise Exception ("Bad width: " + str(width))
        self.width = width
        light_pieces = [Man((row, column), Colors.LIGHT)
                        for row in self._rows(Colors.LIGHT)
                        for column in self._columns(row)]
        dark_pieces = [Man((row, column), Colors.DARK)
                       for row in self._rows(Colors.DARK)
                       for column in self._columns(row)]
        self.pieces = light_pieces + dark_pieces

    # Querying pieces =========================================================

    def get_pieces (self, color):
        """Return the list of all pieces of a given color on this board."""
        return [piece for piece in self.pieces if piece.color == color]

    def get_piece (self, position):
        """Return the piece at a given position on this board, or None."""
        for piece in self.pieces:
            if piece.position == position:
                return piece
        return None

    # Querying positions ======================================================

    def is_valid (self, position):
        """Return True if and only if a given position is on this board."""
        return (position[0] >= 0
                and position[0] < self.width
                and position[1] >= 0
                and position[1] < self.width)

    def is_empty (self, position):
        """Return True if and only if there is no piece at a given position."""
        return not any([piece.position == position for piece in self.pieces])

    def is_occupied (self, position, color):
        """Return True if and only if there is a piece of a given color at a given position."""
        return any([piece.position == position and piece.color == color for piece in self.pieces])

    @staticmethod
    def forward (color):
        """Return the forward direction (delta_row = +1 or -1) for a given color."""
        if color == Colors.LIGHT:
            return 1
        else:
            return -1

    # Handling moves and pieces ===============================================

    def move (self, start, end):
        """Move the piece at a given position to another, given position.

        Does nothing else than moving the piece (does not check captures, etc.).
        Is silent if there is no piece at the given starting position."""
        for piece in self.pieces:
            if piece.position == start:
                piece.position = end

    def remove_piece (self, position):
        """Remove the piece at a given position on this board.

        Is silent if there is no piece at the given position."""
        for i in range(len(self.pieces)):
            if self.pieces[i].position == position:
                del self.pieces[i]
                break

    def execute (self, move):
        """Execute a move, including captures and promotion.

        move -- an instance of class Move"""
        # Executing the sequence of atomic moves
        for atomic_move in move:
            self.move(atomic_move.start, atomic_move.end)
            if isinstance(atomic_move, Capture):
                self.remove_piece(atomic_move.middle)
        # Promoting to king if last move ended on last row
        last_position = move[-1].end
        piece = self.get_piece(last_position)
        if last_position[0] == self._last_row(piece.color):
            if isinstance(piece, Man):
                self.remove_piece(last_position)
                self.pieces.append(King(last_position, piece.color))

    # Text representation =====================================================

    def to_lines (self):
        """Return a multiline plain text representation of the board."""
        # Get list of pieces in display order
        ordering = lambda piece: self._position_to_int(piece.position)
        to_display = sorted(self.pieces, key = ordering)
        res = ""
        for row in range(self.width-1,-1,-1):
            for column in range(self.width):
                if to_display != [] and to_display[0].position == (row,column):
                    # Display a piece
                    piece = to_display[0]
                    del to_display[0]
                    res += str(piece)
                    res += " " * (Board.square_width - len(str(piece)))
                else:
                    # Display an empty square
                    res += "."
                    res += " " * (Board.square_width - 1)
                res += " "
            res += "\n" * Board.square_height
        return res

    # Auxiliary methods =======================================================

    # Used by execute, for promotions
    def _last_row (self, color):
        """Return the last (promotion) row for a given color."""
        if color == Colors.LIGHT:
            return self.width-1
        else:
            return 0

    # Used by to_lines, for accessing pieces in display order
    def _position_to_int (self, position):
        """Compute an integer for a given position, for ordering purposes.

        The top-left (resp. bottom-right) position has the smallest
        (resp. larger) integer.
        """
        return (self.width - 1 - position[0]) * self.width + position[1]

    # Used by __init__, for the initial setting of pieces
    def _rows (self, color):
        """Return the rows initially occupied by a given color."""
        if color == Colors.LIGHT:
            return range(self.width // 2 - 1)
        else:
            return range(self.width - 1, self.width // 2, -1)

    # Used by __init__, for the initial setting of pieces
    def _columns (self, row):
        """Return the columns initially occupied in a given row."""
        return range(row % 2, self.width, 2)
