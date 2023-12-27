import copy

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("--" * 5)

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if is_winner(board, 'X'):
        return -1
    if is_winner(board, 'O'):
        return 1
    if is_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_move = None
    best_eval = float('-inf')

    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        eval = minimax(board, 0, False)
        board[i][j] = ' '

        if eval > best_eval:
            best_eval = eval
            best_move = (i, j)

    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = True  # True for human, False for AI

    while True:
        print_board(board)

        if player_turn:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                player_turn = not player_turn
            else:
                print("Cell already occupied. Try again.")
        else:
            print("AI's turn:")
            move = get_best_move(board)
            board[move[0]][move[1]] = 'O'
            player_turn = not player_turn

        if is_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break
        elif is_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
