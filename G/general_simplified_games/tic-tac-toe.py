def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_win(board, player):
    """Checks if the current player has won the game."""
    # Check rows, columns, diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    """Checks if the game ended in a draw."""
    return all(cell != ' ' for row in board for cell in row)

def get_player_input(player):
    """Handles player input, ensuring valid input and availability of the cell."""
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter row and column (0, 1, 2) separated by space: ").split())
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid input. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

def main():
    # Initialize the board and player symbols
    board = [[' '] * 3 for _ in range(3)]
    players = ['X', 'O']
    current_player = players[0]

    for _ in range(9):
        print_board(board)
        row, col = get_player_input(current_player)
        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            return

        # Switch to the other player for the next turn
        current_player = players[1] if current_player == players[0] else players[0]

if __name__ == "__main__":
    main()
