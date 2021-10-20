from player import Player
from board import Board
import random

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

class RandomAgent(Player):

    def get_move(self, board:Board):
        possible_moves = board.possible_moves(self.identifier)
        move = random.choice(possible_moves)
        return move
