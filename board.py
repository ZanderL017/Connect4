from tile import Tile

class Board:

    def __init__(self, num_rows, num_cols):
        self.grid = []
        for i in range(num_rows):
            grid_row = []
            for j in range(num_cols):
                tile = Tile("-", i, j)
                grid_row.append(tile)
            self.grid.append(grid_row)
    
    def __repr__(self):
        s = ""
        for row in self.grid:
            s += str(row) + "\n"
        return s