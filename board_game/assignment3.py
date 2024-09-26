import sys


def read_file(input_file):
    """Reads the input file and returns a list of lists that represents the game board"""
    with open(input_file, 'r') as file:
        board = [[int(i) for i in line if i in "0123456789"] for line in file]
        return board


def display_board(board, score=0):
    """Prints the game board and score to terminal"""
    new_board = ""
    for row in board:
        for i in row:
            new_board += str(i) + " " if i is not None else "  "
        new_board = new_board.rstrip()
        new_board += "\n"
    print(new_board)
    print(f"Your score is: {score}\n")


def control_neighbors(board, row, col, visited=None):
    """Checks the neighbouring cells and returns indexes of the ones with the same value"""
    if visited is None:
        visited = []

    # control left cell
    if col > 0 and (row, col - 1) not in visited and board[row][col] == board[row][col - 1] and board[row][col]:
        visited.append((row, col - 1))
        control_neighbors(board, row, col - 1, visited)

    # control right cell
    if col < len(board[row]) - 1 and (row, col + 1) not in visited and board[row][col] == board[row][col + 1] \
            and board[row][col]:
        visited.append((row, col + 1))
        control_neighbors(board, row, col + 1, visited)

    # control above cell
    if row > 0 and (row - 1, col) not in visited and board[row][col] == board[row - 1][col] and board[row][col]:
        visited.append((row - 1, col))
        control_neighbors(board, row - 1, col, visited)

    # control below cell
    if row < len(board) - 1 and (row + 1, col) not in visited and board[row][col] == board[row + 1][col] \
            and board[row][col]:
        visited.append((row + 1, col))
        control_neighbors(board, row + 1, col, visited)
    return visited


def delete_cells(board, visited):
    """Deletes visited cells and shifts the cells and columns"""
    new_board = [row[:] for row in board]

    # replace the values of the visited cells with None
    for i in visited:
        new_board[i[0]][i[1]] = None

    # shift the cells vertically
    for j in range(len(new_board[0])):
        non_empty_cells = [new_board[k][j] for k in range(len(new_board)) if new_board[k][j] is not None]
        for k in range(len(board) - 1, -1, -1):
            new_board[k][j] = non_empty_cells.pop() if non_empty_cells else None

    # remove empty rows
    new_board = [row for row in new_board if any(cell is not None for cell in row)]

    # shift columns to left
    non_empty_cols = [col for col in range(len(new_board[0])) if any(row[col] is not None for row in new_board)]
    new_board = [[new_board[row][col] for col in non_empty_cols] for row in range(len(new_board))]

    return new_board


def calculate_score(board, visited, score):
    """Calculates the score"""
    score += len(visited) * board[visited[0][0]][visited[0][1]] if visited else 0
    return score


def game_over(board):
    """Checks if the game is over"""
    for i in range(len(board)):
        for j in range(len(board[0])):
            neighbors = control_neighbors(board, i, j)
            if len(neighbors) != 0:
                return False
    return True


def main():
    """main function for taking input, managing gameplay and board updating"""
    if len(sys.argv) != 2:
        print("Usage: python3 assignment3.py <input_file>")
        return
    input_file = sys.argv[1]
    board = read_file(input_file)
    score = 0
    display_board(board, score)
    while not game_over(board):
        user_input = input("Please enter a row and a column number: ")
        print()
        row, col = int(user_input.split(" ", 1)[0]) - 1, int(user_input.split(" ", 1)[1]) - 1
        if row + 1 > len(board) or col + 1 > len(board[0]):
            print("Please enter a correct size!\n")
            continue
        visited = control_neighbors(board, row, col)
        score = calculate_score(board, visited, score)
        new_board = delete_cells(board, visited)
        if board == new_board:
            print("No movement happened try again\n")
        board = new_board
        display_board(board, score)
    print("Game over")


if __name__ == '__main__':
    main()
