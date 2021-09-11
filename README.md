# Simple-Tic-Tac-Toe

A Simple Tic-Tac-Toe (3x3) completed through the JetBrains Academy.

Two players take it in turns, entering coordinates to place their `X` or `O`.

## Input

When prompted, each player must enter 2 numbers, seperated by a space, between 1 and 3 representing the coordinate to play on the grid. 

Like so:

```
Enter the coordinates: 1 1
```

> Note: A player cannot move where a previous player has already played.

## Grid

The grid is a 3 by 3 grid with each cell represented by the coordinate shown below.

```
-----------------------
| (1,1), (1,2), (1,3) |
| (2,1), (2,2), (2,3) |
| (3,1), (3,2), (3,3) |
-----------------------
```

## Example

```
---------
|       |
|       |
|       |
---------
Enter the coordinates: 2 2
---------
|       |
|   X   |
|       |
---------
Enter the coordinates: 2 2
This cell is occupied! Choose another one!
Enter the coordinates: two two
You should enter numbers!
Enter the coordinates: 1 4
Coordinates should be from 1 to 3!
Enter the coordinates: 1 1
---------
| O     |
|   X   |
|       |
---------
Enter the coordinates: 3 3
---------
| O     |
|   X   |
|     X |
---------
Enter the coordinates: 2 1
---------
| O     |
| O X   |
|     X |
---------
Enter the coordinates: 3 1
---------
| O     |
| O X   |
| X   X |
---------
Enter the coordinates: 2 3
---------
| O     |
| O X O |
| X   X |
---------
Enter the coordinates: 3 2
---------
| O     |
| O X O |
| X X X |
---------
X wins
```

## Customization

The game can be customised by changing the spaces on the grid from an underscore '`_`' to any other custom value like a space '` `' for example.
