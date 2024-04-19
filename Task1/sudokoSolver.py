
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]



def solve(bo):
    """
    solves the board and Returns True if it is solved else False
 
    Args:
        bo (list): The board to be solved
         
 
    Returns:
        Bool : True or False
    """
    
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    """
    Validate the row and col of for a number
    Args:
        bo (list): The board to be solved
        num (int): The number to be inserted  
        pos (tuple): The position of empty spot  
 
    Returns:
        Bool : True or False
    """
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    """
    Print the board and Returns None
 
    Args:
        bo (list): The board to be solved 
 
    Returns:
        None
    """
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    """
    Find the empty spot and Return a Tuple 
 
    Args:
        bo (list): The board to be solved 
 
    Returns:
        Tuple : The position of empty spot
    """
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)
solve(board)
print("  ___________________")
if find_empty(board):
    print("Board cannot be solved")
else:    
    print("solved")
    print_board(board)