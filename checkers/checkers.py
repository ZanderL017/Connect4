from .board import Board
from .user import User

class Checkers():
    
    def __init__(self, p1, p2):
        assert p1.identifier == 'X'
        assert p2.identifier == 'O'
        self.p1 = p1
        self.p2 = p2
        self.game_board = Board()
        self.winner = None

    def play(self):
        currently_moving =  self.p1
        while self.winner == None:
            move = currently_moving.take_turn(self.game_board)
            self.game_board.flip_grid()
            currently_moving = self.next_turn(currently_moving)
            if self.hasLost(currently_moving):
                self.winner = self.next_turn(currently_moving)


    def next_turn(self, currently_moving):
        if currently_moving == self.p1:
            return self.p2
        else:
            return self.p1

    def hasLost(self, player):
        return self.game_board.num_pieces(player.identifier) == 0 or len(self.game_board.possible_moves(player.identifier)) == 0

    def print_results(self):
        print("The winner is player " + self.winner.identifier + ".")
        print(self.game_board)
