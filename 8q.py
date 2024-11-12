def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i = row
    j = col
    while i < 8 and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_n_queen(board, col):
    # Base case: If all queens are placed, return True
    if col == 8:
        solutions.append([row[:] for row in board])
        return True

    # Place this queen in all rows one by one
    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 1

            # Recur to place rest of the queens
            solve_n_queen(board, col + 1)

            # If placing a queen in board[i][col] doesn't lead to a solution, remove the queen
            board[i][col] = 0

    # If queen can not be placed in any row in this column, return False
    return False

def print_solution(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
        print()

solutions = []
board = [[0 for _ in range(8)] for _ in range(8)]
solve_n_queen(board, 0)

print(f"Number of solutions: {len(solutions)}")
print("Solutions:")
for solution in solutions:
    print_solution(solution)
    print()