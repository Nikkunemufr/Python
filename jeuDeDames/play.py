"""Provide a function for handling a game of draughts in console mode (in French)."""


from board import *


def prompt_move (moves):
    """Display a list of moves and prompt for one."""
    res = -1
    while res < 0 or res >= len(moves):
        print("Coups possibles :")
        for i in range(len(moves)):
            prompt = str(i)
            move = moves[i]
            for atomic_move in move:
                prompt += " : "
                prompt += str(atomic_move)
            print(prompt)
        res = int(input("Coup n° ? "))
    return moves[res]

def play (board_size):
    """Manage a complete game in console move for a given board size."""
    board = Board(board_size)
    current_color = Colors.LIGHT
    while board.get_pieces(current_color) != []:
        # Display the current situation
        print("")
        print(board.to_lines())
        print("Tour des :", Colors.str(current_color))
        # All legal moves at this point
        moves = [move
                 for piece in board.get_pieces(current_color)
                 for move in piece.moves(board)]
        if moves != []:
            # Prompt the user for a move
            move = prompt_move(moves)
            board.execute(move)
            current_color = Colors.opponent(current_color)
        else:
            # No move available, game is over
            print("Les", Colors.str(current_color), "ont perdu (aucun coup possible).")
            break
    # No piece left, game is over
    print("")
    print(board.to_lines())
    print("Les", Colors.str(current_color), "ont perdu (plus de pièces).")
