from .tile import Tile

class Board:

    def __init__(self, num_rows, num_cols):
        self.EMPTY_TILE_VALUE = '_'
        self.winning_forms = self.genererate_winning_forms()
        self.num_rows = num_rows
        self.num_cols = num_cols
        # make grid
        self.grid = []
        for i in range(num_rows):
            grid_row = []
            for j in range(num_cols):
                tile = Tile(self.EMPTY_TILE_VALUE, i, j)
                grid_row.append(tile)
            self.grid.append(grid_row)
    
    def __repr__(self):
        s = ""
        for row in self.grid:
            s += str(row) + "\n"
        return s

    # create list of winning 4-in-a-row combinations
    
    def genererate_winning_forms(self):
        slopes = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        location_forms = [
            (0, 1, 2, 3), # new move on edge
            (-1, 0, 1, 2) # new move in middle
        ]
        winning_forms = []
        for location_form in location_forms:
            for slope in slopes:
                winning_form = []
                for scalar in location_form:
                    winning_form.append(self.multiply_coordinates(slope, scalar))
                winning_forms.append(winning_form)
        return winning_forms



    # Functions for checking and making valid moves

    def is_valid_move(self, column):
        return self.is_inbounds((0, column)) and self.get_tile((0, column)).value == self.EMPTY_TILE_VALUE
        
    def make_move(self, column, new_value):
        assert self.is_valid_move(column)

        input_location = (0, column)
        while True:
            if input_location[0] == self.num_rows - 1:
                break
            if self.get_tile(self.add_coordinates(input_location, (1, 0))).value != self.EMPTY_TILE_VALUE:
                break
            input_location = self.add_coordinates(input_location, (1, 0))
        self.change_tile_value(new_value, input_location)
        return input_location

    def change_tile_value(self, new_value, location):
        self.get_tile(location).value = new_value

    # Functions for checking for a winner

    def is_winning_move(self, tile):
        if not self.is_inbounds(tile.get_location()):
            return False
        for form in self.winning_forms:
            if self.is_winning_form(tile, form):
                return True
        return False

    def is_winning_form(self, tile, form):
        for location_diff in form:
            board_coordinates = self.add_coordinates(tile.get_location(), location_diff)
            if not self.is_inbounds(board_coordinates):
                return False
            if self.get_tile(board_coordinates).value == self.EMPTY_TILE_VALUE:
                return False
            if self.get_tile(board_coordinates).value != tile.value:
                return False
        return True

    # Helpter functions

    def is_inbounds(self, location):
        row, col = location
        return row >= 0 and row < self.num_rows and col >= 0 and col < self.num_cols

    def add_coordinates(self, location_1, location_2):
        return (location_1[0] + location_2[0], location_1[1] + location_2[1])

    def multiply_coordinates(self, location, scalar):
        return (location[0] * scalar, location[1] * scalar)

    def get_tile(self, location):
        return self.grid[location[0]][location[1]]