def knight(p1: str, p2: str) -> int:
    chess_board = []
    for _ in range(8):
        chess_board.append([1] * 8)
    
    length = 0
    start_position = (ord(p1[0]) - 97, int(p1[1]) - 1) # find the index by 
    end_position = (ord(p2[0]) - 97, int(p2[1]) - 1)   # converging to ascii                                                  
    column, row = start_position 
    chess_board[column][row] = 0
    queue = [(column, row, 0)] # third value is length
    # only way a knight might move on the chess board
    knight_moves = [(2, -1), (2, 1), (-2, 1), (-2, -1), 
                    (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    while queue:
        column, row, length = queue.pop(0)
        if column == end_position[0] and row == end_position[1]:
            return length
        
        for move in knight_moves:
            increment_column, increment_row = move
            next_column = column + increment_column
            next_row = row + increment_row

            if ((next_column < 0 or next_column > 7) 
                or (next_row < 0 or next_row > 7)
                or chess_board[next_column][next_row] == 0):
                continue

            chess_board[next_column][next_row] = 0
            queue.append((next_column, next_row, length + 1))
        
    return length

