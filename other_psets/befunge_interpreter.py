# Befunge Interpreter

from random import choice


def get_field(code: str) -> list:
    return [x for x in code.split("\n")]


def math(a: int, b: int, curr: str) -> int:
    result = 0
    if curr == "+":
        result =  a + b
    elif curr == "-":
        result =  b - a
    elif curr == "*":
        result =  a * b
    elif curr == "/" or "//":
        if a != 0:  
            result =  int(b / a)
    elif curr == "%":
        if a != 0:  
            result =  b % a
    return result


def if_pop(x_value: int, curr_symbol: str):  
    if curr_symbol == "_":
        if x_value == 0:
            return ">"
        return "<"
    elif curr_symbol == "|":
        if x_value == 0:
            return "v"
        return "^"


def not_operator(value: int) -> int:
    if value == 0:
        return 1
    return 0


def backtick(x_value: int, y_value: int) -> int:
    if y_value > x_value:
        return 1
    return 0


def random_direction(moves: dict) -> tuple:
    return choice(list(moves.values()))    


def swap_top_two(stack: list) -> list:
    if len(stack) == 1:
        stack.append(0)
    else:
        stack_one, stack_two = stack[-1], stack[-2]
        stack[-1], stack[-2] = stack_two, stack_one
    return stack

def put(x_value: int, y_value: int, filed: list, value: int) -> str:
    ascii_value = chr(value)
    column = filed[y_value]
    new_column = column[:x_value] + ascii_value + column[x_value + 1:]
    return new_column


def duplicate(stack: list) -> int:
    if len(stack) == 0:
        return 0
    else:
        last_item = stack[-1]
        return last_item


def interpret(code: str) -> str:
    
    field = get_field(code)
    stack = []
    moves = {
        ">": (0, 1), # default starting move
        "<": (0, -1),
        "^": (-1, 0),
        "v": (1, 0)
    }

    math_operators = ("+", "-", "*", "/", "%")    
    curr_column, curr_row = 0, 0
    curr_symbol = field[0][0]
    curr_move = moves[">"]
    string_mode = False
    output = ""    
    rotations = 0
    while curr_symbol != "@":
        rotations += 1
        if string_mode:
            if curr_symbol != '"':
                stack.append(ord(curr_symbol))
            else:
                string_mode = False
        elif curr_symbol == " ":
            pass            
        elif curr_symbol in math_operators:
            x_value = stack.pop()
            y_value = stack.pop()
            stack.append(math(x_value, y_value, curr_symbol))
        elif curr_symbol in moves:
            curr_move = moves[curr_symbol]
        elif curr_symbol == "!":
            x_value = stack.pop()
            stack.append(not_operator(x_value))
        elif curr_symbol == "`":
            x_value = stack.pop()
            y_value = stack.pop()
            stack.append(backtick(x_value, y_value))
        elif curr_symbol == "_" or curr_symbol == "|":
            x_value = stack.pop()
            curr_move = moves[if_pop(x_value, curr_symbol)] #type: ignore
        elif curr_symbol == '"':
            string_mode = True
        elif curr_symbol == ":":
            stack.append(duplicate(stack))
        elif curr_symbol == "\\":
            stack = swap_top_two(stack)
        elif curr_symbol == "$":
            stack.pop()
        elif curr_symbol == ".":
            stack_one = stack.pop()
            output += f"{stack_one}"
        elif curr_symbol == ",":
            stack_one = stack.pop()
            output += f"{chr(stack_one)}"
        elif curr_symbol == "#":
            increment_column, increment_row = curr_move 
            curr_column += increment_column 
            curr_row += increment_row  
        elif curr_symbol == "p":
            y_value = stack.pop()
            x_value = stack.pop()
            v_value = stack.pop()
            field[y_value] = put(x_value, y_value, field, v_value)
        elif curr_symbol == "g":
            field_colum = stack.pop()
            field_row = stack.pop()
            stack.append(ord(field[field_colum][field_row]))
        elif curr_symbol == "?":
            curr_move = random_direction(moves)
        else:
            stack.append(int(curr_symbol))
            
        increment_column, increment_row = curr_move  
        curr_column += increment_column 
        curr_row += increment_row 
        curr_symbol = field[curr_column][curr_row]

    return output

