"""
This program creates a initializes a Board and an AI object to start a game of tic tac toe in
the play method. The user starts as X and makes a move by entering the number of the position
they want to place an X on the board.

Jaden Russell
4/1/2026
"""

from board import Board
from ai import AI
import random


def get_player_move(board):
    while True:
        try:
            move = int(input("Your move (1-9): ")) - 1
            if 0 <= move <= 8 and board.make_move(move, 'X'):
                return
            print("Invalid move, try again.")
        except ValueError:
            print("Enter a number 1-9.")


def play():
    board = Board()
    ai = AI(player='O', opponent='X')

    print("Tic-Tac-Toe — You are X, AI is O")
    print("Positions: 1-9 (left to right, top to bottom)\n")

    while True:
        board.display()
        winner, _ = board.check_winner()

        if winner:
            print(f"\n{'You win!' if winner == 'X' else 'AI wins!'}")
            break
        if board.is_full():
            print("\nIt's a draw!")
            break

        if len(board.available_moves()) % 2 == 1:
            get_player_move(board)
        else:
            move = ai.best_move(board)
            board.cells[move] = 'O'
            print(f"AI plays position {move + 1}")


if __name__ == "__main__":
    play()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
