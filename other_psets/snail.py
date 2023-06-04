def snail(snail_map) -> list:
    
    rows = len(snail_map[0])
    columns = len(snail_map)
    total_number = rows * columns
    result = []
    sequence = [(0,1), (1,0), (0,-1), (-1,0)]
    cur_column, cur_row = 0, 0

    while len(result) < total_number:

        new_column, new_row = sequence.pop(0)
        if snail_map[cur_column][cur_row] != 0:
            result.append(snail_map[cur_column][cur_row])
        snail_map[cur_column][cur_row] = 0
        
        while True:
            next_column = cur_column + new_column
            next_row = cur_row + new_row
            if next_row >= rows or next_column >= columns:
                break
            if snail_map[next_column][next_row] == 0:
                break
            
            cur_column, cur_row = next_column, next_row
            result.append(snail_map[cur_column][cur_row])
            snail_map[cur_column][cur_row] = 0
        
        sequence.append((new_column,new_row))
    
    return result