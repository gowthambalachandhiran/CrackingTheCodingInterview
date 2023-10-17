def check_winner(board):
    n = len(board)

    # Check rows and columns
    for i in range(n):
        # Check rows
        row = board[i][0]
        if row != ' ':
            for j in range(1, n):
                if board[i][j] != row:
                    break
            else:
                return row

        # Check columns
        col = board[0][i]
        if col != ' ':
            for j in range(1, n):
                if board[j][i] != col:
                    break
            else:
                return col

    # Check diagonals
    diag1 = board[0][0]
    if diag1 != ' ':
        for i in range(1, n):
            if board[i][i] != diag1:
                break
        else:
            return diag1

    diag2 = board[0][n - 1]
    if diag2 != ' ':
        for i in range(1, n):
            if board[i][n - i - 1] != diag2:
                break
        else:
            return diag2

    return None

# Example usage
n = 3  # Change this to the size of your board
board = [
    ['O', 'O', 'O'],
    ['O', 'X', 'O'],
    ['X', 'O', ' ']
]

winner = check_winner(board)
if winner:
    print(f"{winner} wins!")
else:
    print("It's a tie or the game is still ongoing.")