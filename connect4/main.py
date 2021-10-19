from connect4 import Connect4
from user import User

player1 = User('X')
player2 = User('O')

game = Connect4(player1, player2)

game.play()
game.print_results()