def destroy_ship(matrix, coordinates) -> int:
    destroyed = 0

    # we refactor the coordinates so we can use them as matrix indexes
    coordinates = [i.replace("-","") for i in coordinates]

    # we use the above refactored string as indexes to check the values in the 
    # row's list
    for index in coordinates:

        index_0 = int(index[0])
        index_1 = int(index[1])

        if matrix[index_0][index_1] > 1:
            matrix[index_0][index_1] -= 1

        elif matrix[index_0][index_1] == 1:
            matrix[index_0][index_1] -= 1
            
            destroyed += 1

    return destroyed

def main():
    number_rows = int(input())

    battle_field = [] 

    for _ in range(number_rows):
        # we create a list of int's to append to the list above
        battle_field.append([int(i) for i in input().split()]) 

    # we take a input string of of coordinates like {num}-{num}
    # we will refactor this in the ship_destroyed function
    attack_coordinates_string = input().split(" ")

    return destroy_ship(battle_field, attack_coordinates_string)

if __name__ == "__main__":
    main()
