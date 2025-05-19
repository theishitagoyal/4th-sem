PLAYER_X = 'X'  # AI player
PLAYER_O = 'O'  # Human player
EMPTY = ' '

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("---------")

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    return all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))

def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def dfs(board, player):
    if check_winner(board, PLAYER_X):
        return 1
    if check_winner(board, PLAYER_O):
        return -1
    if is_board_full(board):
        return 0

    next_player = PLAYER_O if player == PLAYER_X else PLAYER_X
    scores = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = player
                scores.append(dfs(board, next_player))
                board[i][j] = EMPTY

    return max(scores) if player == PLAYER_X else min(scores)

def find_best_move(board):
    best_score = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                score = dfs(board, PLAYER_O)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

def get_human_move(board):
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == EMPTY:
                return row, col
            else:
                print("Invalid move. Cell is occupied or out of bounds.")
        except ValueError:
            print("Please enter valid integers between 0 and 2.")
PLAYER_X = 'X'  # AI
PLAYER_O = 'O'  # Human
EMPTY = ' '

def print_board(board):
    for i in range(3):
        row_display = []
        for j in range(3):
            cell = board[i][j]
            if cell == EMPTY:
                cell_number = i * 3 + j + 1
                row_display.append(str(cell_number))
            else:
                row_display.append(cell)
        print(" | ".join(row_display))
        if i < 2:
            print("---------")

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    return all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))

def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def dfs(board, player):
    if check_winner(board, PLAYER_X):
        return 1
    if check_winner(board, PLAYER_O):
        return -1
    if is_board_full(board):
        return 0

    next_player = PLAYER_O if player == PLAYER_X else PLAYER_X
    scores = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = player
                scores.append(dfs(board, next_player))
                board[i][j] = EMPTY

    return max(scores) if player == PLAYER_X else min(scores)

def find_best_move(board):
    best_score = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                score = dfs(board, PLAYER_O)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

def get_human_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                row = (move - 1) // 3
                col = (move - 1) % 3
                if board[row][col] == EMPTY:
                    return row, col
                else:
                    print("That cell is already taken.")
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Enter a number from 1 to 9.")

def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    current_player = PLAYER_X  # AI starts

    while True:
        print_board(board)
        print()

        if current_player == PLAYER_X:
            print("AI's turn:")
            row, col = find_best_move(board)
        else:
            print("Your turn:")
            row, col = get_human_move(board)

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

if __name__ == "__main__":
    play_game()

def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    current_player = PLAYER_X  # AI goes first

    while True:
        print_board(board)
        print()

        if current_player == PLAYER_X:
            print("AI's turn:")
            row, col = find_best_move(board)
        else:
            print("Your turn:")
            row, col = get_human_move(board)

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

if __name__ == "__main__":
    play_game()
