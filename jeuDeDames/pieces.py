"""Define classes for representing pieces for the game of draughts.

Pieces have a position and a color, and can compute their possible
moves on a given board."""


from moves import *


class Colors:
    """A utility class for handling colors for the game of draughts.

    Provides two colors, LIGHT and DARK."""

    LIGHT = 0

    DARK = 1

    @staticmethod
    def str (color):
        """Return a human-readable string for a given color in French."""
        if color == Colors.LIGHT:
            return "blancs"
        else:
            return "noirs"
        return Colors.to_string(color, "english")

    @staticmethod
    def opponent (color):
        """Return the opposite color of a given one."""
        return 1 - color


class Piece:
    """A base class for classes representing pieces.

    This class is not intended to be directly instantiated."""

    def __init__ (self, position, color):
        """Build a piece."""
        self.position = position
        self.color = color

    def moves (self, board):
        """Yield all possible moves for this piece on a given board.

        Relies on methods atomic_moves(self, board) and
        _captures(self, board, position) being defined and yielding,
        respectively, all moves without capture
        from the current position, and all atomic captures from a given
        position."""
        # Atomic moves without captures
        for move in self.atomic_moves(board):
            yield Move(move)
        # Atomic captures and sequences of captures
        yield from self._sequences(board, self.position, [])

    def _sequences (self, board, position, captured):
        """Yield all nonempty sequences of captures.

        Captures are computed from a given position on a given board,
        assuming the pieces at a given list of positions have already
        been jumped over during the same move (hence cannot be jumped over
        again. The starting position may be different from the real position
        of this piece.

        Relies on methods atomic_moves and _captures being defined (see
        documentation of moves(self, board))."""
        for capture in self._captures(board, position):
            if not capture.middle in captured:
                # Atomic capture
                yield Move(capture)
                # Sequences of captures starting with this one
                for continuation in self._sequences(board, capture.end, captured+[capture.middle]):
                    yield Move(capture, *continuation)


class Man(Piece):
    """Represent a man for the game of draughts."""

    def __init__ (self, position, color):
        """Build a man."""
        Piece.__init__(self, position, color)

    def __str__ (self):
        """Return a short representation of a man, depending on its color."""
        if self.color == Colors.LIGHT:
            return "pb"
        return "PN"

    def atomic_moves (self, board):
        """Yield all possible atomic moves without capture from the current position."""
        # Men only move forward
        row = self.position[0] + board.forward(self.color)
        # Enumerate both horizontal directions
        for delta_column in [-1, 1]:
            end = (row, self.position[1] + delta_column)
            if board.is_valid(end) and board.is_empty(end):
                yield AtomicMove(self.position, end)

    def atomic_captures (self, board):
        """Yield all possible atomic captures from the current position."""
        return self._captures(board, self.position)

    def _captures (self, board, position):
        """Yield all possible atomic captures from a given position.

        The starting position may be different from the real position of this man."""
        # Enumerate all four directions (captures are possible backwards)
        for delta_row in [-1, 1]:
            for delta_column in [-1, 1]:
                end = (position[0] + 2*delta_row, position[1] + 2*delta_column)
                middle = (position[0] + delta_row, position[1] + delta_column)
                if board.is_valid(end) and board.is_empty(end):
                    if board.is_occupied(middle, Colors.opponent(self.color)):
                        yield Capture(position, end, middle)


class King(Piece):
    """Represent a king for the game of draughts."""

    def __init__ (self, position, color):
        """Build a king."""
        Piece.__init__ (self, position, color)

    def __str__ (self):
        """Return a short representation of a king, depending on its color."""
        if self.color == Colors.LIGHT:
            return "db"
        return "DN"

    def atomic_moves (self, board):
        """Yield all possible atomic moves without capture from the current position."""
        # Enumerate all four directions
        for delta_row in [-1, 1]:
            for delta_column in [-1, 1]:
                # Enumerate all distances up to reaching a nonempty square
                # or leaving the board
                i = 1
                while True:
                    end = (self.position[0] + i * delta_row,
                           self.position[1] + i * delta_column)
                    if board.is_valid(end) and board.is_empty(end):
                        yield AtomicMove(self.position, end)
                    else:
                        break
                    i += 1

    def _captures (self, board, position):
        """Yield all possible atomic captures from a given position.

        The starting position may be different from the real position of this man."""
        # Enumerate all four directions
        for delta_row in [-1, 1]:
            for delta_column in [-1, 1]:
                # No opponent jumped over so far
                capturable = None
                # Enumerate all distances and recording whether an opponent has been jumped
                # over up to reaching a piece of the same color, a second opponent,
                # or leaving the board
                i = 1
                while True:
                    end = (position[0] + i * delta_row,
                           position[1] + i * delta_column)
                    if not board.is_valid(end):
                        # Out of grid
                        break
                    elif board.is_occupied(end, self.color):
                        # Piece of the same color, cannot go further
                        break
                    elif board.is_empty(end) and capturable is None:
                        # No opponent jumped over yet
                        i += 1
                        continue
                    elif board.is_empty(end):
                        # Empty square after an opponent
                        yield Capture(position, end, capturable)
                    elif capturable is None:
                        # First opponent encountered
                        capturable = end
                    else:
                        # Second capturable encountered
                        break
                    i += 1
