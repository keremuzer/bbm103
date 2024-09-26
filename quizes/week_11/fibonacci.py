import sys


def read_file(file):
    """Reads the input file and returns a list of integers that represents the game board"""
    with open(file, 'r') as file:
        inputs = [int(line) for line in file]
    return inputs


def write_line(line, file):
    """Appends a line to the output file"""
    with open(file, 'a') as file:
        file.write(line)


def naive(n, output_file):
    """Calculates the "n"th fibonacci number recursively using naive approach"""
    if n < 1:
        write_line("ERROR: Fibonacci cannot be calculated for the non-positive numbers!\n", output_file)
        return "nan"
    if n == 1 or n == 2:
        write_line(f"fib({n}) = {1}\n", output_file)
        return 1
    write_line(f"fib({n}) = fib({n - 1}) + fib({n - 2})\n", output_file)
    return naive(n - 1, output_file) + naive(n - 2, output_file)


def eager(n, solutions, output_file):
    """Calculates the "n"th fibonacci number recursively using eager approach"""
    if n < 1:
        write_line("ERROR: Fibonacci cannot be calculated for the non-positive numbers!\n", output_file)
        return "nan"
    if n <= len(solutions):
        write_line(f"fib({n}) = {solutions[n - 1]}\n", output_file)
        return solutions[n - 1]
    else:
        write_line(f"fib({n}) = fib({n - 1}) + fib({n - 2})\n", output_file)
        solutions.append(eager(n - 1, solutions, output_file) + eager(n - 2, solutions, output_file))
    return solutions[n - 1]


def main():
    """main function for taking input and managing program flow"""
    if len(sys.argv) != 4:
        print("Usage:  python3 fibonacci.py input.txt output_naive.txt output_eager.txt")
        return
    input_file = sys.argv[1]
    inputs = read_file(input_file)
    output_n = sys.argv[2]
    output_e = sys.argv[3]

    # clear output files or create them
    with open(output_n, 'w') as naive_output:
        naive_output.write("")
    with open(output_e, 'w') as eager_output:
        eager_output.write("")

    # write naive solutions to output file
    for i in inputs:
        write_line("-" * 32 + "\n" + f"Calculating {i}. Fibonacci number:\n", output_n)
        write_line(f"{i}. Fibonacci number is: {naive(i, output_n)}\n", output_n)
    write_line("-" * 32, output_n)

    # write eager solutions to output file
    solutions = [1, 1]
    for i in inputs:
        write_line("-" * 32 + "\n" + f"Calculating {i}. Fibonacci number:\n", output_e)
        write_line(f"{i}. Fibonacci number is: {eager(i, solutions, output_e)}\n", output_e)
    write_line(f"{'-' * 32}\nStructure for the eager solution:\n{solutions}\n{32 * '-'}", output_e)


if __name__ == '__main__':
    main()
