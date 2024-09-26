import sys


# read sudoku board from input file
def read_file(input_file):
    with open(input_file, 'r') as file:
        board = []
        for line in file:
            row = []
            for i in line:
                if i in "0123456789":
                    row.append(int(i))
            board.append(row)
        return board


# write sudoku board to output file after each step
def write_file(board, number, row_index, col_index, step):
    output_file = sys.argv[2]
    new_board = 18 * "-" + "\n" + f"Step {step} - {number} @ R{row_index}C{col_index}\n" + 18 * "-" + "\n"
    for row in board:
        for i in row:
            new_board += str(i) + " "
        new_board = new_board.rstrip()
        new_board += "\n"
    with open(output_file, 'a') as file:
        file.write(new_board)


# check row to get possible solutions
def control_row(row):
    possible_solutions = []
    for i in range(1, 10):
        if i not in row:
            possible_solutions.append(i)
    return possible_solutions


# check column to get possible solutions
def control_col(board, col_index):
    possible_solutions = []
    column = []
    for row in board:
        column.append(row[col_index])
    for i in range(1, 10):
        if i not in column:
            possible_solutions.append(i)
    return possible_solutions


# check 3x3 region to get possible solutions
def control_region(board, row_index, col_index):
    possible_solutions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    square_row = row_index // 3
    square_column = col_index // 3
    for i in range(square_row * 3, square_row * 3 + 3):
        for j in range(square_column * 3, square_column * 3 + 3):
            if board[i][j] in possible_solutions:
                possible_solutions.remove(board[i][j])
    return possible_solutions


# get possible solutions for a cell
def control(board, row, i):
    possible_solutions = []
    for j in control_row(row):
        if j in control_col(board, i):
            if j in control_region(board, board.index(row), i):
                possible_solutions.append(j)
    return possible_solutions


# solve the sudoku board and write each step to a file
def solve(board, step):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                possible_solutions = control(board, board[i], j)
                if len(possible_solutions) == 1:
                    board[i][j] = possible_solutions[0]
                    write_file(board, possible_solutions[0], i + 1, j + 1, step)
                    step += 1
                    solve(board, step)  # solve again with updated board until sudoku completed


# main function to read input and solve the board
def main():
    if len(sys.argv) != 3:
        print("Usage: python3 sudoku.py <input_file> <output_file>")
        return
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # clear the output file or create one
    with open(output_file, 'w') as file:
        file.write("")

    board = read_file(input_file)
    step = 1
    solve(board, step)
    with open(output_file, 'a') as f:
        f.write("-" * 18)


if __name__ == "__main__":
    main()
