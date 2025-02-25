import sys


def check_inputs():
    # Define custom exceptions for error handling
    class NumberOfArgumentsError(Exception):
        # Define a custom exception for if number of given arguments is not equal two
        pass

    class NameMatchError(Exception):
        # Define an error for the case where the entered argument name does not match
        pass

    class LineError(Exception):
        pass

    class OperandError(Exception):
        pass

    try:
        # Get output file name from command-line arguments
        output_file_name = sys.argv[2]
        # Check if the correct number of command-line arguments is provided
        if len(sys.argv) != 3:
            raise NumberOfArgumentsError

        # Get input file name from command-line arguments
        input_file_name = sys.argv[1]
        # Check if the input file name matches the expected value
        if input_file_name != "input.txt":
            raise NameMatchError

        results = []  # Collect the results

        # Open and read from the input file
        with open(input_file_name, "r") as input_file:
            # Iterate through each line in the input file
            for line in input_file:
                # Split the line into a list of strings
                input_string = line.split()

                # Check if the line is not empty
                if input_string == []:
                    continue

                try:
                    # Check if the line has the expected format
                    if len(input_string) != 3:
                        raise LineError
                except LineError:
                    results.append(f"{line.strip()}\nERROR: Line format is erroneous!")
                    continue

                # Extract operator from the line
                operand = input_string[1]

                try:
                    # Convert operands to float
                    operand1 = float(input_string[0])
                    operand2 = float(input_string[2])

                    # Perform the operation based on the operator
                    if operand == '+':
                        result = operand1 + operand2
                    elif operand == '-':
                        result = operand1 - operand2
                    elif operand == '*':
                        result = operand1 * operand2
                    elif operand == '/':
                        result = operand1 / operand2
                    else:
                        raise OperandError

                    # Append the result to the results list
                    results.append(f"{line.strip()}\n={result:.2f}")

                except ValueError:
                    results.append(f"{line.strip()}\nERROR: Operand is not a number!")

                except OperandError:
                    results.append(f"{line.strip()}\nERROR: There is no such an operator!")

        # Write all results to the output file
        with open(output_file_name, "w") as output_file:
            for result in results:
                output_file.write(result)
                output_file.write("\n")

    except NameMatchError:
        print(f'ERROR: There is either no such a file namely '
              f'{input_file_name} or this program does not have permission to read it!')

    except NumberOfArgumentsError:
        print("ERROR: This program needs two command line arguments to run, "
              "where the first one is the input file and the second one is the output file!")


def main():
    check_inputs()


if __name__ == "__main__":
    main()
