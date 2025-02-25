import sys


def native_fib(n, output_naive_file):
    # Function to calculate Fibonacci numbers with detailed recursive steps
    # Base cases for Fibonacci sequence
    if n == 1:
        output_naive_file.write("fib(1) = 1")
        output_naive_file.write("\n")
        return 1
    elif n == 2:
        output_naive_file.write("fib(2) = 1")
        output_naive_file.write("\n")
        return 1
    else:
        # Print the current recursive call
        output_naive_file.write("fib({}) = fib({}) + fib({})".format(n, n-1, n-2))
        output_naive_file.write("\n")
        # Recursive calls and sum of the results
        return native_fib(n - 1, output_naive_file) + native_fib(n - 2, output_naive_file)


fibonacci_sequence = [1, 1]


def eager_fib(n, output_eager_file):

    if n == 1:

        return 1

    elif n == 2:

        return 1
    else:
        while n > len(fibonacci_sequence):
            output_eager_file.write("fib({}) = fib({}) + fib({})".format(n, n - 1, n - 2))
            output_eager_file.write("\n")
            fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

        return fibonacci_sequence[n - 1]


def main():
    input_file = open(sys.argv[1], "r")
    output_naive_file = open(sys.argv[2], "w")
    number_string = input_file.read().split()
    output_eager_file = open(sys.argv[3], "w")
    numbers = []

    for number in number_string:
        number = int(number)
        numbers.append(number)
    for number in numbers:
        if number <= 0:
            # Handle non-positive numbers
            output_naive_file.write(32 * "-")
            output_naive_file.write("\n")
            output_naive_file.write("Calculating {}. Fibonacci number:".format(number))
            output_naive_file.write("\n")
            output_naive_file.write("ERROR: Fibonacci cannot be calculated for the non-positive numbers!")
            output_naive_file.write("\n")
            output_naive_file.write("{}. Fibonacci number is: nan".format(number))
            output_naive_file.write("\n")
        else:
            output_naive_file.write(32 * "-")
            output_naive_file.write("\n")
            # Calculate Fibonacci number using the naive approach
            output_naive_file.write("Calculating {}. Fibonacci number:".format(number))
            output_naive_file.write("\n")

            result = native_fib(number, output_naive_file)
            output_naive_file.write("{}. Fibonacci number is: {}".format(number, result))
            output_naive_file.write("\n")
    output_naive_file.write(32*"-")
    output_naive_file.flush()
    output_naive_file.close()
    for number in numbers:
        if number <= 0:
            output_eager_file.write(32 * "-")
            output_eager_file.write("\n")
            output_eager_file.write("Calculating {}. Fibonacci number:".format(number))
            output_eager_file.write("\n")
            output_eager_file.write("ERROR: Fibonacci cannot be calculated for the non-positive numbers!")
            output_eager_file.write("\n")
            output_eager_file.write("{}. Fibonacci number is: nan".format(number))
            output_eager_file.write("\n")
        else:
            output_eager_file.write(32 * "-")
            output_eager_file.write("\n")
            output_eager_file.write("Calculating {}. Fibonacci number:".format(number))
            output_eager_file.write("\n")
            if number < len(fibonacci_sequence):
                output_eager_file.write("fib({}) = {}".format(number, fibonacci_sequence[number - 1]))
                output_eager_file.write("\n")
            if number - 1 == len(fibonacci_sequence):
                output_eager_file.write("fib({}) = {}".format(number, fibonacci_sequence[number - 2]))
                output_eager_file.write("\n")
                output_eager_file.write("fib({}) = {}".format(number, fibonacci_sequence[number - 3]))
                output_eager_file.write("\n")
                result = eager_fib(number, output_eager_file)
                output_eager_file.write("{}. Fibonacci number is: {}".format(number, result))
                output_eager_file.write("\n")

    output_eager_file.write(32*"-")
    output_eager_file.flush()
    output_eager_file.close()


if __name__ == "__main__":
    main()
