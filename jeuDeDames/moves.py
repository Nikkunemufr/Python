"""Define classes for representing moves for the game of draughts.

Three classes are provided, for atomic moves (without capture), for
atomic captures, and for sequences of captures. They are simple classes,
essentially encapsulating positions."""


class AtomicMove:
    """Represent an atomic move without capture."""

    def __init__ (self, start, end):
        """Build an atomic move."""
        self.start = start
        self.end = end

    def __eq__ (self, other):
        """Return True if and only if this instance represents the same move as another, given one."""
        return (isinstance(other, AtomicMove)
                and self.start == other.start
                and self.end == other.end)

    def __str__ (self):
        """Return a human-readable representation of this move."""
        return "(" + str(self.start) + " -> " + str(self.end) + ")"


class Capture(AtomicMove):
    """Represent a move consisting of a single capture."""

    def __init__ (self, start, end, middle):
        """Build an atomic capture.

        middle -- the position at which an opponent is captured (may
        not be the real middle of the move, if this is a capture by a king."""
        AtomicMove.__init__(self, start, end)
        self.middle = middle

    def __eq__ (self, other):
        """Return True if and only if this instance represents the same move as another, given one."""
        return (isinstance(other, Capture)
                and self.start == other.start
                and self.end == other.end
                and self.middle == other.middle)


class Move(list):
    """Represent an arbitrary move for the game of draughts.

    A move is represented as a list of atomic moves and captures, intended to be
    nonempty but possibly a singleton."""

    def __init__ (self, *atomic_moves):
        """Build a move"""
        list.__init__(self)
        for move in atomic_moves:
            self.append(move)

    def first_position ():
        """Return the starting position of this move."""
        return self[0].start

    def last_position ():
        """Return the last position of this move."""
        return self[-1].end

    def captured_positions ():
        """Return the list of position where this move captures an opponent piece."""
        return [move.middle for move in self if isinstance(move, Capture)]

    def __eq__ (self, other):
        """Return True if and only if this instance represents the same move as another, given one."""
        return isinstance(other, Move) and list.__eq__(self, other)

    def __str__ (self):
        """Return a human-readable representation of this move."""
        return ";".join([str(move) for move in self])
