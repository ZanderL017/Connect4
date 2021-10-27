# Board Games

This repository has implementations of board games in python! So far, I have Connect4 and Checkers. They were developed in python 3.8.

Currently, they support playing through a command line interface. For Connect4, start a game by typing

```python3 play.py connect4```

and make moves by choosing the column to put your piece in, 0-6.

```
[_, _, _, _, _, _, _]
[_, _, _, _, _, _, _]
[_, _, _, _, _, _, _]
[_, _, _, _, _, _, _]
[_, _, _, _, _, _, _]
[_, _, _, _, _, _, _]

What is X's move? 
0
[_, _, _, _, _, _, _]
[_, _, _, _, _, _, _]
[_, _, _, _, _, _, _]
[_, _, _, _, _, _, _]
[_, _, _, _, _, _, _]
[X, _, _, _, _, _, _]

What is O's move? 
```
For checkers, start a game by typing 

```python3 play.py checkers```

```
A - o - o - o - o 
B o - o - o - o - 
C - o - o - o - o 
D - - - - - - - - 
E - - - - - - - - 
F x - x - x - x - 
G - x - x - x - x 
H x - x - x - x - 
  1 2 3 4 5 6 7 8 
What is X's move? 
F3 NE
A - x - x - x - x 
B x - x - x - x - 
C - x - x - - - x 
D - - - - x - - - 
E - - - - - - - - 
F o - o - o - o - 
G - o - o - o - o 
H o - o - o - o - 
  1 2 3 4 5 6 7 8 
What is O's move? 
F7 NW
A - o - o - o - o 
B o - o - o - o - 
C - - - o - o - o 
D - - o - - - - - 
E - - - x - - - - 
F x - - - x - x - 
G - x - x - x - x 
H x - x - x - x - 
  1 2 3 4 5 6 7 8 
What is X's move? 
```
You can make moves by specfying the piece you want to move [A-H][1-8] and then the direction (NW, NE, SW, SE). Notice that the board flips after every turn! King pieces, which can move in all 4 directions, are signified with capital letters, while normal pieces are lowercase letters.
