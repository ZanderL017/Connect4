from typing import Tuple

VALID_TYPES = ['normal', 'king']
VALID_IDS = ['X', 'O']

class Piece():
    def __init__(self, type:str, id:str):
        assert type in VALID_TYPES
        assert id in VALID_IDS
        self.type = type
        self.id = id

    def __repr__(self):
        if self.type == "normal":
            return self.id.lower()
        elif self.type == "king":
            return self.id
        else:
            raise ValueError
    
    def get_possible_directions(self):
        if self.type == "normal":
            return ['NW', 'NE']
        elif self.type == 'king':
            return ['NW', 'NE', 'SW', 'SE']
        else:
            raise ValueError

    
            
