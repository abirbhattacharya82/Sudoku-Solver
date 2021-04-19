# Algorithm
-  Scan each row and find the empty box. Here the Empty boxes are represented by '0'.
- Put the first possible Number in that box and move onto the next empty box in the same row.
- At one point putting a certain number in a box might not be valid, that moment move back to previous box and delete the number. 
- Continue this entire process until all of the boxes are filled or in other words there are no '0' in the entire board.

# Explaining the Methods
- find_space(board): This method helps in finding the nearest empty box or the box containing '0' while scanning every row. If no empty box is found then it returns `None` else it returns the position of the box.
- check(board, num, r, c): This method helps in checking if the number `num` is already present in the the row `r` or column `c` or in the box. This is done in three ways.If the number is found then `False` is return else `True` is returned.
    1) checking if the number `num` is present in the row `r` by scanning through the row.
    2) checking if the number `num` is present in the column `c` by scanning through the column
    3) checking if the number `num` is present in the box. To do so the first thing to do is doing the integer division of the row `r` and column `c` and store it in a couple of variable lets say `x` and `y`. The next job is to find the index of the first box of the 3x3 box. This is done by multiplying the variables `x` and `y` by 3.
- solve(board): This method puts a number in the first found empty box and then checks if the number's position is valid or not. This is done with the help of two methods `find_space(board)` and `check(board,num,r,c)`.
- show(board): This method prints the board in the form of a Sudoku Table/Board. 
- enter_datas(board): This method takes the values from the puzzle setter.