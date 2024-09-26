import sys


def read_file(input_file):
    """Reads the input file and returns the constraints and the board as a list of lists."""
    with open(input_file, "r") as file:
        lines = file.readlines()
        constraints = [
            [int(i) for i in line.strip().split(" ") if i != " "] for line in lines[:4]
        ]
        board = [[i for i in line.strip() if i != " "] for line in lines[4:]]
        return constraints, board


def write_file(output_file, result):
    """Writes the board to the output file."""
    with open(output_file, "w") as file:
        output = ""
        if result is not None:
            for row in result:
                output += " ".join(row) + "\n"
        else:
            output = "No solution!"
        file.write(output.strip())


def control_neighbours(board):
    """Checks if there are two adjacent H or B in the board."""
    for row in board:
        for i in range(len(row) - 1):
            if row[i] == row[i + 1] and row[i] in "HB":
                return False

    for i in range(len(board[0])):
        for j in range(len(board) - 1):
            if board[j][i] == board[j + 1][i] and board[j][i] in "HB":
                return False
    return True


def is_complete(board):
    """Checks if the board is complete."""
    for row in board:
        if "L" in row or "U" in row:
            return False
    return True


def control(constraints, board):
    """Checks if there are two adjacent H or B in the board and checks if the board satisfies the constraints."""
    for row_index, row in enumerate(board):
        for i in range(len(row) - 1):
            if row[i] == row[i + 1] and row[i] in "HB":
                return False

        h_count = row.count("H")
        if h_count != constraints[0][row_index] and constraints[0][row_index] != -1:
            return False

        b_count = row.count("B")
        if b_count != constraints[1][row_index] and constraints[1][row_index] != -1:
            return False

    for col_index in range(len(board[0])):
        for j in range(len(board) - 1):
            if (
                board[j][col_index] == board[j + 1][col_index]
                and board[j][col_index] in "HB"
            ):
                return False

        h_count = sum(1 for row in board if row[col_index] == "H")
        if h_count != constraints[2][col_index] and constraints[2][col_index] != -1:
            return False

        b_count = sum(1 for row in board if row[col_index] == "B")
        if b_count != constraints[3][col_index] and constraints[3][col_index] != -1:
            return False

    return True


def solve(constraints, board):
    """Solves the board using backtracking."""

    # If there are two adjacent H or B in the board, return None
    if not control_neighbours(board):
        return None

    # If the board is complete and satisfies the constraints, return the board
    if is_complete(board) and control(constraints, board):
        return board

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] in ("L", "U"):
                for guess in range(3):
                    new_board = [row[:] for row in board]
                    if board[i][j] == "L":
                        new_board[i][j] = (
                            "H" if guess == 0 else "B" if guess == 1 else "N"
                        )
                        new_board[i][j + 1] = (
                            "B" if guess == 0 else "H" if guess == 1 else "N"
                        )
                        result = solve(constraints, new_board)
                    else:  # board[i][j] == "U"
                        new_board[i][j] = (
                            "H" if guess == 0 else "B" if guess == 1 else "N"
                        )
                        new_board[i + 1][j] = (
                            "B" if guess == 0 else "H" if guess == 1 else "N"
                        )
                        result = solve(constraints, new_board)  # Recursive call

                    if result is not None:
                        return result  # If a solution is found, return it

                return None  # Cut the branch if no solution found for the current cell

    return None  # No solution found


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 blind_valley.py input_file output_file")
        return
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    constraints, board = read_file(input_file)

    result = solve(constraints, board)
    write_file(output_file, result)


if __name__ == "__main__":
    main()
