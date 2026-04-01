"""
This program creates the board class with methods to initialize the tic tac toe board, allow
players to make moves and check for a winner, tie or any available moves to be made

Jaden Russell
4/1/2026
"""


class Board:
    def __init__(self):
        self.cells = [' '] * 9

    def display(self):
        for i in range(0, 9, 3):
            row = self.cells[i:i+3]
            print(' | ' .join(row))
            if i < 6:
                print('---------')

    def make_move(self, index, player):
        if self.cells[index] == ' ':
            self.cells[index] = player
            return True
        return False

    def available_moves(self):
        return [i for i, c in enumerate(self.cells) if c == ' ']

    def check_winner(self):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
            [0, 4, 8], [2, 4, 6]           # diagonals
        ]
        for combo in wins:
            a, b, c = combo
            if (self.cells[a] == self.cells[b] == self.cells[c]
                    and self.cells[a] != ' '):
                return self.cells[a], combo
        return None, None

    def is_full(self):
        return ' ' not in self.cells
