def grid() -> list:
    matrix = []
    for _ in range(8):
        row = input().split()
        matrix.append(row)
    return matrix


# recursive function to check if a queen is threatening the king
def validate_checkmate(curr_position: list, move: tuple) -> bool:
    # get the current position, and one of eight grid traversal moves
    # we create a new grid position variable for columns and rows
    next_column, next_row = move
    current_column, current_row = curr_position
    new_column = current_column + next_column
    new_row = current_row + next_row
    
    # series of "base conditions" checks for our recursive function calls
    # these two conditions check if the next cell is out of bonds
    if ((new_column < 0 or new_column >= columns) 
        or (new_row < 0 or new_row >= rows)):
        return False

    # this condition checks if between the queen and king there is
    # another queen thus making the current queen a invalid threat
    if chess_board[new_column][new_row] == "Q":
        return False
    # if we find a king in any of the queens grid moves we return True
    # since we can checkmate the king
    if chess_board[new_column][new_row] == "K":
        return True
    # if all above base cases fail we use this function to 
    # check the next cell from our new current position 
    return validate_checkmate([new_column, new_row], move)


def get_row(matrix: list) -> int:
    return len(matrix)


def get_column(matrix: list) -> int:
    return len(matrix[0])


chess_board = grid()
columns = get_column(chess_board)
rows = get_row(chess_board)
# the grid vectors or "queen moves"
queen_moves = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), 
               (-1, 1), (0, 1), (1, 1))
checkmate = []

# we iterate over every item in the grid "chess board" 
# to find a queen and check if she is a threat to the king
for column in range(columns):
    for row in range(rows):

        if chess_board[column][row] == "Q":
            queen_position = [column, row]

            for move in queen_moves:
                new_column, new_row = move
                position = [column, row]

                if validate_checkmate(position, move):
                    checkmate.append(queen_position)

if checkmate:
    print(*checkmate, sep="\n")
else:
    print("The king is safe!")

#####################################
#  version two - with no functions  #
#####################################

# grid = []
# for _ in range(8):
#     row = input().split()
#     grid.append(row)
   
# columns = len(grid[0])
# rows = len(grid)

# queen_moves = ((-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1))
# checkmate = []
    
# for column in range(columns):
#     for row in range(rows):

#         if grid[column][row] == "Q":
                
#             queen_position = [column, row]

#             for move in queen_moves:
#                 new_column, new_row = move
#                 current_column, current_row = column, row                    

#                 while True:
#                     next_column = current_column + new_column
#                     next_row = current_row + new_row
                        
#                     if next_column < 0 or next_column >= columns:
#                         break
#                     if next_row < 0 or next_row >= rows:
#                         break
                        
#                     if grid[next_column][next_row] == "Q":
#                         break
#                     if grid[next_column][next_row] == "K":
#                         checkmate.append(queen_position)
#                         break
                        
#                     current_column, current_row = next_column, next_row
    
# if checkmate:
#     print(*checkmate, sep="\n")
# else:
#     print("The king is safe!")