from .player import Player

class User(Player):

    def get_move(self, board):
        print(board)
        move = -1
        while not board.is_valid_move(move):
            move = int(input("What is " + self.identifier + "'s move? \n"))
        return move
