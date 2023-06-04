def take_skip(string) -> str:

    # we take only the numbers from the provided string
    num_list = [int(i) for i in string if i.isdecimal()]

    # we take only the letters from the provided string
    letter_list = "".join([i for i in string if not i.isdecimal()])

    # we make two list the one with the numbers in every even index
    # and one with the odd index values
    take_list = [num_list[i] for i in range(len(num_list)) if i % 2 == 0]
    skip_list = [num_list[i] for i in range(len(num_list)) if i % 2 != 0]

    # this is going to be our new string
    taken_string = ""

    for index in range(len(take_list)):
        
        # we take every string with every value in the take list
        # and we skip with the values from the skip list
        taken_string += letter_list[:take_list[index]]
        letter_list = letter_list[take_list[index] + skip_list[index]:]
    
    return taken_string

def main():

    original_string = input()

    return take_skip(original_string)

if __name__ == "__main__":
    print(main())
