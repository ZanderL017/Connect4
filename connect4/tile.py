class Tile:
    """
    A tile represent a given spot on the board in connect 4. It has a location, given by a 
    row and column, and a value. An empty tile is denoted by '-', and each player has their
    own unique value for their tiles.
    """
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col

    def __repr__(self):
        return self.value

    def get_location(self):
        return self.row, self.col