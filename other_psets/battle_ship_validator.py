def validate_battlefield(field) -> bool:

    length_row = len(field[0])
    length_column = len(field)

    moves = ((-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1))
    objects = []
    battleship = 0
    cruisers = 0
    destroyers = 0
    submarine = 0

    for column in range(length_column):
        for row in range(length_row):

            if field[column][row] == 1:
                neighbors = [(column, row)]
                field[column][row] = 0
                moves_used = [(column, row)]
                
                while neighbors:
                    idx_0, idx_1 = neighbors.pop(0)
                    
                    for move in moves:
                        
                        new_column, new_row = move
                        next_column = idx_0 + new_column
                        next_row = idx_1 + new_row

                        if next_column < 0 or next_column >= length_column:
                            continue
                        if next_row < 0 or next_row >= length_row:
                            continue

                        if field[next_column][next_row] == 1:
                            neighbors.append((next_column, next_row))
                            field[next_column][next_row] = 0
                            moves_used.append(move)
                
                objects.append(moves_used)

    for ship in objects:
        ship_type = len(ship)
        if len(set(ship)) == 2 or len(set(ship)) == 1:
            match ship_type:
                case 4:
                    battleship += 1
                case 3:
                    cruisers += 1
                case 2:
                    destroyers += 1
                case 1:
                    submarine += 1

    if battleship == 1 and cruisers == 2 and destroyers == 3 and submarine == 4:
        return True
    return False