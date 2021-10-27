import sys

VALID_GAMES = ['checkers', 'connect4']

if len(sys.argv) == 1:
    raise Exception("No game is specified. Choose a game to play!")

if len(sys.argv) > 2:
    raise Exception("To many arguments - just specify which game you would like to play.")

game = sys.argv[1]
if game not in VALID_GAMES:
    raise ValueError("Invalid game. Choose a game from " + str(VALID_GAMES))

if game == "checkers":
    from checkers.checkers import Checkers
    from checkers.user import User
    p1 = User('X')
    p2 = User('O')
    game = Checkers(p1, p2)
    game.play()
    game.print_results()

if game == "connect4":
    from connect4.connect4 import Connect4
    from connect4.user import User
    player1 = User('X')
    player2 = User('O')
    game = Connect4(player1, player2)
    game.play()
    game.print_results()