"""
This program creates an AI class that calculates the best move to make using the minimax method
and returns the index of the board

Jaden Russell
4/1/2026
"""


class AI:
    def __init__(self, player='O', opponent='X'):
        self.player = player
        self.opponent = opponent

    def best_move(self, board):
        best_score = float('-inf')
        move = None
        for i in board.available_moves():
            board.cells[i] = self.player
            score = self.minimax(board, False)
            board.cells[i] = ' '
            if score > best_score:
                best_score = score
                move = i
        return move

    def minimax(self, board, is_maximizing):
        winner, _ = board.check_winner()
        if winner == self.player:
            return 1
        if winner == self.opponent:
            return -1
        if board.is_full():
            return 0

        if is_maximizing:
            best = float('-inf')
            for i in board.available_moves():
                board.cells[i] = self.player
                best = max(best, self.minimax(board, False))
                board.cells[i] = ' '
            return best
        else:
            best = float('inf')
            for i in board.available_moves():
                board.cells[i] = self.opponent
                best = min(best, self.minimax(board, True))
                board.cells[i] = ' '
            return best
