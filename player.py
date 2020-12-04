from board import Board

class Player:

    def __init__(self, id):
        self.identifier = id

    def take_turn(self, board):
        move = self.get_move(board)
        move_location = board.make_move(move, self.identifier)
        return move_location

    def get_move(self, board):
        pass
        

