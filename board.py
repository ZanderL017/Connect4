from tile import Tile

class Board:

    def __init__(self, num_rows, num_cols):
        self.EMPTY_TILE_VALUE = '_'
        # winning 4-in-a-row indices
        self.winning_forms = [
            [(0, 0), (-1, 1), (-2, 2), (-3, 3)],
            [(0, 0), (-1, 0), (-2, 0), (-3, 0)],
            [(0, 0), (-1, -1), (-2, -2), (-3, -3)],
            [(0, 0), (0, -1), (0, -2), (0, -3)],
            [(0, 0), (1, -1), (2, -2), (3, -3)],
            [(0, 0), (1, 0), (2, 0), (3, 0)],
            [(0, 0), (1, 1), (2, 2), (3, 3)],
            [(0, 0), (0, 1), (0, 2), (0, 3)]
        ]
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
    
    # Function for updating player moves to the board

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

    def get_tile(self, location):
        return self.grid[location[0]][location[1]]