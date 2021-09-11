def print_grid():
    # declare grid border strings to print
    horizontal_line = '---------'
    vertical_line = '|'

    # print strings to make grid
    print(horizontal_line)
    for row in grid:
        # commas in print() produce spaced output
        print(vertical_line, row[0], row[1], row[2], vertical_line)
    print(horizontal_line)


def number_of(symbol):
    count = 0
    for row in grid:
        if row[0] is symbol:
            count += 1
        if row[1] is symbol:
            count += 1
        if row[2] is symbol:
            count += 1
    return count


def is_winner(symbol):
    # winner is determined by 3 of the same symbols in a row - vertically, horizontally, or diagonally.

    # test horizontally (rows)
    for row in grid:
        if all([cell is symbol for cell in row]):
            return True

    # test vertically (columns)
    #
    # invert 2D list
    # Solution 1:
    #   grid_columns = [[grid[0][i],
    #                    grid[1][i],
    #                    grid[2][i]]
    #                   for i in range(0, 3)]
    # Solution 2:
    #   zip(*grid) makes the grid list inverse, but outputs it as as tuple, which is an immutable list.
    for column in zip(*grid):
        if all([cell is symbol for cell in column]):
            return True

    # test diagonally
    # top-left to bottom-right
    if grid[0][0] is grid[1][1] and grid[2][2] is grid[1][1] and grid[1][1] is symbol:
        return True
    # top-right to bottom-left
    elif grid[0][2] is grid[1][1] and grid[2][0] is grid[1][1] and grid[1][1] is symbol:
        return True
    return False


def is_grid_full():
    # not a blank space in any row
    return not any([blank_space in row for row in grid])


def game_state():
    game_not_finished_str = 'Game not finished'
    draw_str = 'Draw'
    x_wins_str = 'X wins'
    o_wins_str = 'O wins'
    impossible_str = 'Impossible'

    # test the difference in player turns
    if abs(number_of('O') - number_of('X')) >= 2:
        # print(impossible_str)
        return False
    # both players can't win
    elif is_winner('X') and is_winner('O'):
        # print(impossible_str)
        return False
    elif is_winner('X'):
        print(x_wins_str)
        return False
    elif is_winner('O'):
        print(o_wins_str)
        return False
    elif is_grid_full():
        print(draw_str)
        return False
    else:
        # print(game_not_finished_str)
        return True


def take_turn(symbol):
    while True:
        # get user input
        inp_coords_str = input('Enter the coordinates: ')
        coords = inp_coords_str.split()
        # validate user input
        # is numeric
        if not all([coord.isnumeric() for coord in coords]):
            print('You should enter numbers!')
            continue
        coords = [int(coord) for coord in coords]
        # is within range
        if not all([1 <= coord <= 3 for coord in coords]):
            print('Coordinates should be from 1 to 3!')
            continue
        # is a free space
        if not grid[coords[0] - 1][coords[1] - 1] is blank_space:
            print('This cell is occupied! Choose another one!')
            continue
        break
    # update grid
    grid[coords[0] - 1][coords[1] - 1] = symbol
    print_grid()
    return


blank_space = '_'
grid = [[blank_space for column in range(0, 3)] for row in range(0, 3)]
print_grid()

turn = 'X'
while game_state():
    take_turn(turn)
    turn = 'O' if turn == 'X' else 'X'
