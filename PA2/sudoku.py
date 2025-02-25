import sys


def check(grid, row, col, number):
    # Check if number is present in the same row
    for i in range(9):
        if grid[row][i] == number:
            return False
    # Check if number is present in the same column
    for i in range(9):
        if grid[i][col] == number:
            return False
    # Check if number is present in the 3x3 subgrid
    corner_row = row - row % 3
    corner_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[corner_row + i][corner_col + j] == number:
                return False
    return True


def find_possibilities(grid, row, col):
    # Find possible numbers for the given cell by checking each number from 1 to 9
    # Evaluate how many possibilities there are
    possibilities = []
    for number in range(1, 10):
        if check(grid, row, col, number):
            possibilities.append(number)
    return possibilities


def is_sudoku_completed(grid):
    # Check if all cells are filled in the grid
    for column in grid:
        for cell in column:
            if cell == 0:
                return False
    return True


def solve(grid, step, output_file):
    for row in range(9):
        for col in range(9):
            if grid[row][col] > 0:
                # Skip cells if cells are already filled
                continue
            possibilities = find_possibilities(grid, row, col)
            if len(possibilities) == 1:
                # If there's only one possibility, fill the cell with appropriate number
                number_added = possibilities[0]
                # Write the step and the updated grid
                grid[row][col] = number_added

                value_of_row = row + 1
                value_of_col = col + 1
                step += 1
                output_file.write(
                    "------------------\nStep {} - {} @ R{}C{}\n------------------\n".format(step, number_added,
                                                                                             value_of_row,
                                                                                             value_of_col))

                for i in range(9):
                    for j in range(9):
                        if j == 8:
                            output_file.write(str(grid[i][j]))
                        else:
                            output_file.write(str(grid[i][j]) + " ")
                    output_file.write("\n")

                if solve(grid, step, output_file):
                    return True  # Exit the loop when the sudoku is completed

                grid[row][col] = 0  # Set the cell that does not decide which number to fill the cell with equal to 0

    # Check if the puzzle is completely solved
    if is_sudoku_completed(grid):
        return True


def main():
    # Open input and output files
    input_file = open(sys.argv[1], "r")
    output_file = open(sys.argv[2], "w")
    # Read Sudoku puzzle from input file and get a list of numbers
    sudoku_string = input_file.read().split()
    sudoku_integer = []
    for i in sudoku_string:
        j = int(i)
        sudoku_integer.append(j)

    grid = []

    for i in range(0, 81, 9):
        # Convert 1D list to a 2D grid (get 9x9 matrix)
        t = sudoku_integer[i:i + 9]
        grid.append(t)

    step = 0

    if solve(grid, step, output_file):
        output_file.write("------------------")

        output_file.flush()
        output_file.close()


if __name__ == "__main__":
    main()
