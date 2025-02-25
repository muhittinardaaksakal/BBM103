import sys
# Read the input file and initialize the grid
input_file = open(sys.argv[1], "r")


grid = []

for line in input_file:
    row = line.split()
    grid.append(row)

first_board = ""
for row in grid:
    first_board += " ".join(row) + "\n"

# Display the initial grid

print(first_board)
print("Your score is: 0")
print()


def check(grid, row, col, n):
    # Recursive function to check and remove adjacent cells with the same number
    global score
    if row > 0 and grid[row-1][col] == n:
        grid[row-1][col] = " "
        score += int(n)

        check(grid, row-1, col, n)

    if row < len(grid) - 1 and grid[row+1][col] == n:
        grid[row+1][col] = " "

        score += int(n)

        check(grid, row+1, col, n)

    if col > 0 and grid[row][col-1] == n:
        grid[row][col-1] = " "

        score += int(n)
        check(grid, row, col-1, n)

    if col < len(grid[0]) - 1 and grid[row][col+1] == n:
        grid[row][col+1] = " "

        score += int(n)
        check(grid, row, col+1, n)


def is_valid_move(grid, row, col):
    # Check if the move is within bounds and not an empty cell
    if row > len(grid) - 1 or col > len(grid[0]) - 1 or grid[row][col] == " ":
        print("Please enter a correct size!")
        print()
        return False
    else:
        # Get the number at the selected coordinate
        n = grid[row][col]
        # Check for chosen cell's neighbors
        is_unnecessary_move(grid, row, col, n)
        check(grid, row, col, n)
        return True


def up_down_shifting(grid):
    # Shift non-empty cells down
    if len(grid) > 0 and len(grid) > 0:
        for y in range(len(grid[0])):
            for x in range(len(grid)-2, -1, -1):

                while x < len(grid) - 1 and grid[x][y] != " " and grid[x+1][y] == " ":
                    grid[x][y], grid[x+1][y] = grid[x+1][y], grid[x][y]
                    x += 1


def left_right_shifting(grid):
    # If all elements in a column become empty, shift the columns to the left of it to the left
    if len(grid) > 0 and len(grid) > 0:
        for y in range(len(grid[0]) - 1, -1, -1):
            counter = 0
            for x in range(len(grid)):
                if grid[x][y] == " ":
                    counter = counter + 1
            if counter == len(grid):
                for row in grid:
                    row.pop(y)


def is_unnecessary_move(grid, row, col, n):
    # Check if the selected cell has a different or same neighbor
    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

    for x in neighbors:
        neighbor_row = x[0]
        neighbor_col = x[1]

        if 0 <= neighbor_row <= len(grid) - 1 and 0 <= neighbor_col <= len(grid[0]) - 1 and grid[neighbor_row][neighbor_col] != " " and grid[neighbor_row][neighbor_col] == n:

            return True  # There exist a same neighbor
    print("No movement happened try again")
    print()
    return False  # For selected cell all neighbors are different number


def check_game_over(grid):
    # Check if the game is over
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != " ":
                current_number = grid[row][col]

                # Check neighbors (up, down, left, right)
                neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

                for x in neighbors:
                    neighbor_row = x[0]
                    neighbor_col = x[1]
                    if 0 <= neighbor_row <= len(grid) - 1 and 0 <= neighbor_col <= len(grid[0]) - 1 and grid[neighbor_row][neighbor_col] == current_number:

                        return False  # At least one neighboring cell has the same number and game is keep going

    return True  # No neighboring cells with the same number found, game over


def delete_empty_row(grid):
    # Delete rows that contain only empty cells
    rows_to_delete = []
    for row in range(len(grid)):
        counter = 0
        for col in range(len(grid[0])):
            if grid[row][col] == " ":
                counter += 1
        if counter == len(grid[0]):
            rows_to_delete.append(row)

    rows_to_delete.reverse()  # Reverse the list to delete rows from bottom to top
    for row in rows_to_delete:
        grid.pop(row)


score = 0
while True:
    if check_game_over(grid):

        print("Game Over")
        break
    inputs = input("Please enter a row and a column number: ")
    print()
    input_list = inputs.split()

    row = int(input_list[0]) - 1
    col = int(input_list[1]) - 1

    if not is_valid_move(grid, row, col):
        continue

    delete_empty_row(grid)
    up_down_shifting(grid)

    left_right_shifting(grid)

    result_board = ""
    for row in grid:
        result_board += " ".join(row) + "\n"

    # Display the updated board
    print(result_board)
    print("Your score is:", score)
    print()
