
# N-Queens Problem using Manual Backtracking

# Function to check whether position is safe
def is_safe(board, row, col, n):

    # Check same column
    for i in range(row):

        if board[i] == col:
            return False

    # Check left diagonal
    for i, j in zip(range(row - 1, -1, -1),
                    range(col - 1, -1, -1)):

        if board[i] == j:
            return False

    # Check right diagonal
    for i, j in zip(range(row - 1, -1, -1),
                    range(col + 1, n)):

        if board[i] == j:
            return False

    return True


# Function to print chess board
def print_board(board, n):

    print("\nCurrent Chess Board:\n")

    for i in range(n):

        for j in range(n):

            # Print Queen
            if board[i] == j:
                print("Q", end=" ")

            # Empty space
            else:
                print(".", end=" ")

        print()

    print()


# Manual Backtracking Function
def solve_manual_backtracking(n):

    # Initialize board with -1
    board = [-1] * n

    row = 0

    # Continue until all queens are placed
    while row < n:

        # Show current board
        print_board(board, n)

        print(f"Enter column for Row {row} (0 to {n-1})")
        print("Enter -1 to BACKTRACK")

        # Take manual input from user
        col = int(input("Your choice: "))

        # ---------------- BACKTRACKING ----------------
        if col == -1:

            if row == 0:
                print("Cannot backtrack further!")

            else:
                print(f"Backtracking from Row {row} to Row {row-1}")

                # Remove previous queen
                board[row] = -1

                row -= 1

            continue

        # Invalid input
        if col < 0 or col >= n:

            print("Invalid column! Try again.")
            continue

        # Check safe position
        if is_safe(board, row, col, n):

            # Place queen
            board[row] = col

            print(f"Queen placed at ({row}, {col})")

            # Move to next row
            row += 1

        else:
            print("Not Safe! Try again OR press -1 to backtrack.")

    return board


# ---------------- MAIN PROGRAM ----------------

# Take number of queens from user
n = int(input("Enter number of queens (N): "))

# Solve manually using backtracking
solution = solve_manual_backtracking(n)

# Final solution
print("\nFinal Solution:")

print_board(solution, n)

