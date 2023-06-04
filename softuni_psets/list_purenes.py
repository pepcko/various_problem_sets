def best_list_pureness(list_arg: list[int], number_k) -> str:
    best_pureness = -float("inf")
    rotation = 0
    
    for rotations in range(number_k + 1):
        result = 0
        for index, value in enumerate(list_arg):
            result += index * value
            if result > best_pureness:
                best_pureness = result
                rotation = rotations
        
        last_value = list_arg.pop()
        list_arg.insert(0, last_value)

    return f"Best pureness {best_pureness} after {rotation} rotations"

def main():
        test = ([7, 9, 2, 5, 3, 4], 3)
        result = best_list_pureness(*test)
        return print(result)
        
if __name__ == "__main__":
    main()
