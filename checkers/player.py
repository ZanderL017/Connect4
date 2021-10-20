from board import Board

class Player:

    def __init__(self, id:str):
        self.identifier = id

    def take_turn(self, board:Board):
        move = self.get_move(board)
        board.make_move(move, self.identifier)

    def get_move(self, board:Board):
        pass
        