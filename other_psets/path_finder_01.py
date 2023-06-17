def path_finder(maze: str):

    grid = []
    for row in maze.split("\n"):
        row = []
        for column in row:
            if column == ".":
                row.append(1)
            elif column == "W":
                row.append(0)
        grid.append(row)
    
    x_length = len(grid)
    queue = [(0, 0, 0)] # row, colum, length
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    while queue:
        x, y, length = queue.pop(0)
        if x == x_length - 1 and y == x_length -1:
            return length
        
        for move in moves:
            increment_x, increment_y = move
            next_x = x + increment_x
            next_y = y + increment_y

            if ((next_x < 0 or next_x >= x_length) or 
            (next_y < 0 or next_y >= x_length) or grid[next_x][next_y] == 0):
                continue

            grid[next_x][next_y] = 0    
            queue.append((next_x, next_y, length + 1))
    
    return False