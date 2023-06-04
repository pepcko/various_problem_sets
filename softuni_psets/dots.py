def longest_area(matrix) -> int:
    # we get the number of row's and columns, so we can check if a
    # BFS search move is out of bounds
    rows = len(matrix[0])
    columns = len(matrix)

    # we create a list that will store all the BFS calls
    # and a list of tuples with the move coordinates for BFS
    answer = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # we start looping though the matrix
    for column in range(columns):
        for row in range(len(matrix[0])):

            # if we find a dot we initialize the BFS
            if matrix[column][row] == ".":

                # we create a queue with the dots coordinates
                # and change it to a dash, so we don't look for it again
                queue = [(column, row)]
                matrix[column][row] = "-"
                result = 0

                while queue:
                    idx_0, idx_1 = queue.pop(0)
                    result += 1

                    # we loop through all our moves
                    for move in moves:
                        new_colum, new_row = move

                        neighbor_column = idx_0 + new_colum
                        neighbor_row = idx_1 + new_row

                        # we check to see if the next move is out of bonds
                        if neighbor_column < 0 or neighbor_column >= columns:
                            continue
                        if neighbor_row >= rows or neighbor_row < 0:
                            continue

                        # if we find a dot we add its coordinates to the
                        # queue, so we can search its neighbors
                        if matrix[neighbor_column][neighbor_row] == ".":
                            queue.append((neighbor_column, neighbor_row))
                            matrix[neighbor_column][neighbor_row] = "-"

                answer.append(result)
    
    if answer:
        return max(answer)
    return 0


def main():
    number = int(input())

    # we create the matrix with a given 
    # number of columns and the given rows
    board = []
    for _ in range(number):
        board.append(input().split())

    return print(longest_area(board))

if __name__ == "__main__":
    main()
