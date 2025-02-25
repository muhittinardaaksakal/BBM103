import sys


def constraint_check(board, conditions):
    # Check if the current board configuration satisfies the given constraints for each row and column
    # Returns True if the constraints are met, False otherwise
    # Constraints are provided in the 'conditions' list
    for i in range(len(board)):
        # Check the number of occurrences of "H" in each row
        if int(conditions[0][i]) != -1:
            if board[i].count("H") != int(conditions[0][i]):
                return False

    for i in range(len(board)):
        # Check the number of occurrences of "B" in each row
        if int(conditions[1][i]) != -1:
            if board[i].count("B") != int(conditions[1][i]):
                return False

    for i in range(len(board[0])):
        # Check the number of occurrences of "H" in each column
        counter = 0
        if int(conditions[2][i]) != -1:
            for j in range(len(board)):

                if board[j][i] == "H":
                    counter += 1
            if counter != int(conditions[2][i]):
                return False

    for i in range(len(board[0])):
        # Check the number of occurrences of "B" in each column
        counter = 0
        if int(conditions[3][i]) != -1:
            for j in range(len(board)):

                if board[j][i] == "B":
                    counter += 1
            if counter != int(conditions[3][i]):
                return False

    return True


def ud_hb_corner_check(board, row, col):
    # Check neighbors for placing "HB" tile in an upward direction
    # Returns True if the placement is valid, False otherwise
    if row - 1 >= 0 and board[row - 1][col] == "H":
        return False
    if col - 1 >= 0 and board[row][col - 1] == "H":
        return False
    if row + 1 < len(board) and col - 1 >= 0 and board[row + 1][col - 1] == "B":
        return False
    if col + 1 < len(board[0]) and board[row][col + 1] == "H":
        return False
    return True


def ud_bh_corner_check(board, row, col):
    # Check neighbors for placing "BH" tile an upward direction
    # Returns True if the placement is valid, False otherwise.
    if row - 1 >= 0 and board[row - 1][col] == "B":
        return False
    if col - 1 >= 0 and board[row][col - 1] == "B":
        return False
    if row + 1 < len(board) and col - 1 >= 0 and board[row + 1][col - 1] == "H":
        return False
    if col + 1 < len(board[0]) and board[row][col + 1] == "B":
        return False
    return True


def lr_hb_corner_check(board, row, col):
    # Check neighbors for placing "HB" tile a horizontal direction
    # Returns True if the placement is valid, False otherwise.
    if row - 1 >= 0 and board[row - 1][col] == "H":
        return False
    if col - 1 >= 0 and board[row][col - 1] == "H":
        return False
    if col + 2 < len(board[0]) and board[row][col + 2] == "B":
        return False
    if row - 1 >= 0 and col + 1 < len(board[0]) and board[row - 1][col + 1] == "B":
        return False
    return True


def lr_bh_corner_check(board, row, col):
    # Check neighbors for placing "BH" tile a horizontal direction
    # Returns True if the placement is valid, False otherwise.
    if row - 1 >= 0 and board[row - 1][col] == "B":
        return False
    if col - 1 >= 0 and board[row][col - 1] == "B":
        return False
    if col + 2 < len(board[0]) and board[row][col + 2] == "H":
        return False
    if row - 1 >= 0 and col + 1 < len(board[0]) and board[row - 1][col + 1] == "H":
        return False
    return True


def gamesolver(board, row, col, conditions):
    # Recursive backtracking algorithm to explore possible moves and find a valid solution
    if col == len(board[0]):
        if row == len(board) - 1:
            return constraint_check(board, conditions)

        row += 1
        col = 0

    if board[row][col] == "N" or board[row][col] == "H" or board[row][col] == "B":
        # When a cell is already filled,move to the next cell
        return gamesolver(board, row, col + 1, conditions)

    if board[row][col] == "U":
        # When a cell is in upward direction try making a move in the vertical direction
        for move in ["HB", "BH", "NN"]:
            if move[0] == "H" and ud_hb_corner_check(board, row, col):
                board[row][col] = "H"
                board[row + 1][col] = "B"
                if gamesolver(board, row, col + 1, conditions):
                    return True
                # Undo the move
                board[row][col] = "U"
                board[row + 1][col] = "D"

            elif move[0] == "B" and ud_bh_corner_check(board, row, col):
                board[row][col] = "B"
                board[row + 1][col] = "H"
                if gamesolver(board, row, col + 1, conditions):
                    return True
                # Undo the move
                board[row][col] = "U"
                board[row + 1][col] = "D"

            elif move[0] == "N":
                board[row][col] = "N"
                board[row + 1][col] = "N"
                if gamesolver(board, row, col + 1, conditions):
                    return True
                # Undo the move
                board[row][col] = "U"
                board[row + 1][col] = "D"

    elif board[row][col] == "L":
        # When a cell is in horizontal direction try making a move in the horizontal direction
        for move in ["HB", "BH", "NN"]:
            if move[0] == "H" and lr_hb_corner_check(board, row, col):
                board[row][col] = "H"
                board[row][col + 1] = "B"
                if gamesolver(board, row, col + 1, conditions):
                    return True
                # Undo the move
                board[row][col] = "L"
                board[row][col + 1] = "R"

            elif move[0] == "B" and lr_bh_corner_check(board, row, col):
                board[row][col] = "B"
                board[row][col + 1] = "H"
                if gamesolver(board, row, col + 1, conditions):
                    return True
                # Undo the move
                board[row][col] = "L"
                board[row][col + 1] = "R"

            elif move[0] == "N":
                board[row][col] = "N"
                board[row][col + 1] = "N"
                if gamesolver(board, row, col + 1, conditions):
                    return True
                # Undo the move
                board[row][col] = "L"
                board[row][col + 1] = "R"

    return False  # There is no solution for this board


def print_board(board, output_file):
    # Print the final board configuration to the output file.
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j == len(board[0]) - 1:
                output_file.write(board[i][j])
            else:
                output_file.write(board[i][j] + " ")
        if i != len(board) - 1:
            output_file.write("\n")


def main():
    # Open input and output files
    input_file = open(sys.argv[1], "r")
    output_file = open(sys.argv[2], "w")

    # Read the first 4 lines into the 'conditions' list
    conditions = []
    for _ in range(4):
        line = input_file.readline()
        conditions.append(line.split())

    # Read the rest of the lines into the 'board' list
    board = []
    for line in input_file:
        board.append(line.split())

    # Close the input file
    input_file.close()
    if gamesolver(board, 0, 0, conditions):

        print_board(board, output_file)
    else:
        output_file.write("No solution!")
    output_file.flush()
    output_file.close()


if __name__ == "__main__":
    main()
