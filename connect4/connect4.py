from .board import Board

NUM_ROWS = 6
NUM_COLS = 7

class Connect4:

    def __init__(self, player1, player2):
        self.NUM_ROWS = 6
        self.NUM_COLS = 7
        self.game_board = Board(self.NUM_ROWS, self.NUM_COLS)
        self.player1 = player1
        self.player2 = player2
        self.winner = None

    def play(self):
        is_winner = None
        current_turn = self.player1
        while not is_winner:
            move = current_turn.take_turn(self.game_board)
            if self.game_board.is_winning_move(self.game_board.get_tile(move)):
                is_winner = current_turn
            
            if (current_turn == self.player1):
                current_turn = self.player2
            else:
                current_turn = self.player1
        self.winner = is_winner

    def print_results(self):
        print("The winner is player " + self.winner.identifier + ".")
        print(self.game_board)
