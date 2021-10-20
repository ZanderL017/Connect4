from player import Player
from board import Board

class User(Player):

    def get_move(self, board:Board):
        print(board)
        move = -1
        while (True):
            move_str = input("What is " + self.identifier + "'s move? \n")
            move = move_str.strip().split(" ")
            if board.is_valid_move(move, self.identifier):
                break;
            else:
                print("Not a valid move.")
        return move
        