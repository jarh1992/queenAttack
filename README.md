# Queens Attack
*Based in the test Queens Attack which the objective is calculate How many movements can do the queen in a chess board with obstacles. The text and images here are not of my authoship, just the queen.py code*

You will be given a square chess board with one queen and a number of obstacles placed on it. Determine how many squares the queen can attack. 

A queen is standing on an n x n  chessboard. The chess board's rows are numbered from 1 to n , going from bottom to top. Its columns are numbered from 1 to n, going from left to right. Each square is referenced by a tuple, (r,c) , describing the row, r , and column, c , where the square is located.

The queen is standing at position (rq, cq) . In a single move, she can attack any square in any of the eight directions (left, right, up, down, and the four diagonals). In the diagram below, the green circles denote all the cells the queen can attack from (4,4):

<img src="https://raw.githubusercontent.com/jarh1992/queenAttack/master/image001.png" width="300" height="300" />

There are obstacles on the chessboard, each preventing the queen from attacking any square beyond it on that path. For example, an obstacle at location (3,5)  in the diagram above prevents the queen from attacking cells (3,5), (2,6), (1,7)

<img src="https://raw.githubusercontent.com/jarh1992/queenAttack/master/image002.png" width="300" height="300" />

Given the queen's position and the locations of all the obstacles, find and print the number of squares the queen can attack from her position at (rq, cq) . In the board above, there are 24 such squares.

**Function Description**

The function should receive as input a string that will be read from a file. It should return an integer that describes the number of squares the queen can attack.

queensAttack has the following parameters: 
- n: an integer, the number of rows and columns in the board 
- k: an integer, the number of obstacles on the board 
- r_q: integer, the row number of the queen's position 
- c_q: integer, the column number of the queen's position 
- obstacles: a two dimensional array of integers where each element is an array of 2 integers, the row and column of an obstacle

**Input Format**

    - The first line contains two space-separated integers  and , the length of the board's sides and the number of obstacles.
    - The next line contains two space-separated integers  and , the queen's row and column position.
    - Each of the next  lines contains two space-separated integers  and , the row and column position of .

**Constraints**

    - 0 < n <= 10^5
    - 0 <= k <= 10^5
    - A single cell may contain more than one obstacle
    - There will never be an obstacle at the position where the queen is located

**How to run it:**
- Requirements: Python 3.6 and add it to env vars
- Go to the terminal and write: $ queen.py sample.txt
