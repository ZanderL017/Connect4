from .piece import Piece
from typing import Tuple
import re

BOARD_LENGTH = 8
EMPTY_SQUARE = '-'
ROW_TAGS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
COL_TAGS = ['1', '2', '3', '4', '5', '6', '7', '8']

class Board():
    def __init__(self):
        self.grid = []
        for i in range(BOARD_LENGTH):
            row = []
            for j in range(BOARD_LENGTH):
                row.append(EMPTY_SQUARE)
            self.grid.append(row)
        self.make_starting_board()


    def __repr__(self):
        s = ""
        for row_i in range(BOARD_LENGTH):
            s += ROW_TAGS[row_i]
            s += " "
            for col_i in range(BOARD_LENGTH):
                s +=  str(self.grid[row_i][col_i]) + " "
            s += "\n"
        s += "  "
        for tag in COL_TAGS:
            s += tag + " "
        return s
    

    def make_starting_board(self):
        # Create X pieces
        rows_filled = 0
        for row_i in range(BOARD_LENGTH - 3, BOARD_LENGTH):
            offset = rows_filled % 2
            for col in range(0, BOARD_LENGTH, 2):
                col_i = col + offset
                piece = Piece('normal', 'X')
                self.grid[row_i][col_i] = piece
            rows_filled += 1
        # Create O pieces
        for row_i in range(0, 3):
            offset = rows_filled % 2
            for col in range(0, BOARD_LENGTH, 2):
                col_i = col + offset
                piece = Piece('normal', 'O')
                self.grid[row_i][col_i] = piece
            rows_filled += 1


    def is_valid_move(self, move, id:str):
        if len(move) != 2:
            return False
        if re.match('[A-H][0-9]', move[0]) == None:
            return False

        piece_loc, direction = move;
        piece_coords = self.loc_to_coords(piece_loc)
        piece = self.get_piece(piece_coords)

        if type(piece) != Piece:
            return False
        if piece.id != id.upper():
            return False
        if direction not in piece.get_possible_directions():
            return False

        destination = self.next_coords(piece_coords, direction)
        if not self.is_inbounds(destination):
            return False
        # Check for jump
        if self.is_piece(destination):
            # Can't jump over own piece
            if not self.can_make_jump(destination, direction, id):
                return False
        return True


    def make_move(self, move:Tuple[str, str], id:str):
        #assumes the move is valid
        piece_loc, direction = move;
        piece_coords = self.loc_to_coords(piece_loc)
        piece = self.get_piece(piece_coords)

        destination = self.next_coords(piece_coords, direction)
        
        # Normal Move
        if not self.is_piece(destination):
            self.set_piece(piece_coords, EMPTY_SQUARE)
            if self.reached_end(destination):
                piece.type = 'king'
            self.set_piece(destination, piece)
            return
        jumped_coords = destination
        while self.can_make_jump(jumped_coords, direction, id):
            jump_dest = self.next_coords(jumped_coords, direction)
            self.set_piece(jumped_coords, EMPTY_SQUARE)
            jumped_coords = self.next_coords(jump_dest, direction)
            if not self.is_inbounds(jumped_coords) or not self.is_piece(jumped_coords):
                break;
        self.set_piece(piece_coords, EMPTY_SQUARE)
        if self.reached_end(jump_dest):
                piece.type = 'king'
        self.set_piece(jump_dest, piece)

        
    def can_make_jump(self, jumped_coords:Tuple[int, int], direction:str, id:str):
        jumped_piece = self.get_piece(jumped_coords)
        if jumped_piece.id == id.upper():
            return False
        jump_dest = self.next_coords(jumped_coords, direction)
        # Jump landing has to be inbounds and empty
        if not self.is_inbounds(jump_dest):
            return False
        if self.is_piece(jump_dest):
            return False
        return True


    def num_pieces(self, id):
        num = 0
        for row_i in range(BOARD_LENGTH):
            for col_i in range(BOARD_LENGTH):
                if self.is_piece((row_i, col_i)):
                    if self.get_piece((row_i, col_i)).id == id:
                        num += 1
        return num

    def possible_moves(self, id):
        moves = []
        for row_i in range(BOARD_LENGTH):
            for col_i in range(BOARD_LENGTH):
                if not self.is_piece((row_i, col_i)):
                    continue
                piece = self.get_piece((row_i, col_i))
                if piece.id == id:
                    for direction in piece.get_possible_directions():
                        move = [self.coords_to_loc((row_i, col_i)), direction]
                        if self.is_valid_move(move, id):
                            moves.append(move)
        return moves


    def flip_grid(self):
        self.grid.reverse()
        for row in self.grid:
            row.reverse()


    def loc_to_coords(self, piece_loc:str):
        row = ROW_TAGS.index(piece_loc[0])
        col = COL_TAGS.index(piece_loc[1])
        return (row, col)

    def coords_to_loc(self, coords:Tuple[int, int]):
        row = ROW_TAGS[coords[0]]
        col = COL_TAGS[coords[1]]
        return row + col


    def get_piece(self, piece_coords:Tuple[int, int]):
        return self.grid[piece_coords[0]][piece_coords[1]]


    def is_inbounds(self, coords:Tuple[int, int]):
        row, col = coords
        return row >= 0 and row < BOARD_LENGTH and col >= 0 and col < BOARD_LENGTH


    def next_coords(self, coords, direction):
        if direction == 'NW':
            return (coords[0] - 1, coords[1] - 1)
        elif direction == 'NE':
            return (coords[0] - 1, coords[1] + 1)
        elif direction == 'SW':
            return (coords[0] + 1, coords[1] - 1)
        elif direction == 'SE':
            return (coords[0] + 1, coords[1] + 1)
        else:
            raise ValueError
    

    def is_piece(self, coords:Tuple[int, int]):
        return type(self.get_piece(coords)) == Piece


    def set_piece(self, coords:Tuple[int, int], piece):
        self.grid[coords[0]][coords[1]] = piece

    def reached_end(self, coords:Tuple[int, int]):
        return coords[0] == 0

