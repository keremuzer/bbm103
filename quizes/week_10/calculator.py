import sys


def read_file(input_file):
    """Reads the input file and returns a list of non-empty lines"""
    try:
        with open(input_file, 'r') as file:
            inputs = [line.strip() for line in file if line.strip() != ""]
        return inputs
    except (FileNotFoundError, PermissionError):
        print(f"ERROR: There is either no such a file namely {input_file} or this program does not have permission to "
              "read it!")
        print("Program is going to terminate!")
        return


def write_line(line):
    """Appends a line to the output file"""
    output_file = sys.argv[2]
    with open(output_file, 'a') as file:
        if file.tell() != 0:
            file.write("\n")
        file.write(line)


def calculate(line):
    """Makes a calculation based on input line and writes the result or error to output file """
    try:
        write_line(line)
        if len(line.split(" ")) != 3:
            raise ValueError("ERROR: Line format is erroneous!")
        operand1, operator, operand2 = line.split(" ")
        try:
            operand1 = float(operand1)
        except ValueError:
            write_line("ERROR: First operand is not a number!")
            return
        try:
            operand2 = float(operand2)
        except ValueError:
            write_line("ERROR: Second operand is not a number!")
            return
        try:
            if operator == "+":
                result = operand1 + operand2
            elif operator == "-":
                result = operand1 - operand2
            elif operator == "*":
                result = operand1 * operand2
            elif operator == "/":
                result = operand1 / operand2
            else:
                raise ValueError("ERROR: There is no such an operator!")
            write_line(f"={result:.2f}")
        except ValueError as e:
            write_line(str(e))
            return
    except ValueError as e:
        write_line(str(e))
        return


def main():
    try:
        if len(sys.argv) != 3:
            raise IndexError
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        with open(output_file, 'w') as file:
            file.write("")  # clear the output file or create one
        inputs = read_file(input_file)
        if inputs is not None:
            for line in inputs:
                calculate(line)
    except IndexError:
        print("ERROR: This program needs two command line arguments to run, where first one is the input file and the "
              "second one is the output file!")
        print("Sample run command is as follows: python3 calculator.py input.txt output.txt")
        print("Program is going to terminate!")
        return


if __name__ == '__main__':
    main()
