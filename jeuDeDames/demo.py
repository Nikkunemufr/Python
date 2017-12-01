"""Provide a demo for this package together with a function for playing demoes.

A demo is simply a list of legal moves, starting from the initial position (not necessarily
ending in a finished game)."""


from board import *


def play_demo (board_size, demo):
    board = Board(board_size)
    current_color = Colors.LIGHT
    # Playing moves in turn
    for move in demo:
        # Displaying current situation
        print("")
        print(board.to_lines())
        print("Tour des :", Colors.str(current_color))
        input("Tapez sur <entrée> pour continuer")
        # List of all legal moves at this point
        moves = [one_move
                 for piece in board.get_pieces(current_color)
                 for one_move in piece.moves(board)]
        # Checking then executing the move
        if move not in moves:
            raise Exception("Move " + str(move) + " is not allowed at this point")
        else:
            board.execute(move)
            current_color = Colors.opponent(current_color)
    # Finalizing, once the demo has been exhausted
    print("")
    print(board.to_lines())
    if board.get_pieces(current_color) == []:
        print("Les", Colors.str(current_color), "ont perdu (plus de pièces).")
    elif [move for piece in board.get_pieces(current_color) for move in piece.moves(board)] == []:
        print("Les", Colors.str(current_color), "ont perdu (plus de coups légaux).")
    print("Fin de la démo.")

demo = [
    Move(AtomicMove((1,1), (2,2))),
    Move(AtomicMove((4,2), (3,1))),
    Move(AtomicMove((1,3), (2,4))),
    Move(Capture((3,1), (1,3), (2,2)), Capture((1,3), (3,5), (2,4))),
    Move(AtomicMove((0,4), (1,3))),
    Move(AtomicMove((3,5), (2,4))),
    Move(AtomicMove((0,2), (1,1))),
    Move(Capture((2,4), (0,2), (1,3)), Capture((0,2), (2,0), (1,1))),
    Move(AtomicMove((0,0), (1,1))),
    Move(Capture((2,0), (0,2), (1,1))),
    Move(AtomicMove((1,5), (2,4))),
    Move(AtomicMove((0,2), (1,3))),
    Move(AtomicMove((2,4), (3,5))),
    Move(AtomicMove((5,3), (4,2))),
    Move(Capture((3,5), (5,3), (4,4))),
    Move(AtomicMove((4,0), (3,1))),
    Move(AtomicMove((5,3), (3,5))),
    Move(AtomicMove((1,3), (2,4))),
    Move(Capture((3,5), (1,3), (2,4)), Capture((1,3), (4,0), (3,1))),
    Move(AtomicMove((4,2), (3,3))),
    Move(AtomicMove((4,0), (2,2))),
    Move(Capture((3,3), (1,1), (2,2)))
]
